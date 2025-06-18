#!/usr/bin/env python3
"""
Test OCR with the exact same preprocessing as the API
"""

import sys
import os
sys.path.append(os.getcwd())

from main import MCQExtractor
import cv2
import numpy as np
from PIL import Image
import pytesseract

def test_api_ocr():
    """Test OCR with the exact API preprocessing"""
    
    if not os.path.exists("test_mcq.png"):
        print("test_mcq.png not found")
        return
    
    print("Testing OCR with API preprocessing...")
    
    # Use the exact same process as the API
    extractor = MCQExtractor()
    
    # Load image like the API does
    with open("test_mcq.png", 'rb') as f:
        file_content = f.read()
    
    try:
        # Extract text using the exact API method
        text = extractor.extract_text_from_image(file_content)
        
        print("API extracted text:")
        print("="*50)
        print(text)
        print("="*50)
        print(f"Text length: {len(text)}")
        
        # Try to parse MCQs
        mcqs = extractor.parse_mcqs(text)
        print(f"\nFound {len(mcqs)} MCQs")
        
        if mcqs:
            for i, mcq in enumerate(mcqs):
                print(f"\nMCQ {i+1}:")
                print(f"Question: {mcq.get('question', 'N/A')}")
                print(f"Options: {mcq.get('options', {})}")
                print(f"Answer: {mcq.get('correct_answer', 'N/A')}")
        else:
            print("No MCQs found - this explains the API error")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_api_ocr()
