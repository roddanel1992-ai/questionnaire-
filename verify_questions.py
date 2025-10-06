import json
import sys

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

files = [
    'questions_aws_developer.json',
    'questions_aws_ai.json',
    'questions_azure_developer.json',
    'questions_azure_ai.json'
]

print("="*70)
print("QUESTION BANK VERIFICATION")
print("="*70)

total = 0
for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            questions = json.load(file)
            count = len(questions)
            total += count
            print(f"\n{f}")
            print(f"  Questions: {count}")
            print(f"  Status: {'OK' if count == 300 else 'CHECK'}")
            
            # Verify structure
            if count > 0:
                sample = questions[0]
                required_keys = ['question', 'options', 'answer', 'explanation']
                has_all_keys = all(key in sample for key in required_keys)
                print(f"  Structure: {'VALID' if has_all_keys else 'INVALID'}")
    except Exception as e:
        print(f"\n{f}")
        print(f"  ERROR: {e}")

print("\n" + "="*70)
print(f"TOTAL QUESTIONS: {total}")
print("="*70)
print(f"\nTarget per certification: 300")
print(f"Target total: 1,200")
print(f"Achievement: {total / 1200 * 100:.1f}%")
print("\nSTATUS: {'SUCCESS' if total >= 1200 else 'IN PROGRESS'}")

