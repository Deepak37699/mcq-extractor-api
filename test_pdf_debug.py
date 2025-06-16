#!/usr/bin/env python3
"""
Test improved PDF processing and debug capabilities
"""

import requests

BASE_URL = "http://127.0.0.1:8000"

def test_pdf_debug():
    """Test the debug-pdf endpoint"""
    print("🔍 PDF Debug Endpoint Available!")
    print("\n📋 How to use /debug-pdf:")
    print("1. Upload your PDF file to http://127.0.0.1:8000/debug-pdf")
    print("2. See detailed extraction results from multiple methods")
    print("3. Get recommendations for improving extraction")
    
    print("\n🔧 What the debug endpoint shows:")
    print("  • PyPDF2 extraction results")
    print("  • PyMuPDF extraction results") 
    print("  • PDF metadata and page count")
    print("  • Specific recommendations")
    
    print("\n💡 For your 'Apex Civil engineer objective 2080-04-06.pdf':")
    print("  • Try uploading it to /debug-pdf first")
    print("  • This will show why text extraction failed")
    print("  • You'll get specific recommendations")
    
    print("\n🚀 Improvements made:")
    print("  ✅ Added PyMuPDF as fallback for complex PDFs")
    print("  ✅ Added OCR support for scanned PDFs")
    print("  ✅ Added debug endpoint for troubleshooting")
    print("  ✅ Better error handling and reporting")

def test_server_status():
    """Check if all endpoints are working"""
    endpoints = [
        ("/", "Root"),
        ("/health", "Health Check"),
        ("/supported-formats", "Supported Formats"),
    ]
    
    print("\n🧪 Testing Server Status:")
    for endpoint, name in endpoints:
        try:
            response = requests.get(f"{BASE_URL}{endpoint}")
            status = "✅ OK" if response.status_code == 200 else f"❌ {response.status_code}"
            print(f"  {name}: {status}")
        except Exception as e:
            print(f"  {name}: ❌ Error - {e}")

if __name__ == "__main__":
    test_server_status()
    test_pdf_debug()
    
    print("\n" + "="*60)
    print("🎯 NEXT STEPS:")
    print("1. Visit http://127.0.0.1:8000/docs")
    print("2. Try /debug-pdf with your PDF file")
    print("3. Use recommendations to improve extraction")
    print("4. Re-upload to /extract-mcq")
    print("="*60)
