#!/usr/bin/env python3
"""
Quick test of the /extract-mcq endpoint
"""

import requests
import io

BASE_URL = "http://127.0.0.1:8000"

def test_extract_mcq_endpoint():
    """Test the /extract-mcq endpoint with sample data"""
    
    # Sample MCQ content
    sample_mcq = """1. What is the capital of Python programming?
A) Variables
B) Functions
C) Classes
D) Objects
Answer: B

Question: 2
Which of the following is a web framework?
(A) Django
(B) Pandas
(C) NumPy
(D) Matplotlib
Ans: A

Q3: What does API stand for?
A. Application Programming Interface
B. Advanced Programming Interface
C. Automated Programming Interface
D. Applied Programming Interface
Correct: A"""
    
    print("🧪 Testing /extract-mcq endpoint...")
    print("📄 Sample content:")
    print(sample_mcq[:200] + "...")
    
    # Create file-like object
    sample_file = io.BytesIO(sample_mcq.encode('utf-8'))
    files = {"file": ("test_mcq.txt", sample_file, "text/plain")}
    
    try:
        response = requests.post(f"{BASE_URL}/extract-mcq", files=files)
        
        print(f"\n📊 Response:")
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ SUCCESS!")
            print(f"📁 Filename: {data['filename']}")
            print(f"📋 File Type: {data['file_type']}")
            print(f"🔢 Total Questions: {data['total_questions']}")
            
            print(f"\n📝 Extracted MCQs:")
            for i, mcq in enumerate(data.get('mcqs', []), 1):
                print(f"\n{i}. {mcq['question']}")
                for letter, option in mcq['options'].items():
                    marker = "✓" if letter == mcq.get('correct_answer') else " "
                    print(f"   {letter}) {option} {marker}")
                print(f"   Correct Answer: {mcq.get('correct_answer', 'Not detected')}")
                
        else:
            print(f"❌ FAILED")
            print(f"Error: {response.text}")
            
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")

if __name__ == "__main__":
    test_extract_mcq_endpoint()
