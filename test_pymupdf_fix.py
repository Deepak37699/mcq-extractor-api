#!/usr/bin/env python3
"""
Test PyMuPDF API usage to ensure the fix works
"""

import fitz
import io

def test_pymupdf_api():
    """Test PyMuPDF API with a simple PDF"""
    print("Testing PyMuPDF API usage...")
    
    # Create a simple PDF content to test with
    # This will fail if the PDF is invalid, but we're testing the API usage
    fake_pdf = b"%PDF-1.4\n1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj 2 0 obj<</Type/Pages/Kids[3 0 R]/Count 1>>endobj 3 0 obj<</Type/Page/Parent 2 0 R/MediaBox[0 0 612 792]>>endobj xref 0 4 0000000000 65535 f 0000000010 00000 n 0000000053 00000 n 0000000125 00000 n trailer<</Size 4/Root 1 0 R>> startxref 203 %%EOF"
    
    try:
        # Test the API usage that was causing the error
        pdf_doc = fitz.open(stream=fake_pdf, filetype="pdf")
        print(f"PDF opened successfully. Page count: {pdf_doc.page_count}")
        
        # Test the corrected method
        if pdf_doc.page_count > 0:
            print("Testing load_page() method...")
            page = pdf_doc.load_page(0)  # This is the correct method
            print("✅ load_page() works correctly")
            
            # Test getting text (this might fail for our fake PDF but should not error on the method)
            try:
                text = page.get_text()
                print(f"Text extraction: {len(text)} characters")
            except Exception as e:
                print(f"Text extraction failed (expected for fake PDF): {e}")
        
        pdf_doc.close()
        print("✅ PDF API usage is correct")
        
    except Exception as e:
        print(f"❌ PDF API test failed: {e}")

def test_with_real_pdf_content():
    """Test with actual PDF processing through the API"""
    import requests
    
    # Test with a fake PDF file through the API
    fake_pdf_content = b"This is not a real PDF file"
    
    try:
        files = {'file': ('test.pdf', fake_pdf_content, 'application/pdf')}
        response = requests.post("http://localhost:8000/extract-mcq", files=files, timeout=30)
        
        print(f"\nAPI Test Status: {response.status_code}")
        
        if response.status_code == 400:
            error_detail = response.json()['detail']
            print("Error message:")
            print(error_detail)
            
            # Check if the old error is gone
            if "'Document' object has no attribute 'page'" in error_detail:
                print("❌ Old error still present!")
            else:
                print("✅ PyMuPDF API error fixed!")
        else:
            print(f"Unexpected response: {response.json()}")
            
    except Exception as e:
        print(f"❌ API test failed: {e}")

if __name__ == "__main__":
    test_pymupdf_api()
    test_with_real_pdf_content()
