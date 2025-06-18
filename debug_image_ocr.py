#!/usr/bin/env python3
"""
Debug script to see what text is extracted from the test image
"""

import os
import cv2
import numpy as np
from PIL import Image
import pytesseract
import io

def debug_image_ocr():
    """Debug OCR extraction from test image"""
    
    if not os.path.exists("test_mcq.png"):
        print("test_mcq.png not found")
        return
    
    print("Debugging OCR extraction from test_mcq.png...")
    
    # Load image
    image = Image.open("test_mcq.png")
    print(f"Image size: {image.size}")
    print(f"Image mode: {image.mode}")
    
    # Convert to OpenCV format
    opencv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    
    # Preprocess (same as in main.py)
    try:
        # Convert to grayscale
        gray = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2GRAY)
        
        # Apply Gaussian blur to reduce noise
        blurred = cv2.GaussianBlur(gray, (3, 3), 0)
        
        # Apply threshold to get better contrast
        _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        # Apply dilation and erosion to remove noise
        kernel = np.ones((1, 1), np.uint8)
        processed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
        
        print("✅ Image preprocessing successful")
        
        # Try OCR with different PSM modes
        psm_modes = [6, 4, 3, 1]
        
        for psm in psm_modes:
            print(f"\n--- OCR with PSM mode {psm} ---")
            try:
                text = pytesseract.image_to_string(processed, config=f'--psm {psm}')
                print(f"Extracted text length: {len(text)}")
                if text.strip():
                    print("Extracted text (first 500 chars):")
                    print(text[:500])
                    print("..."if len(text) > 500 else "")
                else:
                    print("No text extracted")
            except Exception as e:
                print(f"OCR failed with PSM {psm}: {e}")
        
    except Exception as e:
        print(f"❌ Image preprocessing failed: {e}")

if __name__ == "__main__":
    debug_image_ocr()
