"""
Verify all questions have 4-6 answer options
"""
import json
import sys

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

files = {
    'AWS Developer': 'questions_aws_developer.json',
    'AWS AI': 'questions_aws_ai.json',
    'Azure Developer': 'questions_azure_developer.json',
    'Azure AI': 'questions_azure_ai.json'
}

print("="*70)
print("VERIFYING ANSWER OPTIONS COUNT")
print("="*70)

all_good = True
for name, filepath in files.items():
    with open(filepath, 'r', encoding='utf-8') as f:
        questions = json.load(f)
    
    # Check options count
    option_counts = {}
    issues = 0
    for i, q in enumerate(questions):
        opt_count = len(q.get('options', []))
        option_counts[opt_count] = option_counts.get(opt_count, 0) + 1
        if opt_count < 4:
            print(f"\nISSUE in {name}, Q{i+1}: Only {opt_count} options!")
            issues += 1
            all_good = False
    
    print(f"\n{name} ({len(questions)} questions)")
    print(f"  Option distribution:")
    for count in sorted(option_counts.keys()):
        print(f"    {count} options: {option_counts[count]} questions")
    
    if issues == 0:
        print(f"  ✓ All questions have 4+ options")
    else:
        print(f"  ✗ {issues} questions need fixing")

print("\n" + "="*70)
if all_good:
    print("✓ SUCCESS: All 1,200 questions have 4-6 answer options!")
else:
    print("✗ ISSUES FOUND: Some questions still need fixing")
print("="*70)

