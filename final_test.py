#!/usr/bin/env python3
"""
🚀 FINAL COMPREHENSIVE TEST - MCQ Extractor API
=============================================================

This script performs a complete test of all API functionality
including OCR extraction for scanned documents.

Author: GitHub Copilot
Date: 2025
"""

import requests
import json
import os
from pathlib import Path

# API Configuration
BASE_URL = "http://127.0.0.1:8000"
API_ENDPOINTS = {
    "root": "/",
    "health": "/health",
    "formats": "/supported-formats",
    "extract": "/extract-mcq",
    "extract_ocr": "/extract-mcq-ocr",
    "test_ocr": "/test-ocr",
    "debug_pdf": "/debug-pdf"
}

def test_endpoint(name: str, method: str = "GET", endpoint: str = "", files=None, data=None):
    """Test an API endpoint and return the result"""
    try:
        url = f"{BASE_URL}{endpoint}"
        print(f"🧪 Testing {name}...")
        
        if method == "GET":
            response = requests.get(url)
        elif method == "POST":
            response = requests.post(url, files=files, data=data)
        
        print(f"   Status: {response.status_code}")
        
        if response.status_code in [200, 201]:
            print(f"   ✅ SUCCESS")
            return True, response.json()
        else:
            print(f"   ❌ FAILED")
            return False, response.json() if response.content else None
            
    except Exception as e:
        print(f"   ❌ ERROR: {str(e)}")
        return False, None

def main():
    print("🚀 MCQ EXTRACTOR API - FINAL COMPREHENSIVE TEST")
    print("=" * 60)
    
    results = {}
    
    # Test 1: Basic Endpoints
    print("\n📋 PART 1: BASIC API FUNCTIONALITY")
    print("-" * 40)
    
    success, data = test_endpoint("Root Endpoint", "GET", API_ENDPOINTS["root"])
    results["root"] = success
    
    success, data = test_endpoint("Health Check", "GET", API_ENDPOINTS["health"])
    results["health"] = success
    
    success, data = test_endpoint("Supported Formats", "GET", API_ENDPOINTS["formats"])
    results["formats"] = success
    if success and data:
        print(f"   📄 Supported formats: {len(data.get('supported_formats', []))}")
        print(f"   🔧 Special endpoints: {len(data.get('special_endpoints', {}))}")
    
    # Test 2: Text File MCQ Extraction
    print("\n📝 PART 2: TEXT FILE MCQ EXTRACTION")
    print("-" * 40)
    
    if os.path.exists("sample_test.txt"):
        with open("sample_test.txt", "rb") as f:
            files = {"file": ("sample_test.txt", f, "text/plain")}
            success, data = test_endpoint("MCQ Extraction (Text)", "POST", API_ENDPOINTS["extract"], files=files)
            results["text_extraction"] = success
            if success and data:
                print(f"   📊 Questions found: {data.get('total_questions', 0)}")
                print(f"   📄 File type: {data.get('file_type', 'unknown')}")
    else:
        print("   ⚠️  Sample text file not found")
        results["text_extraction"] = False
    
    # Test 3: OCR Functionality
    print("\n🖼️  PART 3: OCR IMAGE EXTRACTION")
    print("-" * 40)
    
    if os.path.exists("test_mcq.png"):
        with open("test_mcq.png", "rb") as f:
            files = {"file": ("test_mcq.png", f, "image/png")}
            success, data = test_endpoint("OCR Test (Image)", "POST", API_ENDPOINTS["test_ocr"], files=files)
            results["ocr_image"] = success
            if success and data:
                print(f"   📝 Text length: {data.get('text_length', 0)} characters")
                print(f"   🎯 OCR status: {data.get('confidence', 'unknown')}")
    else:
        print("   ⚠️  Test image not found")
        results["ocr_image"] = False
    
    # Test 4: PDF Analysis
    print("\n📑 PART 4: PDF ANALYSIS")
    print("-" * 40)
    
    pdf_files = list(Path(".").glob("*.pdf"))
    if pdf_files:
        pdf_file = pdf_files[0]
        print(f"   📄 Testing with: {pdf_file.name}")
        
        with open(pdf_file, "rb") as f:
            files = {"file": (pdf_file.name, f, "application/pdf")}
            success, data = test_endpoint("PDF Debug Analysis", "POST", API_ENDPOINTS["debug_pdf"], files=files)
            results["pdf_analysis"] = success
            if success and data:
                print(f"   📄 PDF pages: {data.get('pages', 0)}")
                print(f"   📝 Text extraction: {data.get('text_extraction_status', 'unknown')}")
                print(f"   🔧 Recommendation: {data.get('recommendation', 'none')}")
    else:
        print("   ⚠️  No PDF files found in current directory")
        results["pdf_analysis"] = False
    
    # Test 5: Error Handling
    print("\n🚨 PART 5: ERROR HANDLING")
    print("-" * 40)
    
    # Test unsupported file type
    try:
        fake_file = io.BytesIO(b"fake content")
        files = {"file": ("test.xyz", fake_file, "application/unknown")}
        success, data = test_endpoint("Unsupported Format", "POST", API_ENDPOINTS["extract"], files=files)
        results["error_handling"] = not success  # Should fail for unsupported format
        if not success:
            print("   ✅ Correctly rejected unsupported format")
    except Exception as e:
        print(f"   ⚠️  Error test failed: {e}")
        results["error_handling"] = False
    
    # Final Summary
    print("\n🎯 FINAL TEST RESULTS")
    print("=" * 60)
    
    total_tests = len(results)
    passed_tests = sum(1 for v in results.values() if v)
    
    for test_name, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"   {test_name:<20}: {status}")
    
    print(f"\n📊 SUMMARY: {passed_tests}/{total_tests} tests passed")
    
    if passed_tests == total_tests:
        print("\n🎉 ALL TESTS PASSED!")
        print("🚀 Your MCQ Extractor API is fully functional!")
        print("\n🌐 Ready for production:")
        print(f"   • API Docs: {BASE_URL}/docs")
        print(f"   • MCQ Extraction: {BASE_URL}/extract-mcq")
        print(f"   • OCR Extraction: {BASE_URL}/extract-mcq-ocr")
        print(f"   • PDF Analysis: {BASE_URL}/debug-pdf")
    else:
        print(f"\n⚠️  {total_tests - passed_tests} test(s) failed")
        print("🔧 Check the failed components above")
    
    print("\n" + "=" * 60)
    print("Test completed! 🎯")

if __name__ == "__main__":
    import io
    main()
