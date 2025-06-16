#!/usr/bin/env python3
"""
🔧 Test OCR Error Handling and Option Completion
===============================================

This script tests the improved parsing logic specifically
for handling OCR errors and incomplete options.
"""

import requests
import json

def test_ocr_error_handling():
    """Test with OCR errors similar to your PDF"""
    print("🔧 Testing OCR Error Handling")
    print("=" * 50)
    
    # This simulates the OCR errors in your PDF
    test_text_with_errors = """1. Nepal is bordered by which Indian state in the west?
a. Sikkim b. West Bengal
c. Uttarakhand d. Uttar Pradesh

2. How many Hilly districts are there according to new structure of Nepal?
a. 34 b. 35
G. (36 d. 37

3. Mt. Manaslu is located in which district?
a. Myagdi b. Gorakha
c. Kaski d. Solukhumbu

16. How many articles are there in Part 1 of the Constitution of Nepal?
a. 8 b. 7
d. 9

17. How many levels are there in the basic structure of Federal Democratic Republic of Nepal?
a. 2 b. 3"""
    
    # Create test file
    with open("ocr_error_test.txt", "w", encoding="utf-8") as f:
        f.write(test_text_with_errors)
    
    try:
        # Test with API
        with open("ocr_error_test.txt", "rb") as f:
            files = {"file": ("ocr_error_test.txt", f, "text/plain")}
            response = requests.post("http://127.0.0.1:8000/extract-mcq", files=files)
        
        print(f"📡 API Status: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ SUCCESS!")
            print(f"📊 Questions Extracted: {result.get('total_questions', 0)}")
            
            print("\n🔍 OPTION ANALYSIS:")
            print("-" * 40)
            
            for mcq in result.get('mcqs', []):
                q_num = mcq['question_number']
                options = mcq['options']
                option_count = len(options)
                
                print(f"\n📝 Question {q_num}: {option_count} options")
                
                if q_num == 2:  # This should have the OCR error "G. (36"
                    print(f"   🔧 OCR Error Test (should have 4 options): {list(options.keys())}")
                    if 'C' in options:
                        print(f"   ✅ OCR error fixed: C = {options['C']}")
                    else:
                        print(f"   ❌ OCR error not fixed")
                
                if q_num == 16:  # This has missing option C
                    print(f"   🔍 Missing Option Test: {list(options.keys())}")
                    print(f"   Expected: A, B, C, D | Got: {list(options.keys())}")
                
                if q_num == 17:  # This has only 2 options
                    print(f"   ⚠️  Incomplete Options: {list(options.keys())}")
                
                for letter, option in options.items():
                    print(f"     {letter}: {option}")
        
        else:
            print(f"❌ FAILED: {response.text}")
    
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
    
    finally:
        # Cleanup
        import os
        if os.path.exists("ocr_error_test.txt"):
            os.remove("ocr_error_test.txt")

def analyze_pdf_response():
    """Analyze the response from your PDF to identify patterns"""
    print("\n📊 PDF Response Analysis")
    print("=" * 50)
    
    # Based on your response, let's identify the patterns
    issues = [
        {"q": 2, "issue": "Missing C and D options", "text": "G. (36 d. 37"},
        {"q": 16, "issue": "Missing C option", "text": "a. 8 b. 7 d. 9"},
        {"q": 17, "issue": "Only A and B", "text": "a. 2 b. 3"},
        {"q": 30, "issue": "Only A and B", "text": "Missing character"},
        {"q": 34, "issue": "Only A and B", "text": "Number series"},
    ]
    
    print("🔍 Identified Issues:")
    for issue in issues:
        print(f"   Question {issue['q']}: {issue['issue']}")
        print(f"   Likely cause: {issue['text']}")
    
    print("\n💡 Solutions Applied:")
    print("   ✅ OCR error cleaning (G. → c.)")
    print("   ✅ Enhanced option detection")
    print("   ✅ Multiple parsing approaches")
    print("   ✅ Validation and completion")

if __name__ == "__main__":
    print("🚀 OCR ERROR HANDLING TEST")
    print("🔧 Testing improved parsing for incomplete options")
    print("=" * 60)
    
    test_ocr_error_handling()
    analyze_pdf_response()
    
    print("\n" + "=" * 60)
    print("🎯 Next Steps:")
    print("1. Upload your PDF again to test the improvements")
    print("2. Check if more complete options are extracted")
    print("3. Report any remaining issues for further tuning")
    print("=" * 60)
