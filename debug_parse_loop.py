#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main import MCQExtractor
import re

def debug_parse_loop():
    """Debug the exact parse loop logic"""
    
    print("=" * 80)
    print("DEBUGGING PARSE LOOP LOGIC")
    print("=" * 80)
    
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

55. Question with Answer
A) Option A
B) Option B
C) Option C
D) Option D
Answer: B

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
"""
    
    extractor = MCQExtractor()
    
    # Preprocess exactly like the real method
    text = extractor._preprocess_text(test_text)
    lines = text.split('\n')
    clean_lines = []
    for line in lines:
        line = line.strip()
        if line and len(line) > 1:
            clean_lines.append(line)
    
    print(f"Total clean lines: {len(clean_lines)}")
    for i, line in enumerate(clean_lines):
        print(f"  {i:2d}: '{line}'")
    
    print(f"\n" + "=" * 50)
    print("SIMULATING EXACT PARSE LOOP")
    print("=" * 50)
    
    mcqs = []
    i = 0
    loop_count = 0
    
    while i < len(clean_lines):
        loop_count += 1
        if loop_count > 100:  # Safety break
            print("❌ INFINITE LOOP DETECTED!")
            break
            
        line = clean_lines[i]
        print(f"\nLoop {loop_count}: Checking line {i}: '{line}'")
        
        # Check for question patterns with more flexibility
        question_match = None
        question_number = None
        question_text = ""
        
        # Try each pattern
        for pattern_idx, pattern in enumerate(extractor.question_patterns):
            match = re.match(pattern, line)
            if match:
                question_match = match
                print(f"  ✅ QUESTION FOUND with pattern {pattern_idx}: {pattern}")
                if len(match.groups()) == 1:
                    question_text = match.group(1).strip()
                    num_match = re.match(r'^(\d+)', line)
                    question_number = int(num_match.group(1)) if num_match else len(mcqs) + 1
                elif len(match.groups()) == 2:
                    question_number = int(match.group(1))
                    question_text = match.group(2).strip()
                print(f"    Question #{question_number}: '{question_text}'")
                break
        
        if question_match and question_text:
            current_options = {}
            current_answer = None
            
            # Look ahead for options and question continuation
            j = i + 1
            
            print(f"    Looking for options starting from line {j}...")
            
            while j < len(clean_lines):
                if j >= len(clean_lines):
                    break
                    
                next_line = clean_lines[j]
                print(f"      Checking line {j}: '{next_line}'")
                
                # Check if this line contains options
                if extractor._contains_multiple_options(next_line):
                    print(f"        ✅ Multiple options found!")
                    options = extractor._extract_multiple_options(next_line)
                    current_options.update(options)
                    j += 1
                    break
                
                # Check if this is a single option
                is_single_option = False
                for opt_pattern in extractor.option_patterns:
                    option_match = re.match(opt_pattern, next_line)
                    if option_match:
                        option_letter = option_match.group(1).upper()
                        option_text = option_match.group(2).strip()
                        current_options[option_letter] = option_text
                        print(f"        ✅ Option {option_letter}: '{option_text}'")
                        is_single_option = True
                        break
                
                if is_single_option:
                    j += 1
                    continue
                
                # Check if this is a new question
                is_new_question = False
                for pattern in extractor.question_patterns:
                    if re.match(pattern, next_line):
                        is_new_question = True
                        print(f"        ⚠️  New question detected at line {j}")
                        break
                
                if is_new_question:
                    break
                
                # Check for answer
                for pattern in extractor.answer_patterns:
                    match = re.search(pattern, next_line)
                    if match:
                        current_answer = match.group(1).upper()
                        print(f"        ✅ Answer found: {current_answer}")
                        j += 1
                        break
                
                j += 1
            
            print(f"    Final options: {current_options}")
            print(f"    Final answer: {current_answer}")
            
            # Save the question if it has at least one option
            if question_text and current_options:
                mcq = {
                    "question_number": question_number if question_number else len(mcqs) + 1,
                    "question": question_text.strip(),
                    "options": current_options,
                    "correct_answer": current_answer
                }
                mcqs.append(mcq)
                print(f"    ✅ SAVED QUESTION #{mcq['question_number']} with {len(current_options)} options")
            else:
                print(f"    ❌ SKIPPED - No options found")
            
            # Continue from where we left off
            print(f"    Continuing from line {j}")
            i = j
        else:
            print(f"  ❌ No question pattern matched")
            i += 1
    
    print(f"\n" + "=" * 50)
    print("DEBUG RESULTS")
    print("=" * 50)
    print(f"Total loops: {loop_count}")
    print(f"Questions extracted: {len(mcqs)}")
    
    for i, mcq in enumerate(mcqs, 1):
        print(f"  Q{i}: #{mcq['question_number']} - {len(mcq['options'])} options - '{mcq['question'][:50]}...'")
    
    # Compare with actual method
    print(f"\n" + "=" * 50)
    print("COMPARISON WITH ACTUAL METHOD")
    print("=" * 50)
    
    actual_questions = extractor.parse_mcqs(test_text)
    print(f"Actual method extracted: {len(actual_questions)} questions")
    
    for i, q in enumerate(actual_questions, 1):
        print(f"  Q{i}: #{q.get('question_number', 'unknown')} - {len(q.get('options', {}))} options - '{q.get('question', '')[:50]}...'")

if __name__ == "__main__":
    debug_parse_loop()
