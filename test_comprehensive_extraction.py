#!/usr/bin/env python3
"""
🔍 COMPREHENSIVE MCQ EXTRACTION ANALYSIS
=======================================

This script analyzes why questions might be missing and tests
various parsing approaches to maximize question extraction.
"""

import requests
import json
import re

def analyze_text_patterns(text: str):
    """Analyze text patterns to understand why questions might be missed"""
    lines = text.split('\n')
    
    print("🔍 TEXT PATTERN ANALYSIS")
    print("=" * 50)
    
    # Look for all potential question patterns
    question_patterns = [
        r'^\d+\.\s+(.+)',  # 1. Question
        r'^\d+\)\s+(.+)',  # 1) Question  
        r'^\d+\s+(.+)',    # 1 Question
        r'^Q\d+[:\.]?\s+(.+)',  # Q1: Question
        r'^\d+[-\.]\s*(.+)',  # 1- Question or 1. Question
    ]
    
    found_questions = {}
    for pattern_name, pattern in [
        ("Standard (1.)", r'^\d+\.\s+(.+)'),
        ("Parenthesis (1))", r'^\d+\)\s+(.+)'),
        ("No punctuation (1)", r'^\d+\s+(.+)'),
        ("Q format (Q1:)", r'^Q\d+[:\.]?\s+(.+)'),
        ("Dash format (1-)", r'^\d+[-\.]\s*(.+)'),
    ]:
        matches = []
        for i, line in enumerate(lines):
            line = line.strip()
            if re.match(pattern, line):
                # Extract question number
                num_match = re.match(r'^(\d+)', line)
                if num_match:
                    question_num = int(num_match.group(1))
                    matches.append((question_num, line[:80] + "..." if len(line) > 80 else line))
        
        found_questions[pattern_name] = matches
        print(f"📋 {pattern_name}: {len(matches)} questions found")
        if matches:
            print(f"   Range: {min(q[0] for q in matches)} - {max(q[0] for q in matches)}")
            # Show first few
            for q_num, q_text in matches[:3]:
                print(f"   {q_num}: {q_text}")
            if len(matches) > 3:
                print(f"   ... and {len(matches) - 3} more")
    
    # Find the maximum question number
    all_question_numbers = []
    for matches in found_questions.values():
        all_question_numbers.extend([q[0] for q in matches])
    
    if all_question_numbers:
        max_question = max(all_question_numbers)
        total_unique = len(set(all_question_numbers))
        print(f"\n📊 SUMMARY:")
        print(f"   Highest question number found: {max_question}")
        print(f"   Total unique question numbers: {total_unique}")
        print(f"   Expected questions: {max_question}")
        
        # Check for gaps
        expected_range = set(range(1, max_question + 1))
        found_range = set(all_question_numbers)
        missing = expected_range - found_range
        
        if missing:
            print(f"   Missing question numbers: {sorted(list(missing))[:10]}{'...' if len(missing) > 10 else ''}")
        else:
            print(f"   ✅ All question numbers from 1-{max_question} found!")
    
    return found_questions

def test_improved_extraction():
    """Test the improved extraction"""
    print("\n🧪 TESTING IMPROVED EXTRACTION")
    print("=" * 50)
    
    # Create a comprehensive test with various question formats
    test_text = """1. Nepal is bordered by which Indian state in the west?
a. Sikkim b. West Bengal
c. Uttarakhand d. Uttar Pradesh

2. How many Hilly districts are there according to new structure of Nepal?
a. 34 b. 35
c. 36 d. 37

3. Mt. Manaslu is located in which district?
a. Myagdi b. Gorakha
c. Kaski d. Solukhumbu

4) Which river carries the most sand in the world after Huang Ho?
a. Gandaki b. Narayani
c. Koshi d. Karnali

5 Who was the first king to take refuge in Tibet?
a. Narendra Dev b. Udaydev
c. Rajendra Dev d. Mahendra Dev

Q6: What is the capital of Nepal?
a. Kathmandu b. Pokhara
c. Lalitpur d. Bhaktapur

7- When was Nepal declared a republic?
a. 2006 b. 2007
c. 2008 d. 2009

8.Which is the highest mountain in the world?
a. Everest b. K2
c. Kangchenjunga d. Lhotse

50. This is question fifty to test high numbers
a. Option A b. Option B
c. Option C d. Option D

100) This is question one hundred
a. Test A b. Test B
c. Test C d. Test D"""

    # Save to file for testing
    with open("comprehensive_test.txt", "w", encoding="utf-8") as f:
        f.write(test_text)
    
    try:
        # Test with our API
        with open("comprehensive_test.txt", "rb") as f:
            files = {"file": ("comprehensive_test.txt", f, "text/plain")}
            response = requests.post("http://127.0.0.1:8000/extract-mcq-detailed", files=files)
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ API Response Success!")
            print(f"📊 Questions extracted: {result.get('total_questions', 0)}")
            print(f"📊 Complete questions: {result.get('complete_questions', 0)}")
            print(f"📊 Incomplete questions: {result.get('incomplete_questions', 0)}")
            
            print(f"\n📋 Question Numbers Found:")
            mcqs = result.get('mcqs', [])
            question_numbers = [mcq['question_number'] for mcq in mcqs]
            print(f"   Numbers: {sorted(question_numbers)}")
            
            # Check if high numbers are captured
            if 50 in question_numbers:
                print(f"   ✅ High number (50) detected!")
            if 100 in question_numbers:
                print(f"   ✅ Very high number (100) detected!")
                
            # Show option completeness
            print(f"\n📊 Option Statistics:")
            for mcq in mcqs[:5]:  # Show first 5
                q_num = mcq['question_number']
                option_count = len(mcq['options'])
                print(f"   Q{q_num}: {option_count} options")
        
        else:
            print(f"❌ API Error: {response.status_code}")
            print(f"   {response.text}")
    
    except Exception as e:
        print(f"❌ Test Error: {e}")
    
    finally:
        # Cleanup
        import os
        if os.path.exists("comprehensive_test.txt"):
            os.remove("comprehensive_test.txt")

def suggest_improvements():
    """Suggest what might be missing"""
    print(f"\n💡 POTENTIAL IMPROVEMENTS")
    print("=" * 50)
    
    print("🔍 If questions are still missing, it could be:")
    print("   1. 📄 Page breaks splitting questions")
    print("   2. 🖼️  Poor OCR quality on some sections")
    print("   3. 📝 Different formatting patterns we haven't covered")
    print("   4. 🔢 Questions numbered beyond our test range")
    print("   5. 📊 Questions in tables or special layouts")
    
    print(f"\n🔧 Solutions to try:")
    print("   1. Upload your PDF again to test new patterns")
    print("   2. Use /extract-mcq-detailed to see extraction stats")
    print("   3. Check if question numbers go beyond 48")
    print("   4. Look for questions with different numbering styles")

if __name__ == "__main__":
    print("🚀 COMPREHENSIVE MCQ EXTRACTION ANALYSIS")
    print("🎯 Finding out why questions might be missing")
    print("=" * 60)
    
    # Test various question formats
    test_improved_extraction()
    
    # Suggest next steps
    suggest_improvements()
    
    print("\n" + "=" * 60)
    print("🎯 NEXT: Upload your PDF again to test improvements!")
    print("📊 Use /extract-mcq-detailed for full analysis")
    print("=" * 60)
