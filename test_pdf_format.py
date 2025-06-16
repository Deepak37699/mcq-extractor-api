#!/usr/bin/env python3
"""
Test the improved MCQ parsing with PDF-like format
"""

import requests
import io

BASE_URL = "http://127.0.0.1:8000"

def test_pdf_format():
    """Test MCQ extraction with PDF-like format"""
    
    pdf_like_content = """Computer MCQ Test Pdf
Question: 1
Internal hard disk is
(A) Removable but not fixed
(B) Removable
(C) Not fixed
(D) Fixed
Ans: D

Question: 2
The main memory of computer is also called as
(A) Hard-disk
(B) Primary storage
(C) Secondary storage
(D) Internal memory
Ans: B

Question: 3
How much data can be stored in a CD?
(A) 300 MB
(B) 400 MB
(C) 670 MB
(D) 700 MB
Ans: D

Question: 4
CD-ROM stands for
(A) Compactable Read Only Memory
(B) Compact Read Only Memory
(C) Compact Readable Only Memory
(D) Computer Read Only Memory
Ans: B"""
    
    print("🧪 Testing PDF-like format parsing...")
    
    sample_file = io.BytesIO(pdf_like_content.encode('utf-8'))
    files = {"file": ("pdf_format_test.txt", sample_file, "text/plain")}
    
    try:
        response = requests.post(f"{BASE_URL}/extract-mcq", files=files)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ SUCCESS!")
            print(f"Total Questions Found: {data.get('total_questions', 0)}")
            
            for mcq in data.get('mcqs', []):
                print(f"\nQuestion {mcq['question_number']}: {mcq['question']}")
                print(f"Options: {list(mcq['options'].keys())}")
                print(f"Correct Answer: {mcq.get('correct_answer', 'Not detected')}")
        else:
            print(f"❌ FAILED - Status: {response.status_code}")
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")

if __name__ == "__main__":
    test_pdf_format()
