#!/usr/bin/env python3
"""
Debug MCQ Parsing
"""

import re

def debug_mcq_parsing():
    text = """1. What is the capital of France?
A) London
B) Berlin
C) Paris
D) Madrid
Answer: C

2. Which planet is closest to the Sun?
A) Venus
B) Mercury
C) Earth
D) Mars
Ans: B

Q3: What is 2 + 2?
(A) 3
(B) 4
(C) 5
(D) 6
Correct: B

4) What is the largest ocean?
A. Pacific Ocean
B. Atlantic Ocean
C. Indian Ocean
D. Arctic Ocean
Answer: A
"""
    
    question_patterns = [
        r'^\d+\.\s+(.+?)(?=\n[A-D]\)|\n\([A-D]\))',  # 1. Question
        r'^Q\d+[:\.]?\s+(.+?)(?=\n[A-D]\)|\n\([A-D]\))',  # Q1: Question
        r'^\d+\)\s+(.+?)(?=\n[A-D]\)|\n\([A-D]\))',  # 1) Question
    ]
    
    option_patterns = [
        r'^([A-D])\)\s+(.+)',  # A) Option
        r'^\(([A-D])\)\s+(.+)',  # (A) Option
        r'^([A-D])\.\s+(.+)',  # A. Option
    ]
    
    lines = text.split('\n')
    print("Lines in text:")
    for i, line in enumerate(lines):
        print(f"{i+1}: '{line}'")
    
    print("\nTesting question patterns:")
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        for j, pattern in enumerate(question_patterns):
            match = re.match(pattern, line, re.MULTILINE | re.DOTALL)
            if match:
                print(f"Line {i+1}: Pattern {j+1} matched: '{match.group(1)}'")
        
        for j, pattern in enumerate(option_patterns):
            match = re.match(pattern, line)
            if match:
                print(f"Line {i+1}: Option pattern {j+1} matched: {match.group(1)} -> '{match.group(2)}'")

if __name__ == "__main__":
    debug_mcq_parsing()
