#!/usr/bin/env python3

import requests
import json

def test_enhanced_api():
    """Test the enhanced MCQ extraction API endpoint"""
    
    print("=" * 60)
    print("TESTING ENHANCED MCQ EXTRACTION API")
    print("=" * 60)
    
    # API endpoint
    url = "http://localhost:8000/extract-mcq-enhanced"
    
    # Test with our visual content file
    try:
        with open('test_visual_content.txt', 'rb') as f:
            files = {'file': ('test_visual_content.txt', f, 'text/plain')}
            
            print("Sending request to API...")
            response = requests.post(url, files=files)
            
            print(f"Response status: {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                
                print(f"\n✅ SUCCESS! Extracted data:")
                print(f"  - Filename: {data['file_info']['filename']}")
                print(f"  - Total questions: {data['extraction_summary']['total_questions']}")
                print(f"  - Mathematical questions: {data['extraction_summary']['mathematical_questions']}")
                print(f"  - Visual content questions: {data['extraction_summary']['visual_content_questions']}")
                print(f"  - Question type distribution: {data['extraction_summary']['question_type_distribution']}")
                
                print(f"\n📊 Document Analysis:")
                print(f"  - Has mathematical content: {data['document_analysis']['has_mathematical_content']}")
                print(f"  - Has visual content: {data['document_analysis']['has_visual_content']}")
                print(f"  - Tables extracted: {data['document_analysis']['visual_elements']['extracted_tables']}")
                print(f"  - Chart references: {data['document_analysis']['visual_elements']['chart_references']}")
                
                print(f"\n🔍 Individual Questions:")
                for i, mcq in enumerate(data['mcqs'], 1):
                    print(f"  Question {i}:")
                    print(f"    - Type: {mcq.get('question_type', 'unknown')}")
                    print(f"    - Has math: {mcq.get('has_math_content', False)}")
                    print(f"    - Has visual: {mcq.get('has_visual_content', False)}")
                    
                    if mcq.get('has_visual_content') and 'visual_content' in mcq:
                        vc = mcq['visual_content']
                        tables = vc.get('extracted_tables', [])
                        if tables:
                            print(f"    - Tables found: {len(tables)}")
                            for j, table in enumerate(tables):
                                print(f"      Table {j+1}: {table['rows']}x{table['columns']} ({table['type']})")
                        
                        chart_refs = vc.get('chart_references', [])
                        if chart_refs:
                            print(f"    - Chart references: {chart_refs}")
                
                print(f"\n📝 Processing Notes:")
                for note in data.get('processing_notes', []):
                    if note:
                        print(f"  {note}")
                
            else:
                print(f"❌ ERROR: {response.status_code}")
                print(response.text)
                
    except FileNotFoundError:
        print("❌ ERROR: test_visual_content.txt not found")
    except requests.exceptions.ConnectionError:
        print("❌ ERROR: Cannot connect to API. Make sure FastAPI server is running on localhost:8000")
    except Exception as e:
        print(f"❌ ERROR: {e}")

if __name__ == "__main__":
    test_enhanced_api()
