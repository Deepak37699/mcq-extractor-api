#!/usr/bin/env python3
"""
🧪 Test MCQ Extraction with Improved Parsing
==============================================

This script tests the improved MCQ parsing logic specifically
for the format found in your PDF.
"""

import requests
import json

def test_mcq_extraction():
    """Test MCQ extraction with the improved parsing"""
    print("🧪 Testing Improved MCQ Extraction")
    print("=" * 50)
    
    # Test with sample text that matches your PDF format
    sample_text = """1. Nepal is bordered by which Indian state in the west?
a. Sikkim b. West Bengal
c. Uttarakhand d. Uttar Pradesh

2. How many Hilly districts are there according to new structure of Nepal?
a. 34 b. 35
c. 36 d. 37

3. Mt. Manaslu is located in which district?
a. Myagdi b. Gorakha
c. Kaski d. Solukhumbu

4. Which river carries the most sand in the world after Huang Ho?
a. Gandaki b. Narayani
c. Koshi d. Karnali

5. Who was the first king to take refuge in Tibet?
a. Narendra Dev b. Udaydev"""
    
    # Create a temporary test file
    with open("temp_test.txt", "w", encoding="utf-8") as f:
        f.write(sample_text)
    
    # Test the API
    try:
        with open("temp_test.txt", "rb") as f:
            files = {"file": ("temp_test.txt", f, "text/plain")}
            response = requests.post("http://127.0.0.1:8000/extract-mcq", files=files)
        
        print(f"📡 API Response Status: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ SUCCESS!")
            print(f"📊 Total Questions Found: {result.get('total_questions', 0)}")
            print(f"📄 File Type: {result.get('file_type', 'unknown')}")
            
            print("\n🔍 Extracted MCQs:")
            print("-" * 30)
            
            for i, mcq in enumerate(result.get('mcqs', []), 1):
                print(f"\n📝 Question {i}:")
                print(f"   Q: {mcq.get('question', 'N/A')}")
                print(f"   Options:")
                for letter, option in mcq.get('options', {}).items():
                    print(f"     {letter}: {option}")
                answer = mcq.get('correct_answer')
                print(f"   Answer: {answer if answer else 'Not found'}")
        else:
            print(f"❌ FAILED: {response.status_code}")
            print(f"Error: {response.text}")
    
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
    
    finally:
        # Clean up
        import os
        if os.path.exists("temp_test.txt"):
            os.remove("temp_test.txt")

def test_with_actual_pdf():
    """Test with your actual PDF file if available"""
    print("\n🎯 Testing with Your PDF")
    print("=" * 50)
    
    pdf_files = ["Apex Civil engineer objective 2080-04-06.pdf"]
    
    for pdf_file in pdf_files:
        try:
            with open(pdf_file, "rb") as f:
                files = {"file": (pdf_file, f, "application/pdf")}
                response = requests.post("http://127.0.0.1:8000/extract-mcq", files=files)
            
            print(f"📡 Testing: {pdf_file}")
            print(f"📡 Status: {response.status_code}")
            
            if response.status_code == 200:
                result = response.json()
                print(f"✅ SUCCESS!")
                print(f"📊 Total Questions Found: {result.get('total_questions', 0)}")
                
                # Show first few questions as sample
                mcqs = result.get('mcqs', [])
                for i, mcq in enumerate(mcqs[:3], 1):  # Show first 3
                    print(f"\n📝 Question {i}:")
                    print(f"   Q: {mcq.get('question', 'N/A')[:100]}...")
                    print(f"   Options: {len(mcq.get('options', {}))}")
                    answer = mcq.get('correct_answer')
                    print(f"   Answer: {answer if answer else 'Not found'}")
                
                if len(mcqs) > 3:
                    print(f"\n... and {len(mcqs) - 3} more questions")
            else:
                print(f"❌ FAILED: {response.text}")
                
        except FileNotFoundError:
            print(f"⚠️  PDF file not found: {pdf_file}")
        except Exception as e:
            print(f"❌ ERROR: {str(e)}")

if __name__ == "__main__":
    print("🚀 MCQ Extraction Test - Improved Parsing")
    print("🔧 Testing the updated MCQ parsing logic")
    print("=" * 60)
    
    # Test 1: Sample text matching your PDF format
    test_mcq_extraction()
    
    # Test 2: Your actual PDF (if available)
    test_with_actual_pdf()
    
    print("\n" + "=" * 60)
    print("🎯 Test completed!")
    print("📝 If questions are still not extracted properly,")
    print("   we can further adjust the parsing patterns.")
