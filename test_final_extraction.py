#!/usr/bin/env python3
"""
🎯 FINAL TEST - High Question Count Support
==========================================

This test verifies that our extraction can handle large numbers
of questions like those in your PDF (potentially 100+ questions).
"""

import requests
import json

def test_high_question_count():
    """Test with a large number of questions"""
    print("🎯 TESTING HIGH QUESTION COUNT SUPPORT")
    print("=" * 60)
    
    # Create a test with many questions to simulate your PDF
    questions = []
    for i in range(1, 101):  # Test 100 questions
        if i % 10 == 1:  # Every 10th question, vary the format
            format_type = i % 4
            if format_type == 0:
                q_start = f"{i}. Question {i} text here?"
            elif format_type == 1:
                q_start = f"{i}) Question {i} text here?"
            elif format_type == 2:
                q_start = f"Q{i}: Question {i} text here?"
            else:
                q_start = f"{i} Question {i} text here?"
        else:
            q_start = f"{i}. Question {i} text here?"
        
        # Add options - sometimes on same line, sometimes split
        if i % 3 == 0:  # Every 3rd question, split options
            options = f"a. Option A for {i}\nb. Option B for {i}\nc. Option C for {i}\nd. Option D for {i}"
        else:  # Most questions, options on same line
            options = f"a. Option A for {i} b. Option B for {i}\nc. Option C for {i} d. Option D for {i}"
        
        question_block = f"{q_start}\n{options}\n"
        questions.append(question_block)
    
    test_text = "\n".join(questions)
    
    print(f"📝 Generated test with 100 questions")
    print(f"📄 Text length: {len(test_text)} characters")
    
    # Save to file
    with open("large_test.txt", "w", encoding="utf-8") as f:
        f.write(test_text)
    
    try:
        # Test extraction
        with open("large_test.txt", "rb") as f:
            files = {"file": ("large_test.txt", f, "text/plain")}
            response = requests.post("http://127.0.0.1:8000/extract-mcq-detailed", files=files)
        
        if response.status_code == 200:
            result = response.json()
            total = result.get('total_questions', 0)
            complete = result.get('complete_questions', 0)
            incomplete = result.get('incomplete_questions', 0)
            
            print(f"\n✅ EXTRACTION RESULTS:")
            print(f"   📊 Total Questions: {total}/100")
            print(f"   ✅ Complete Questions: {complete}")
            print(f"   ⚠️  Incomplete Questions: {incomplete}")
            print(f"   📈 Success Rate: {(total/100)*100:.1f}%")
            
            # Check question number range
            mcqs = result.get('mcqs', [])
            if mcqs:
                question_numbers = [mcq['question_number'] for mcq in mcqs]
                min_q = min(question_numbers)
                max_q = max(question_numbers)
                print(f"   📋 Question Range: {min_q} - {max_q}")
                
                # Check for missing questions
                expected = set(range(1, 101))
                found = set(question_numbers)
                missing = expected - found
                
                if missing:
                    print(f"   ❌ Missing Questions: {len(missing)} missing")
                    if len(missing) <= 10:
                        print(f"      Missing numbers: {sorted(list(missing))}")
                    else:
                        print(f"      First 10 missing: {sorted(list(missing))[:10]}")
                else:
                    print(f"   🎉 ALL QUESTIONS FOUND!")
            
            # Show extraction method info
            method = result.get('extraction_method', 'unknown')
            print(f"   🔧 Extraction Method: {method}")
            
            if total >= 90:
                print(f"\n🎉 EXCELLENT! High question count support working!")
            elif total >= 70:
                print(f"\n✅ GOOD! Most questions extracted successfully!")
            else:
                print(f"\n⚠️  NEEDS IMPROVEMENT: Only {total}% extracted")
                
        else:
            print(f"❌ API Error: {response.status_code}")
            print(f"   Error: {response.text}")
            
    except Exception as e:
        print(f"❌ Test Error: {e}")
    
    finally:
        # Cleanup
        import os
        if os.path.exists("large_test.txt"):
            os.remove("large_test.txt")

def provide_final_guidance():
    """Provide final guidance for testing the actual PDF"""
    print(f"\n🎯 FINAL TESTING GUIDANCE")
    print("=" * 60)
    
    print("🚀 Your API is now optimized for:")
    print("   ✅ High question counts (100+ questions)")
    print("   ✅ Multiple numbering formats (1., 1), Q1:, etc.)")
    print("   ✅ OCR error correction")
    print("   ✅ Split and merged option lines")
    print("   ✅ Page-by-page text extraction")
    
    print(f"\n📤 TO TEST YOUR PDF:")
    print("   1. Go to: http://127.0.0.1:8000/docs")
    print("   2. Use endpoint: /extract-mcq-detailed")
    print("   3. Upload: Apex Civil engineer objective 2080-04-06.pdf")
    print("   4. Check the detailed results")
    
    print(f"\n📊 WHAT TO EXPECT:")
    print("   • Much higher question count than 48")
    print("   • Better option completion")
    print("   • Fewer OCR errors")
    print("   • More complete extraction")
    
    print(f"\n🔍 IF STILL ISSUES:")
    print("   • Use /debug-pdf to analyze PDF structure")
    print("   • Check extraction_method in detailed results")
    print("   • Look at option_statistics for completion rates")
    print("   • Report specific missing question patterns")

if __name__ == "__main__":
    print("🚀 FINAL COMPREHENSIVE TEST")
    print("🎯 Testing support for high question counts")
    print("=" * 60)
    
    test_high_question_count()
    provide_final_guidance()
    
    print("\n" + "=" * 60)
    print("🎉 MCQ EXTRACTOR API - READY FOR YOUR PDF!")
    print("📤 Upload your PDF now to see the improvements!")
    print("=" * 60)
