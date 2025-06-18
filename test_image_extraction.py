#!/usr/bin/env python3
"""
Test image file extraction to ensure all file types work
"""

import requests
import json
import os

API_URL = "http://localhost:8000"

def test_image_extraction():
    """Test image extraction"""
    print("Testing image extraction...")
    
    if os.path.exists("test_mcq.png"):
        print("Testing with test_mcq.png...")
        
        with open("test_mcq.png", 'rb') as f:
            files = {'file': ('test_mcq.png', f, 'image/png')}
            
            try:
                response = requests.post(f"{API_URL}/extract-mcq", files=files, timeout=60)  # Longer timeout for OCR
                print(f"Status Code: {response.status_code}")
                
                if response.status_code == 200:
                    result = response.json()
                    print("✅ Image extraction successful!")
                    print(f"Found {result['extraction_summary']['total_questions']} questions")
                    print(f"Complete questions: {result['extraction_summary']['complete_questions']}")
                    print(f"Questions with answers: {result['extraction_summary']['questions_with_answers']}")
                else:
                    print("❌ Error:")
                    try:
                        error_detail = response.json()
                        print(f"Error detail: {error_detail}")
                    except:
                        print(f"Response text: {response.text}")
                        
            except requests.exceptions.RequestException as e:
                print(f"❌ Request failed: {e}")
    else:
        print("test_mcq.png not found")

if __name__ == "__main__":
    test_image_extraction()
