#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main import MCQExtractor
import re

def diagnose_extraction_issues():
    """Diagnose MCQ extraction issues and identify patterns"""
    
    print("=" * 80)
    print("DIAGNOSING MCQ EXTRACTION ISSUES")
    print("=" * 80)
    
    # Test with a simple PDF first
    print("\n1. Testing question pattern recognition...")
    
    test_text = """
1. What is the capital of Nepal?
A) Kathmandu
B) Pokhara
C) Chitwan
D) Lalitpur

2. Which river is longest in Nepal?
A) Koshi
B) Gandaki
C) Karnali
D) Mahakali

3. Nepal is bordered by which Indian state in the west?
A) Sikkim
B) West Bengal  
C) Uttarakhand
D) Uttar Pradesh

4. How many Hilly districts are there according to new structure of Nepal?
A) 34
B) 35
C) 36
D) 37

10. Question number jump test
A) Option A
B) Option B
C) Option C
D) Option D

50. Another question
A) Test A
B) Test B
C) Test C
D) Test D

Question 55: Different format
(A) Format test A
(B) Format test B
(C) Format test C
(D) Format test D

99. Near end question
A) Last A
B) Last B
C) Last C
D) Last D

100. Final question
A) Final A
B) Final B
C) Final C
D) Final D
Answer: B
"""
    
    extractor = MCQExtractor()
    
    # Test basic extraction
    questions = extractor.parse_mcqs(test_text)
    print(f"\nBasic test extracted: {len(questions)} questions")
    
    for i, q in enumerate(questions, 1):
        print(f"  Q{i}: #{q.get('question_number', 'unknown')} - {len(q.get('options', {}))} options")
    
    # Test individual patterns
    print(f"\n2. Testing question patterns individually...")
    lines = test_text.split('\n')
    clean_lines = [line.strip() for line in lines if line.strip()]
    
    question_matches = 0
    for i, line in enumerate(clean_lines):
        for j, pattern in enumerate(extractor.question_patterns):
            match = re.match(pattern, line)
            if match:
                question_matches += 1
                print(f"  Line {i}: '{line}' -> Pattern {j}: {pattern}")
                break
    
    print(f"\nTotal question pattern matches: {question_matches}")
    
    # Test option patterns
    print(f"\n3. Testing option patterns...")
    option_matches = 0
    for i, line in enumerate(clean_lines):
        for j, pattern in enumerate(extractor.option_patterns):
            match = re.match(pattern, line)
            if match:
                option_matches += 1
                if option_matches <= 10:  # Show first 10
                    print(f"  Line {i}: '{line}' -> Pattern {j}: {pattern}")
                break
    
    print(f"\nTotal option pattern matches: {option_matches}")
    
    # Test problematic patterns
    print(f"\n4. Testing problematic cases...")
    
    problematic_cases = [
        "Question: 1 What is the answer?",  # PDF format issue
        "1What is the answer?",  # Missing space
        "1. What is the answer? A) Option A B) Option B C) Option C D) Option D",  # Single line
        "Question 1: What is the answer?",  # Different format
        "1) What is the answer?",  # Parenthesis format
        "Q1. What is the answer?",  # Q prefix
        "Question No. 1: What is the answer?",  # Extended format
    ]
    
    for case in problematic_cases:
        matched = False
        for pattern in extractor.question_patterns:
            if re.match(pattern, case):
                print(f"  ✅ '{case}' -> Matched: {pattern}")
                matched = True
                break
        if not matched:
            print(f"  ❌ '{case}' -> No match")
    
    # Test with incomplete questions
    print(f"\n5. Testing incomplete extraction scenarios...")
    
    incomplete_text = """
1. Question with missing options?

2. Question with only some options
A) Option A
B) Option B

3. Complete question
A) Option A
B) Option B  
C) Option C
D) Option D

4. Question with answer immediately
A) Option A
B) Option B
C) Option C
D) Option D
Answer: B

5. Question followed by another question
A) Option A
6. Next question immediately
A) New option A
"""
    
    incomplete_questions = extractor.parse_mcqs(incomplete_text)
    print(f"\nIncomplete test extracted: {len(incomplete_questions)} questions")
    
    for i, q in enumerate(incomplete_questions, 1):
        print(f"  Q{i}: #{q.get('question_number', 'unknown')} - {len(q.get('options', {}))} options - '{q.get('question', '')[:50]}...'")
    
    print(f"\n6. Analyzing extraction method efficiency...")
    
    # Check if the parsing loop is working correctly
    test_lines = test_text.split('\n')
    clean_test_lines = [line.strip() for line in test_lines if line.strip() and len(line.strip()) > 1]
    
    print(f"  Total lines in test: {len(test_lines)}")
    print(f"  Clean lines in test: {len(clean_test_lines)}")
    
    # Simulate the parsing loop
    i = 0
    simulated_questions = 0
    while i < len(clean_test_lines):
        line = clean_test_lines[i]
        
        # Check for question pattern
        question_match = None
        for pattern in extractor.question_patterns:
            match = re.match(pattern, line)
            if match:
                question_match = match
                simulated_questions += 1
                print(f"  Simulated Q{simulated_questions}: Line {i} - '{line}'")
                break
        
        if question_match:
            # Look for options
            j = i + 1
            options_found = 0
            while j < len(clean_test_lines) and j < i + 10:  # Look ahead max 10 lines
                next_line = clean_test_lines[j]
                
                # Check if it's an option
                for pattern in extractor.option_patterns:
                    if re.match(pattern, next_line):
                        options_found += 1
                        break
                
                # Check if it's a new question
                is_new_question = False
                for pattern in extractor.question_patterns:
                    if re.match(pattern, next_line):
                        is_new_question = True
                        break
                
                if is_new_question:
                    break
                    
                j += 1
            
            print(f"    -> Found {options_found} options")
            i = j  # Jump to next potential question
        else:
            i += 1
    
    print(f"\nSimulated extraction would find: {simulated_questions} questions")
    
    return {
        "basic_extraction": len(questions),
        "question_matches": question_matches,
        "option_matches": option_matches,
        "incomplete_extraction": len(incomplete_questions),
        "simulated_questions": simulated_questions
    }

if __name__ == "__main__":
    results = diagnose_extraction_issues()
    
    print(f"\n" + "=" * 80)
    print("DIAGNOSIS SUMMARY")
    print("=" * 80)
    print(f"Basic extraction: {results['basic_extraction']} questions")
    print(f"Question pattern matches: {results['question_matches']}")
    print(f"Option pattern matches: {results['option_matches']}")
    print(f"Incomplete scenario test: {results['incomplete_extraction']} questions")
    print(f"Simulated extraction: {results['simulated_questions']} questions")
    
    if results['basic_extraction'] < results['simulated_questions']:
        print(f"\n⚠️  ISSUE DETECTED: Extraction logic is missing questions!")
        print(f"   Expected: {results['simulated_questions']}")
        print(f"   Actually extracted: {results['basic_extraction']}")
        print(f"   Missing: {results['simulated_questions'] - results['basic_extraction']}")
