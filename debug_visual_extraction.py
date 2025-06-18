#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main import MCQExtractor

def test_visual_extraction():
    """Test visual content extraction with different scenarios"""
    
    extractor = MCQExtractor()
    
    print("=" * 60)
    print("TESTING VISUAL CONTENT EXTRACTION")
    print("=" * 60)
    
    # Test 1: Read from test file
    print("\n1. Testing with test_visual_content.txt:")
    try:
        with open('test_visual_content.txt', 'r', encoding='utf-8') as f:
            content = f.read()
        
        print(f"File content length: {len(content)}")
        print("First 200 chars:")
        print(repr(content[:200]))
        
        visual_result = extractor.detect_visual_content(content)
        print(f"\nVisual detection result:")
        for key, value in visual_result.items():
            print(f"  {key}: {value}")        # Test individual question extraction
        questions = extractor.parse_mcqs(content)
        
        # Enhance with analysis
        if questions:
            questions = extractor.enhance_mcqs_with_analysis(questions)
        
        print(f"\nExtracted {len(questions)} questions")
        
        for i, q in enumerate(questions, 1):
            print(f"\nQuestion {i}:")
            print(f"  Text: {q.get('question', '')[:100]}...")
            print(f"  Question type: {q.get('question_type', 'unknown')}")
            print(f"  Has math content: {q.get('has_math_content', False)}")
            print(f"  Has visual content: {q.get('has_visual_content', False)}")
            
            if 'visual_content' in q and q['visual_content']['has_visual_content']:
                vc = q['visual_content']
                print(f"  Visual analysis:")
                print(f"    - Table references: {len(vc.get('table_references', []))}")
                print(f"    - Chart references: {len(vc.get('chart_references', []))}")
                print(f"    - Extracted tables: {len(vc.get('extracted_tables', []))}")
                
                if vc.get('extracted_tables'):
                    for j, table in enumerate(vc['extracted_tables']):
                        print(f"      Table {j+1}: {table['rows']}x{table['columns']} ({table['type']})")
                        if len(table['data']) > 0:
                            print(f"        Headers: {table['data'][0]}")
            
            if 'math_content' in q and q['math_content']['has_math']:
                mc = q['math_content']
                print(f"  Math analysis:")
                print(f"    - Math symbols: {len(mc.get('math_symbols', []))}")
                print(f"    - Equations: {len(mc.get('equations', []))}")
                print(f"    - Math patterns: {mc.get('math_patterns', [])}")
            
    except Exception as e:
        print(f"Error reading file: {e}")
    
    # Test 2: Single-line table (flattened)
    print("\n" + "=" * 60)
    print("2. Testing with single-line table:")
    
    single_line_table_text = """
2. Based on the following data | City | Population | Area | |------|------------|------| | NYC | 8.4 million| 302 | | LA | 4.0 million| 469 | | Chicago | 2.7 million| 227 | which city has the highest population?
A) New York City
B) Los Angeles  
C) Chicago
D) Houston
Answer: A
"""
    
    print("Testing single-line table text:")
    print(repr(single_line_table_text))
    
    visual_result_single = extractor.detect_visual_content(single_line_table_text)
    print(f"\nSingle-line visual detection result:")
    for key, value in visual_result_single.items():
        print(f"  {key}: {value}")
    
    # Test 3: Multi-line properly formatted table
    print("\n" + "=" * 60)
    print("3. Testing with properly formatted multi-line table:")
    
    multiline_table_text = """
2. Based on the table below, which city has the highest population?

| City | Population | Area |
|------|------------|------|
| NYC  | 8.4 million| 302  |
| LA   | 4.0 million| 469  |
| Chicago | 2.7 million| 227  |

A) New York City
B) Los Angeles  
C) Chicago
D) Houston
Answer: A
"""
    
    print("Testing multi-line table text:")
    print(repr(multiline_table_text[:200]))
    
    visual_result_multi = extractor.detect_visual_content(multiline_table_text)
    print(f"\nMulti-line visual detection result:")
    for key, value in visual_result_multi.items():
        print(f"  {key}: {value}")

if __name__ == "__main__":
    test_visual_extraction()
