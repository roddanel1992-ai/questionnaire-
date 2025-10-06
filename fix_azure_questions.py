"""
Fix Azure questions that have insufficient answer options
All questions should have at least 4 options
"""

import json
import sys
from pathlib import Path

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def check_and_fix_questions(filepath):
    """Check and fix questions with insufficient options"""
    print(f"\n{'='*70}")
    print(f"Checking: {filepath}")
    print('='*70)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        questions = json.load(f)
    
    print(f"Total questions: {len(questions)}")
    
    # Find questions with < 4 options
    issues = []
    for i, q in enumerate(questions):
        options = q.get('options', [])
        if len(options) < 4:
            issues.append((i, q, len(options)))
    
    print(f"Questions with < 4 options: {len(issues)}")
    
    if issues:
        print("\nIssues found:")
        for i, q, opt_count in issues[:5]:
            print(f"  Question {i+1}: '{q['question'][:60]}...' ({opt_count} options)")
        
        # Fix the issues
        print(f"\nFixing {len(issues)} questions...")
        for i, q, opt_count in issues:
            question_text = q['question']
            answer = q['answer']
            options = q['options']
            
            # Generate plausible distractors based on the question type
            if 'Azure' in question_text:
                # Azure service questions
                distractors = [
                    "Azure Virtual Machines",
                    "Azure Storage Account",
                    "Azure Active Directory",
                    "Azure Monitor",
                    "Azure DevOps",
                    "Azure Portal",
                    "Azure Resource Manager",
                    "Azure Logic Apps"
                ]
            elif 'AI' in filepath or 'Cognitive' in question_text:
                # AI/Cognitive services
                distractors = [
                    "Azure Machine Learning",
                    "Azure Cognitive Services",
                    "Computer Vision API",
                    "Speech Service",
                    "Language Understanding",
                    "Text Analytics",
                    "Custom Vision",
                    "Azure Bot Service"
                ]
            else:
                # General distractors
                distractors = [
                    "Configure settings manually",
                    "Use the Azure portal",
                    "Contact Azure support",
                    "Restart the service",
                    "Update the configuration file",
                    "It's not possible",
                    "Use a third-party tool",
                    "Manual deployment only"
                ]
            
            # Make sure answer is in options
            if answer not in options:
                options.insert(0, answer)
            
            # Add distractors until we have 4 options
            for distractor in distractors:
                if len(options) >= 4:
                    break
                if distractor != answer and distractor not in options:
                    options.append(distractor)
            
            # Update the question
            questions[i]['options'] = options[:6]  # Max 6 options (A-F)
        
        # Save fixed questions
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(questions, f, indent=2, ensure_ascii=False)
        
        print(f"✓ Fixed and saved {len(issues)} questions")
    else:
        print("✓ All questions have 4+ options!")
    
    return len(issues)

# Check and fix both Azure files
print("="*70)
print("FIXING AZURE QUESTION OPTIONS")
print("="*70)

azure_dev_issues = check_and_fix_questions('questions_azure_developer.json')
azure_ai_issues = check_and_fix_questions('questions_azure_ai.json')

# Also check AWS files to make sure they're okay
print("\n" + "="*70)
print("VERIFICATION: Checking AWS files too")
print("="*70)

aws_dev_issues = check_and_fix_questions('questions_aws_developer.json')
aws_ai_issues = check_and_fix_questions('questions_aws_ai.json')

print("\n" + "="*70)
print("SUMMARY")
print("="*70)
print(f"Azure Developer: {azure_dev_issues} issues fixed")
print(f"Azure AI: {azure_ai_issues} issues fixed")
print(f"AWS Developer: {aws_dev_issues} issues fixed")
print(f"AWS AI: {aws_ai_issues} issues fixed")
print(f"\nTotal issues fixed: {azure_dev_issues + azure_ai_issues + aws_dev_issues + aws_ai_issues}")
print("\n✓ All questions now have 4-6 answer options!")

