#!/usr/bin/env python3
"""
Debug answer extraction
"""
import re

def test_answer_patterns():
    answer_patterns = [
        r'^Answer:\s*([A-Da-d])',
        r'^Ans:\s*([A-Da-d])',
        r'^Correct:\s*([A-Da-d])',
        r'^Answer\s*[:\-]\s*([A-Da-d])',
        r'^\s*([A-Da-d])\s*$',  # Just a letter on its own line
        r'Answer:\s*([A-Da-d])',  # Answer anywhere in line
        r'Ans:\s*([A-Da-d])',    # Ans anywhere in line
    ]
    
    test_lines = [
        "Answer: A",
        "Answer:A",
        "Answer: B",
        "Ans: C",
        "A",
        "   B   ",
        "The answer is A",
        "Answer: D - This is correct"
    ]
    
    print("Testing answer patterns:")
    for line in test_lines:
        print(f"\nTesting line: '{line}'")
        found = False
        for i, pattern in enumerate(answer_patterns):
            match = re.search(pattern, line)
            if match:
                print(f"  ✅ Pattern {i+1} matched: '{pattern}' -> '{match.group(1)}'")
                found = True
                break
        if not found:
            print(f"  ❌ No pattern matched")

if __name__ == "__main__":
    test_answer_patterns()
