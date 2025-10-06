"""
Upgrade AWS AI questions to professional AWS Solutions Architect level
Replace generic questions with real-world scenario-based questions
"""

import json
import sys

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("="*70)
print("UPGRADING AWS AI QUESTIONS TO PROFESSIONAL LEVEL")
print("="*70)

# Load professional questions
with open('professional_aws_ai_questions.json', 'r', encoding='utf-8') as f:
    professional_questions = json.load(f)

print(f"\nLoaded {len(professional_questions)} professional-grade questions")
print("\nSample professional questions:")
for i, q in enumerate(professional_questions[:3]):
    print(f"\n  Q{i+1}: {q['question'][:100]}...")
    print(f"       Options: {len(q['options'])}, Correct: {q['correctCount']}")

# Load existing AWS AI questions
with open('questions_aws_ai.json', 'r', encoding='utf-8') as f:
    existing_questions = json.load(f)

print(f"\n\nCurrent AWS AI bank: {len(existing_questions)} questions")

# Replace first N questions with professional ones, keep the rest
# This maintains the 300 count while dramatically improving quality
if len(professional_questions) < len(existing_questions):
    # Keep some existing questions and add professional ones
    upgraded_questions = professional_questions + existing_questions[len(professional_questions):]
else:
    upgraded_questions = professional_questions[:300]

print(f"Upgraded bank: {len(upgraded_questions)} questions")
print(f"  - Professional questions: {len(professional_questions)}")
print(f"  - Remaining questions: {max(0, len(upgraded_questions) - len(professional_questions))}")

# Save upgraded questions
with open('questions_aws_ai.json', 'w', encoding='utf-8') as f:
    json.dump(upgraded_questions, f, indent=2, ensure_ascii=False)

print("\n" + "="*70)
print("AWS AI QUESTIONS UPGRADED!")
print("="*70)
print("\nKey improvements:")
print("  ✓ Scenario-based questions (real companies, real problems)")
print("  ✓ Professional wording (like actual AWS exams)")
print("  ✓ Detailed context and requirements")
print("  ✓ Multiple correct answers where appropriate")
print("  ✓ Comprehensive explanations")
print("  ✓ Tests practical knowledge, not just definitions")
print("\nReady for professional AWS certification preparation!")

