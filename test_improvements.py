#!/usr/bin/env python3
"""
Test script to validate the MCQ extraction improvements
"""

import requests
import json
import os
from typing import Dict, List, Any

def test_enhanced_extraction():
    """Test the enhanced MCQ extraction"""
    
    # Test with the sample text that had issues
    sample_text = """
3. Mt. Manaslu is located in which district?
A. Myagdi
B. Gorakha
C. Kaski
D. Solukhumbu

6. When was Sati Practice eliminated from Nepal?
A. BS. 1920
B. BS. 1925
C. BS. 1930
D. BS. 1935

40. A person incurs a loss of 5% by selling a watch for Rs. 1140. At what price should the watch be sold to earn 5% profit?
A. Rs. 1200
B. Rs. 1260
C. Rs. 1300
D. Rs. 1350

Answer Key:
3. B
6. A
40. B
"""

    try:
        # Test the enhanced extraction endpoint
        url = "http://localhost:8000/extract-mcq-enhanced"
        
        # Create a test file
        files = {
            'file': ('test.txt', sample_text.encode(), 'text/plain')
        }
        
        print("🧪 Testing enhanced MCQ extraction...")
        response = requests.post(url, files=files)
        
        if response.status_code == 200:
            result = response.json()
            
            print("✅ Extraction successful!")
            print(f"📊 Total questions extracted: {result['extraction_summary']['total_questions']}")
            print(f"📝 Complete questions: {result['extraction_summary']['complete_questions']}")
            print(f"🎯 Questions with answers: {result['extraction_summary']['questions_with_answers']}")
            
            print("\n📋 EXTRACTED QUESTIONS:")
            for mcq in result['mcqs']:
                print(f"\nQuestion {mcq['question_number']}: {mcq['question'][:60]}...")
                
                print("Options:")
                for opt_key, opt_value in mcq['options'].items():
                    print(f"  {opt_key}. {opt_value}")
                
                answer = mcq.get('correct_answer')
                print(f"Answer: {answer if answer else 'Not found'}")
                
                # Check for extraction issues
                issues = mcq.get('extraction_issues', [])
                if issues:
                    print(f"⚠️ Issues: {', '.join(issues)}")
            
            # Analyze improvements
            print("\n🔍 IMPROVEMENT ANALYSIS:")
            
            # Check for corrupted text
            corrupted_questions = [mcq for mcq in result['mcqs'] if 'corrupted_question' in mcq.get('extraction_issues', [])]
            print(f"🔧 Corrupted questions: {len(corrupted_questions)}")
            
            # Check for incomplete options
            incomplete_options = [mcq for mcq in result['mcqs'] if 'incomplete_options' in mcq.get('extraction_issues', [])]
            print(f"📝 Questions with incomplete options: {len(incomplete_options)}")
            
            # Check answer extraction
            questions_with_answers = sum(1 for mcq in result['mcqs'] if mcq.get('correct_answer'))
            print(f"🎯 Questions with answers found: {questions_with_answers}/{len(result['mcqs'])}")
            
            return True
            
        else:
            print(f"❌ Request failed with status {response.status_code}")
            print(f"Error: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Test failed: {str(e)}")
        return False

def test_corruption_detection():
    """Test the corruption detection logic"""
    
    # Test with corrupted text
    corrupted_text = """
3. s 1 je) a|e]?| jelelelele,
A. 3
B. 4
C. , -2
D. 1
"""

    try:
        url = "http://localhost:8000/extract-mcq-enhanced"
        
        files = {
            'file': ('test_corrupted.txt', corrupted_text.encode(), 'text/plain')
        }
        
        print("\n🧪 Testing corruption detection...")
        response = requests.post(url, files=files)
        
        if response.status_code == 200:
            result = response.json()
            
            corrupted_found = any(
                'corrupted_question' in mcq.get('extraction_issues', []) 
                for mcq in result['mcqs']
            )
            
            if corrupted_found:
                print("✅ Corruption detection working!")
            else:
                print("⚠️ Corruption not detected - may need tuning")
            
            return True
        else:
            print(f"❌ Request failed: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Test failed: {str(e)}")
        return False

def main():
    print("=== MCQ EXTRACTION IMPROVEMENTS TEST ===\n")
    
    # Check if server is running
    try:
        response = requests.get("http://localhost:8000/")
        if response.status_code != 200:
            print("❌ Server not responding correctly")
            return
    except:
        print("❌ Server not running. Please start the FastAPI server first.")
        return
    
    print("✅ Server is running\n")
    
    # Run tests
    test1_success = test_enhanced_extraction()
    test2_success = test_corruption_detection()
    
    print("\n=== TEST SUMMARY ===")
    print(f"Enhanced extraction test: {'✅ PASSED' if test1_success else '❌ FAILED'}")
    print(f"Corruption detection test: {'✅ PASSED' if test2_success else '❌ FAILED'}")
    
    if test1_success and test2_success:
        print("\n🎉 All tests passed! Improvements are working.")
    else:
        print("\n⚠️ Some tests failed. Check the output above for details.")

if __name__ == "__main__":
    main()
