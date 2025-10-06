import json
import re

def clean_text(text):
    """Clean and fix question text"""
    # Remove spam/watermark text
    spam_patterns = [
        r'Passing Certification Exams Made Easy.*?\.com',
        r'Recommend!!.*?Questions?\)',
        r'visit\s*-\s*https?://.*?\.com',
        r'Get the Full DVA-C02 dumps.*?Questions?\)',
        r'Your Partner of IT Exam.*?Questions?\)',
        r'\(127 New Questions?\)',
        r'https?://www\..*?\.com[^\s]*',
    ]
    
    for pattern in spam_patterns:
        text = re.sub(pattern, '', text, flags=re.IGNORECASE | re.DOTALL)
    
    # Fix common truncations
    text = text.replace('functio ', 'function ')
    text = text.replace('bucke ', 'bucket ')
    text = text.replace('clas ', 'class ')
    text = text.replace(' F. ', '. ')
    text = text.replace(' G. ', '. ')
    text = text.replace(' H. ', '. ')
    text = text.replace(' I. ', '. ')
    text = text.replace(' J. ', '. ')
    text = text.replace(' K. ', '. ')
    text = text.replace(' L. ', '. ')
    text = text.replace(' M. ', '. ')
    
    # Remove multiple spaces
    text = re.sub(r'\s+', ' ', text)
    
    return text.strip()

def is_valid_option(option):
    """Check if option is valid"""
    if not option or len(option) < 5:
        return False
    if option.strip() in ['Mastered', 'Not Mastered']:
        return False
    if option.count('.') > 5:  # Too many periods indicates corrupted text
        return False
    return True

def clean_questions(input_file, output_file):
    """Clean all questions"""
    with open(input_file, 'r', encoding='utf-8') as f:
        questions = json.load(f)
    
    cleaned = []
    
    for q in questions:
        # Clean question text
        question_text = clean_text(q['question'])
        
        # Skip if question is too short or too long
        if len(question_text) < 50 or len(question_text) > 800:
            continue
        
        # Clean options
        clean_options = []
        for opt in q['options']:
            clean_opt = clean_text(opt)
            if is_valid_option(clean_opt) and len(clean_opt) < 500:
                clean_options.append(clean_opt)
        
        # Need at least 3 good options
        if len(clean_options) < 3:
            continue
        
        # Clean answer and explanation
        answer = clean_text(q['answer'])
        explanation = clean_text(q.get('explanation', ''))
        
        # Make sure answer is in options
        if answer not in clean_options:
            # Try to find best match
            answer = clean_options[0]
        
        cleaned.append({
            "question": question_text,
            "options": clean_options,
            "answer": answer,
            "explanation": explanation[:1000] if explanation else "Refer to AWS documentation for details."
        })
    
    print(f"Original: {len(questions)} questions")
    print(f"Cleaned: {len(cleaned)} questions")
    print(f"Removed: {len(questions) - len(cleaned)} questions")
    
    # Save cleaned questions
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(cleaned, f, indent=2, ensure_ascii=False)
    
    return len(cleaned)

if __name__ == "__main__":
    count = clean_questions('questions_full.json', 'questions_cleaned.json')
    print(f"\n✅ Created {count} clean questions in questions_cleaned.json")

