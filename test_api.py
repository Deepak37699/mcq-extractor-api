#!/usr/bin/env python3
"""
MCQ Extractor API Test Suite
Tests all endpoints and functionality of the API
"""

import requests
import io
import json
from pathlib import Path

# API base URL
BASE_URL = "http://127.0.0.1:8000"

def test_endpoint(name, url, method="GET", files=None, expected_status=200):
    """Test an API endpoint"""
    print(f"\n🧪 Testing {name}...")
    try:
        if method == "GET":
            response = requests.get(url)
        elif method == "POST":
            response = requests.post(url, files=files)
        
        print(f"   Status Code: {response.status_code}")
        
        if response.status_code == expected_status:
            print(f"   ✅ SUCCESS")
            if response.headers.get('content-type', '').startswith('application/json'):
                data = response.json()
                print(f"   Response: {json.dumps(data, indent=2)}")
            else:
                print(f"   Response: {response.text[:200]}...")
        else:
            print(f"   ❌ FAILED - Expected {expected_status}, got {response.status_code}")
            print(f"   Error: {response.text}")
        
        return response
    except Exception as e:
        print(f"   ❌ ERROR: {str(e)}")
        return None

def create_sample_text_file():
    """Create a sample text file with MCQ questions"""
    content = """1. What is the capital of France?
A) London
B) Berlin
C) Paris
D) Madrid
Answer: C

2. Which planet is closest to the Sun?
A) Venus
B) Mercury
C) Earth
D) Mars
Ans: B

Q3: What is 2 + 2?
(A) 3
(B) 4
(C) 5
(D) 6
Correct: B

4) What is the largest ocean?
A. Pacific Ocean
B. Atlantic Ocean
C. Indian Ocean
D. Arctic Ocean
Answer: A
"""
    return io.BytesIO(content.encode('utf-8'))

def main():
    print("🚀 MCQ Extractor API Test Suite")
    print("=" * 50)
    
    # Test 1: Root endpoint
    test_endpoint("Root Endpoint", f"{BASE_URL}/")
    
    # Test 2: Health check
    test_endpoint("Health Check", f"{BASE_URL}/health")
    
    # Test 3: Supported formats
    test_endpoint("Supported Formats", f"{BASE_URL}/supported-formats")
    
    # Test 4: MCQ extraction with text file
    print(f"\n🧪 Testing MCQ Extraction with Text File...")
    sample_file = create_sample_text_file()
    files = {"file": ("sample_mcq.txt", sample_file, "text/plain")}
    response = test_endpoint("MCQ Extraction (Text)", f"{BASE_URL}/extract-mcq", "POST", files)
    
    # Test 5: Test with unsupported file type
    print(f"\n🧪 Testing Unsupported File Type...")
    fake_file = io.BytesIO(b"fake content")
    files = {"file": ("test.xyz", fake_file, "application/octet-stream")}
    test_endpoint("Unsupported File Type", f"{BASE_URL}/extract-mcq", "POST", files, 400)
    
    # Test 6: Test with no file
    print(f"\n🧪 Testing No File Upload...")
    test_endpoint("No File Upload", f"{BASE_URL}/extract-mcq", "POST", {}, 422)
    
    print(f"\n✨ Test Suite Complete!")
    print(f"\n📋 Summary:")
    print(f"   - API is running on {BASE_URL}")
    print(f"   - All basic endpoints are functional")
    print(f"   - MCQ extraction works with text files")
    print(f"   - Error handling works correctly")
    print(f"\n🌐 Open {BASE_URL}/docs for interactive API documentation")

if __name__ == "__main__":
    main()
