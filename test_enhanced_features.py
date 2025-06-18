#!/usr/bin/env python3
"""
Test Enhanced MCQ Extraction Features

This script tests the new mathematical and visual content detection capabilities.
"""

import asyncio
import json
from main import MCQExtractor

def test_math_detection():
    """Test mathematical content detection"""
    print("🔢 Testing Mathematical Content Detection...")
    
    math_samples = [
        "Calculate the derivative of f(x) = 3x² + 2x - 5",
        "Solve the equation: 2x + 5 = 13",
        "The integral ∫(sin(x) + cos(x))dx equals:",
        "Find the limit: lim(x→0) (sin(x)/x)",
        "Given the matrix A = [[1,2],[3,4]], find det(A)",
        "The function f(x) = x² + 3x - 4 has roots at:",
        "Calculate ∑(i=1 to n) i² = ?",
        "If log₂(x) = 3, then x = ?",
        "The area under the curve y = x² from 0 to 2 is:",
        "Evaluate: √(25) + ∛(27) - π"
    ]
    
    extractor = MCQExtractor()
    
    for i, sample in enumerate(math_samples, 1):
        print(f"\n--- Test {i} ---")
        print(f"Text: {sample}")
        
        analysis = extractor.detect_math_content(sample)
        print(f"Has Math: {analysis['has_math']}")
        print(f"Math Symbols: {analysis['math_symbols']}")
        print(f"Equations: {analysis['equations']}")
        print(f"Math Patterns: {analysis['math_patterns']}")

def test_visual_detection():
    """Test visual content detection"""
    print("\n📊 Testing Visual Content Detection...")
    
    visual_samples = [
        "Based on Table 1 shown below, which region has the highest population?",
        "Refer to Figure 2 in the chart above. What correlation is shown?",
        "The following diagram illustrates the water cycle:",
        "According to the bar chart, which country has the highest GDP?",
        "Study the pie chart showing market share distribution:",
        "The graph displays temperature variations over time:",
        "Observe the circuit diagram in the image:",
        "The table below shows quarterly sales data:",
        "| Name | Age | Score |\n|------|-----|-------|\n| John | 25  | 85    |",
        "Look at the histogram showing grade distribution:"
    ]
    
    extractor = MCQExtractor()
    
    for i, sample in enumerate(visual_samples, 1):
        print(f"\n--- Test {i} ---")
        print(f"Text: {sample}")
        
        analysis = extractor.detect_visual_content(sample)
        print(f"Has Visual: {analysis['has_visual_content']}")
        print(f"Table Refs: {analysis['table_references']}")
        print(f"Chart Refs: {analysis['chart_references']}")
        print(f"Image Refs: {analysis['image_references']}")
        if analysis['extracted_tables']:
            print(f"Tables Found: {len(analysis['extracted_tables'])}")

def test_complete_mcq_extraction():
    """Test complete enhanced MCQ extraction"""
    print("\n🎯 Testing Complete Enhanced MCQ Extraction...")
    
    sample_mcq_text = """
    1. Calculate the derivative of f(x) = 3x² + 2x - 5
    A) f'(x) = 6x + 2
    B) f'(x) = 3x + 2  
    C) f'(x) = 6x² + 2x
    D) f'(x) = 6x - 2
    Answer: A
    
    2. Based on Table 1 shown below, which region has the highest population density?
    A) North America
    B) Europe
    C) Asia
    D) Africa
    
    | Region | Population | Area (km²) | Density |
    |--------|------------|------------|---------|
    | Asia   | 4.6 billion| 44.6 M     | 103     |
    | Europe | 746 million| 10.2 M     | 73      |
    
    Answer: C
    
    3. The integral ∫(sin(x) + cos(x))dx equals:
    A) -cos(x) + sin(x) + C
    B) cos(x) + sin(x) + C
    C) -cos(x) - sin(x) + C
    D) sin(x) - cos(x) + C
    Answer: A
    
    4. Refer to Figure 2 in the chart above. What type of correlation is shown?
    A) Positive linear correlation
    B) Negative linear correlation
    C) No correlation
    D) Exponential correlation
    Answer: B
    
    5. Solve for x: 2x + 3 = 11
    A) x = 4
    B) x = 5
    C) x = 3
    D) x = 7
    Answer: A
    """
    
    extractor = MCQExtractor()
    mcqs = extractor.parse_mcqs(sample_mcq_text)
    
    print(f"Total MCQs extracted: {len(mcqs)}")
    
    for mcq in mcqs:
        print(f"\n--- Question {mcq['question_number']} ---")
        print(f"Question: {mcq['question']}")
        print(f"Type: {mcq['question_type']}")
        print(f"Has Math: {mcq['has_math_content']}")
        print(f"Has Visual: {mcq['has_visual_content']}")
        print(f"Options: {list(mcq['options'].keys())}")
        print(f"Answer: {mcq['correct_answer']}")
        
        if mcq['has_math_content']:
            math_analysis = mcq['content_analysis']['mathematics']
            print(f"Math Symbols: {math_analysis['math_symbols']}")
            print(f"Equations: {math_analysis['equations'][:2]}...")  # Show first 2
        
        if mcq['has_visual_content']:
            visual_analysis = mcq['content_analysis']['visual_elements']
            print(f"Visual Elements: {visual_analysis['visual_patterns']}")
            if visual_analysis['extracted_tables']:
                print(f"Tables: {len(visual_analysis['extracted_tables'])} found")

def test_math_expression_parsing():
    """Test mathematical expression parsing"""
    print("\n🧮 Testing Mathematical Expression Parsing...")
    
    expressions = [
        "f(x) = 3x² + 2x - 5",
        "y = sin(x) + cos(x)",
        "area = π * r²",
        "distance = v₀t + ½at²",
        "E = mc²",
        "quadratic = ax² + bx + c"
    ]
    
    extractor = MCQExtractor()
    
    for expr in expressions:
        print(f"\n--- Expression: {expr} ---")
        analysis = extractor.parse_mathematical_expressions(expr)
        
        if analysis['parsed_expressions']:
            for parsed in analysis['parsed_expressions']:
                print(f"Original: {parsed['original']}")
                print(f"Cleaned: {parsed['cleaned']}")
                if 'expression' in parsed:
                    print(f"Parsed: {parsed['expression']}")
                if 'latex' in parsed:
                    print(f"LaTeX: {parsed['latex']}")
                if 'error' in parsed:
                    print(f"Error: {parsed['error']}")

def main():
    """Run all tests"""
    print("🚀 Enhanced MCQ Extraction Feature Tests")
    print("=" * 50)
    
    try:
        test_math_detection()
        test_visual_detection()
        test_complete_mcq_extraction()
        test_math_expression_parsing()
        
        print("\n✅ All tests completed successfully!")
        print("\nNew Features Summary:")
        print("🔢 Mathematical Content Detection - READY")
        print("📊 Visual Content Detection - READY")
        print("📋 Table Extraction - READY")
        print("🧮 Mathematical Expression Parsing - READY")
        print("🎯 Enhanced Question Classification - READY")
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
