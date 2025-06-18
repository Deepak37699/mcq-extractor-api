#!/usr/bin/env python3
"""
Test script to verify the PDF extraction error fix
"""

import requests
import json
import os

# Test the API endpoint
API_URL = "http://localhost:8000"

def test_pdf_extraction():
    """Test PDF extraction with error handling"""
    print("Testing PDF extraction with improved error handling...")
    
    # Test with a sample PDF if available
    sample_files = [
        "sample_test.txt",  # Start with text file to ensure server is working
    ]
    
    for filename in sample_files:
        if os.path.exists(filename):
            print(f"\nTesting with {filename}...")
            
            with open(filename, 'rb') as f:
                files = {'file': (filename, f, 'application/octet-stream')}
                
                try:
                    response = requests.post(f"{API_URL}/extract-mcq", files=files, timeout=30)
                    print(f"Status Code: {response.status_code}")
                    
                    if response.status_code == 200:
                        result = response.json()
                        print("✅ Success!")
                        print(f"Found {result['extraction_summary']['total_questions']} questions")
                    else:
                        print("❌ Error:")
                        try:
                            error_detail = response.json()
                            print(f"Error detail: {error_detail}")
                        except:
                            print(f"Response text: {response.text}")
                            
                except requests.exceptions.RequestException as e:
                    print(f"❌ Request failed: {e}")
        else:
            print(f"File {filename} not found, skipping...")

def test_error_message_format():
    """Test that error messages are properly formatted (not nested)"""
    print("\n" + "="*50)
    print("Testing error message format...")
    
    # Create a fake/invalid file to test error handling
    fake_content = b"This is not a valid PDF file content"
    
    files = {'file': ('test.pdf', fake_content, 'application/pdf')}
    
    try:
        response = requests.post(f"{API_URL}/extract-mcq", files=files, timeout=30)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code != 200:
            error_response = response.json()
            print("Error Response:", error_response)
            
            # Check if the error message is properly formatted (not nested)
            detail = error_response.get('detail', '')
            if 'Error processing file: 400:' in detail:
                print("❌ Still has nested error format!")
            else:
                print("✅ Error format looks good!")
                
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")

if __name__ == "__main__":
    print("Testing PDF Extraction Fix")
    print("="*50)
    
    # Test basic functionality
    test_pdf_extraction()
    
    # Test error message format
    test_error_message_format()
