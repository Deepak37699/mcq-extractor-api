#!/usr/bin/env python3
"""
Test the MCQ parsing with the exact OCR text from the image
"""

import sys
import os

# Add the current directory to Python path to import main
sys.path.append(os.getcwd())

# Import the MCQExtractor class
from main import MCQExtractor

def test_mcq_parsing():
    """Test MCQ parsing with OCR text"""
    
    # Exact OCR text from the image
    ocr_text = """1. What is 2 ¢ 27
A)3
B)4
cs
oe
Answer. B"""
    
    print("Testing MCQ parsing with OCR text:")
    print("="*50)
    print("Input text:")
    print(ocr_text)
    print("="*50)
    
    # Initialize MCQ extractor
    extractor = MCQExtractor()
    
    # Parse MCQs
    mcqs = extractor.parse_mcqs(ocr_text)
    
    print(f"Found {len(mcqs)} MCQs")
    
    if mcqs:
        for i, mcq in enumerate(mcqs):
            print(f"\nMCQ {i+1}:")
            print(f"Question: {mcq.get('question', 'N/A')}")
            print(f"Options: {mcq.get('options', {})}")
            print(f"Answer: {mcq.get('correct_answer', 'N/A')}")
            print(f"Type: {mcq.get('question_type', 'N/A')}")
    else:
        print("No MCQs found. Let's debug the parsing...")
        
        # Test question detection
        print("\nDebugging question detection:")
        for pattern in extractor.question_patterns:
            import re
            matches = re.findall(pattern, ocr_text, re.MULTILINE)
            if matches:
                print(f"Pattern '{pattern}' found: {matches}")
        
        # Test option detection
        print("\nDebugging option detection:")
        for pattern in extractor.option_patterns:
            matches = re.findall(pattern, ocr_text, re.MULTILINE)
            if matches:
                print(f"Pattern '{pattern}' found: {matches}")
        
        # Test answer detection
        print("\nDebugging answer detection:")
        for pattern in extractor.answer_patterns:
            matches = re.findall(pattern, ocr_text, re.MULTILINE)
            if matches:
                print(f"Pattern '{pattern}' found: {matches}")

if __name__ == "__main__":
    test_mcq_parsing()
