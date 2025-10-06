"""
Analyze AWS questions quality and identify improvements needed
"""
import json
import sys

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def analyze_question_quality(filepath, cert_name):
    with open(filepath, 'r', encoding='utf-8') as f:
        questions = json.load(f)
    
    print(f"\n{'='*70}")
    print(f"Analyzing: {cert_name}")
    print('='*70)
    
    issues = {
        'too_simple': [],
        'no_scenario': [],
        'poor_wording': [],
        'unrealistic': [],
        'good': []
    }
    
    for i, q in enumerate(questions[:50]):  # Check first 50
        question_text = q['question']
        
        # Check for quality issues
        if len(question_text) < 50:
            issues['too_simple'].append((i+1, question_text[:60]))
        elif not any(word in question_text.lower() for word in ['developer', 'application', 'company', 'need', 'want', 'require']):
            issues['no_scenario'].append((i+1, question_text[:60]))
        elif question_text.startswith('What is') or question_text.startswith('Which service'):
            issues['poor_wording'].append((i+1, question_text[:60]))
        else:
            issues['good'].append((i+1, question_text[:60]))
    
    print(f"\nQuality Assessment (first 50 questions):")
    print(f"  Good questions: {len(issues['good'])} ({len(issues['good'])/50*100:.0f}%)")
    print(f"  Too simple/short: {len(issues['too_simple'])} ({len(issues['too_simple'])/50*100:.0f}%)")
    print(f"  No scenario: {len(issues['no_scenario'])} ({len(issues['no_scenario'])/50*100:.0f}%)")
    print(f"  Poor wording: {len(issues['poor_wording'])} ({len(issues['poor_wording'])/50*100:.0f}%)")
    
    print(f"\nExamples of issues found:")
    if issues['too_simple']:
        print(f"\n  Too Simple:")
        for i, text in issues['too_simple'][:3]:
            print(f"    Q{i}: {text}...")
    
    if issues['poor_wording']:
        print(f"\n  Poor Wording:")
        for i, text in issues['poor_wording'][:3]:
            print(f"    Q{i}: {text}...")
    
    return issues

print("="*70)
print("AWS QUESTIONS QUALITY ANALYSIS")
print("="*70)

aws_dev_issues = analyze_question_quality('questions_aws_developer.json', 'AWS Developer (DVA-C02)')
aws_ai_issues = analyze_question_quality('questions_aws_ai.json', 'AWS AI Practitioner (AIF-C01)')

print("\n" + "="*70)
print("RECOMMENDATION")
print("="*70)
print("Need to rewrite questions to be:")
print("  1. Scenario-based (real-world situations)")
print("  2. Professional wording (like actual AWS exams)")
print("  3. Detailed and specific (not generic)")
print("  4. Include context (company needs, requirements)")
print("  5. Test practical knowledge (not just definitions)")

