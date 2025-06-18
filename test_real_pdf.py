#!/usr/bin/env python3
"""
Create a minimal valid PDF for testing
"""

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

def create_test_pdf():
    """Create a simple PDF with MCQ content for testing"""
    buffer = io.BytesIO()
    
    # Create a PDF with reportlab
    p = canvas.Canvas(buffer, pagesize=letter)
    
    # Add some MCQ content
    p.drawString(100, 750, "Sample MCQ Test")
    p.drawString(100, 720, "")
    p.drawString(100, 700, "1. What is the capital of France?")
    p.drawString(120, 680, "A) London")
    p.drawString(120, 660, "B) Berlin") 
    p.drawString(120, 640, "C) Paris")
    p.drawString(120, 620, "D) Madrid")
    p.drawString(100, 600, "Answer: C")
    p.drawString(100, 580, "")
    p.drawString(100, 560, "2. Which planet is closest to the Sun?")
    p.drawString(120, 540, "A) Venus")
    p.drawString(120, 520, "B) Mercury")
    p.drawString(120, 500, "C) Earth")
    p.drawString(120, 480, "D) Mars")
    p.drawString(100, 460, "Answer: B")
    
    p.save()
    
    # Get the PDF content
    buffer.seek(0)
    return buffer.read()

def test_real_pdf_extraction():
    """Test PDF extraction with a real PDF"""
    try:
        # Create a test PDF
        pdf_content = create_test_pdf()
        print(f"Created test PDF: {len(pdf_content)} bytes")
        
        # Save it to a file for testing
        with open("test_sample.pdf", "wb") as f:
            f.write(pdf_content)
        print("Saved test PDF as test_sample.pdf")
        
        # Test through the API
        import requests
        
        files = {'file': ('test_sample.pdf', pdf_content, 'application/pdf')}
        response = requests.post("http://localhost:8000/extract-mcq", files=files, timeout=30)
        
        print(f"\nAPI Response Status: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print("✅ PDF extraction successful!")
            print(f"Questions found: {result['extraction_summary']['total_questions']}")
            print(f"Questions with answers: {result['extraction_summary']['questions_with_answers']}")
            
            # Show the extracted questions
            for i, mcq in enumerate(result['mcqs']):
                print(f"\nQuestion {i+1}: {mcq['question']}")
                print(f"Options: {mcq['options']}")
                print(f"Answer: {mcq.get('correct_answer', 'Not found')}")
        else:
            print("❌ PDF extraction failed:")
            print(response.json())
            
    except ImportError:
        print("⚠️  reportlab not installed. Install with: pip install reportlab")
        print("Testing with existing sample file instead...")
        
        # Alternative: test with any PDF file if available
        pdf_files = ["sample_test.pdf", "test.pdf", "sample.pdf"]
        for pdf_file in pdf_files:
            import os
            if os.path.exists(pdf_file):
                print(f"Testing with existing file: {pdf_file}")
                with open(pdf_file, 'rb') as f:
                    content = f.read()
                
                import requests
                files = {'file': (pdf_file, content, 'application/pdf')}
                response = requests.post("http://localhost:8000/extract-mcq", files=files, timeout=30)
                print(f"Status: {response.status_code}")
                if response.status_code == 200:
                    result = response.json()
                    print(f"✅ Found {result['extraction_summary']['total_questions']} questions")
                else:
                    print(f"Response: {response.json()}")
                break
        else:
            print("No PDF files found for testing")
            
    except Exception as e:
        print(f"❌ Test failed: {e}")

if __name__ == "__main__":
    test_real_pdf_extraction()
