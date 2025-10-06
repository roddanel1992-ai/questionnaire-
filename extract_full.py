import pdfplumber
import json
import re
from pathlib import Path

def clean_spam_text(text):
    """Remove spam/advertisement text"""
    spam_patterns = [
        r'Passing Certification Exams Made Easy.*?\.com',
        r'Recommend!!.*?Questions?\)',
        r'visit\s*-\s*https?://www\..*?\.com',
        r'Get the Full DVA-C02 dumps.*?Questions?\)',
        r'https?://www\.surepassexam\.com[^\s]*',
        r'https?://www\.exambible\.com[^\s]*',
        r'Your Partner of IT Exam.*?Questions?\)',
        r'\(127 New Questions?\)',
    ]
    
    for pattern in spam_patterns:
        text = re.sub(pattern, '', text, flags=re.IGNORECASE | re.DOTALL)
    
    return text.strip()

def extract_questions_from_pdf(pdf_path):
    """Extract questions from AWS exam PDF"""
    questions = []
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            full_text = ""
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    full_text += page_text + "\n"
            
            print(f"  Total text length: {len(full_text)} characters")
            
            # Split by "NEW QUESTION" marker
            # Use a pattern that captures the question number
            parts = re.split(r'(NEW QUESTION \d+)', full_text, flags=re.IGNORECASE)
            
            # Combine headers with their content
            question_blocks = []
            for i in range(1, len(parts), 2):
                if i+1 < len(parts):
                    question_blocks.append(parts[i] + parts[i+1])
            
            print(f"  Found {len(question_blocks)} question blocks")
            
            for block_idx, block in enumerate(question_blocks, 1):
                if len(block.strip()) < 50:
                    continue
                
                try:
                    # Clean spam
                    block_clean = clean_spam_text(block)
                    
                    # Find Answer: line
                    answer_match = re.search(r'\n\s*Answer:\s*([A-E])(?:\s|$)', block_clean, re.IGNORECASE)
                    if not answer_match:
                        continue
                    
                    correct_letter = answer_match.group(1).upper()
                    answer_pos = answer_match.start()
                    
                    # Split into question+options and explanation
                    question_section = block_clean[:answer_pos].strip()
                    explanation_section = block_clean[answer_pos:].strip()
                    
                    # Extract explanation
                    explanation_match = re.search(r'Explanation:\s*(.+?)(?=References:|NEW QUESTION|$)', 
                                                  explanation_section, re.IGNORECASE | re.DOTALL)
                    explanation = ""
                    if explanation_match:
                        explanation = explanation_match.group(1).strip()
                        explanation = clean_spam_text(explanation)
                        explanation = re.sub(r'\s+', ' ', explanation)[:1500]
                    
                    # Extract options - look for patterns like "A. text" or "A text" before "B."
                    # More flexible pattern to handle various formats
                    option_pattern = r'([A-E])[\.\)]\s*([^\n]+(?:\n(?![A-E][\.\)])[^\n]+)*)'
                    option_matches = list(re.finditer(option_pattern, question_section))
                    
                    if not option_matches or len(option_matches) < 2:
                        # Try alternative pattern - options may be on new lines
                        lines = question_section.split('\n')
                        options_dict = {}
                        for line in lines:
                            opt_match = re.match(r'^\s*([A-E])[\.\)]\s*(.+)$', line.strip())
                            if opt_match:
                                letter = opt_match.group(1).upper()
                                text = opt_match.group(2).strip()
                                if text and len(text) > 2:
                                    options_dict[letter] = text
                        
                        if len(options_dict) >= 2:
                            # Find question text (before first option)
                            question_text = question_section
                            for letter in sorted(options_dict.keys()):
                                pos = question_section.find(f'{letter}.')
                                if pos == -1:
                                    pos = question_section.find(f'{letter})')
                                if pos != -1:
                                    question_text = question_section[:pos]
                                    break
                            
                            question_text = clean_spam_text(question_text.strip())
                            question_text = re.sub(r'\s+', ' ', question_text)
                            question_text = re.sub(r'^NEW QUESTION \d+\s*', '', question_text, flags=re.IGNORECASE)
                            
                            if len(question_text) < 20:
                                continue
                            
                            # Build options list
                            options = [options_dict.get(l, '') for l in sorted(options_dict.keys())]
                            options = [clean_spam_text(opt) for opt in options if opt]
                            options = [re.sub(r'\s+', ' ', opt) for opt in options]
                            
                            # Get correct answer text
                            correct_idx = ord(correct_letter) - ord('A')
                            if correct_idx < len(options):
                                correct_answer = options[correct_idx]
                            else:
                                correct_answer = options[0]  # Fallback
                            
                            question_obj = {
                                "question": question_text[:1200],
                                "options": options[:5],  # Max 5 options (A-E)
                                "answer": correct_answer,
                                "explanation": explanation if explanation else "No explanation provided."
                            }
                            
                            questions.append(question_obj)
                            continue
                    
                    # Original method with regex matches
                    if option_matches and len(option_matches) >= 2:
                        # Find question text (before first option)
                        first_option_pos = option_matches[0].start()
                        question_text = question_section[:first_option_pos].strip()
                        question_text = clean_spam_text(question_text)
                        question_text = re.sub(r'\s+', ' ', question_text)
                        question_text = re.sub(r'^NEW QUESTION \d+\s*', '', question_text, flags=re.IGNORECASE)
                        
                        if len(question_text) < 20:
                            continue
                        
                        # Build options list
                        options = []
                        for match in option_matches[:5]:  # Max 5 options (A-E)
                            option_text = match.group(2).strip()
                            option_text = clean_spam_text(option_text)
                            option_text = re.sub(r'\s+', ' ', option_text)
                            if option_text and len(option_text) > 2:
                                options.append(option_text)
                        
                        if len(options) < 2:
                            continue
                        
                        # Get correct answer text
                        correct_idx = ord(correct_letter) - ord('A')
                        if correct_idx < len(options):
                            correct_answer = options[correct_idx]
                        else:
                            correct_answer = options[0]
                        
                        question_obj = {
                            "question": question_text[:1200],
                            "options": options,
                            "answer": correct_answer,
                            "explanation": explanation if explanation else "No explanation provided."
                        }
                        
                        questions.append(question_obj)
                    
                except Exception as e:
                    print(f"    Error in block {block_idx}: {str(e)[:50]}")
                    continue
                    
    except Exception as e:
        print(f"  Error processing {pdf_path}: {e}")
    
    return questions

def remove_duplicates(questions):
    """Remove duplicate questions"""
    seen = set()
    unique = []
    
    for q in questions:
        # Normalize for comparison
        key = re.sub(r'\s+', ' ', q['question'].lower().strip())[:200]
        
        if key not in seen:
            seen.add(key)
            unique.append(q)
    
    return unique

def main():
    pdf_folder = Path("exam_questions with answers")
    pdf_files = sorted(list(pdf_folder.glob("*.pdf")))
    
    print(f"Found {len(pdf_files)} PDF files\n")
    
    all_questions = []
    
    for pdf_file in pdf_files:
        print(f"Processing {pdf_file.name}...")
        questions = extract_questions_from_pdf(pdf_file)
        all_questions.extend(questions)
        print(f"  [OK] Extracted {len(questions)} questions")
        print(f"  Total so far: {len(all_questions)}\n")
    
    if not all_questions:
        print("\n[ERROR] No questions were extracted!")
        return
    
    # Remove duplicates
    print(f"Removing duplicates...")
    unique_questions = remove_duplicates(all_questions)
    print(f"  Before: {len(all_questions)} questions")
    print(f"  After: {len(unique_questions)} unique questions")
    print(f"  Removed: {len(all_questions) - len(unique_questions)} duplicates\n")
    
    # Save to JSON
    output_file = "questions_full.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(unique_questions, f, indent=2, ensure_ascii=False)
    
    print(f"[SUCCESS] Extracted {len(unique_questions)} unique questions!")
    print(f"[SAVED] Saved to {output_file}\n")
    
    # Show sample
    if unique_questions:
        print("--- Sample Question #1 ---")
        q = unique_questions[0]
        print(f"Q: {q['question'][:120]}...")
        print(f"Options ({len(q['options'])}):")
        for i, opt in enumerate(q['options'][:3]):
            print(f"  {chr(65+i)}. {opt[:70]}...")
        print(f"Answer: {q['answer'][:70]}...\n")
        
        if len(unique_questions) > 10:
            print("--- Sample Question #10 ---")
            q = unique_questions[9]
            print(f"Q: {q['question'][:120]}...")
            print(f"Options: {len(q['options'])}")
            print(f"Answer: {q['answer'][:70]}...")

if __name__ == "__main__":
    main()


