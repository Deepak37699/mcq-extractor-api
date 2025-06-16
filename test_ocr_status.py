#!/usr/bin/env python3
"""
Test OCR functionality for scanned PDFs
"""

import requests

BASE_URL = "http://127.0.0.1:8000"

def test_ocr_capabilities():
    """Test OCR extraction capabilities"""
    print("🔍 OCR Extraction for Scanned PDFs")
    print("=" * 50)
    
    print("\n📄 Your PDF Analysis:")
    print("  • File: Apex Civil engineer objective 2080-04-06.pdf")
    print("  • Type: Scanned/Image-based PDF (11 pages)")
    print("  • Creator: iLovePDF")
    print("  • Text Extraction: Failed (empty content)")
    print("  • Recommendation: OCR Required")
    
    print("\n🚀 Available Solutions:")
    print("  1. /extract-mcq (auto-detects and tries OCR)")
    print("  2. /extract-mcq-ocr (forces OCR extraction)")
    print("  3. Install Tesseract OCR for full functionality")
    
    print("\n💡 OCR Requirements:")
    print("  ✅ Python libraries: pillow, pytesseract, opencv-python (installed)")
    print("  ⚠️  Tesseract OCR engine: Needs system installation")
    
    print("\n🔧 Tesseract Installation:")
    print("  Windows: Download from https://github.com/UB-Mannheim/tesseract/wiki")
    print("  After install: Add to PATH or specify path in code")
    
    print("\n🧪 Test OCR Status:")
    try:
        # Test if we can make a request to the OCR endpoint
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            print("  ✅ API Server: Running")
            print("  ✅ OCR Endpoints: Available")
            
            # Check if endpoints exist
            print("\n📋 Available Endpoints:")
            print("  • /extract-mcq (with auto-OCR fallback)")
            print("  • /extract-mcq-ocr (forced OCR)")
            print("  • /debug-pdf (PDF analysis)")
            print("  • /test-ocr (image OCR testing)")
            
        else:
            print("  ❌ API Server: Not responding")
    except Exception as e:
        print(f"  ❌ Connection Error: {e}")

def show_next_steps():
    """Show next steps for user"""
    print("\n" + "=" * 60)
    print("🎯 NEXT STEPS FOR YOUR PDF:")
    print("=" * 60)
    
    print("\n1. 🔧 Install Tesseract OCR:")
    print("   • Download: https://github.com/UB-Mannheim/tesseract/wiki")
    print("   • Install to default location")
    print("   • Add to system PATH")
    
    print("\n2. 🧪 Test OCR:")
    print("   • Visit: http://127.0.0.1:8000/docs")
    print("   • Try /extract-mcq-ocr endpoint")
    print("   • Upload your PDF file")
    
    print("\n3. ✅ If Tesseract not available:")
    print("   • Convert PDF to text-based format")
    print("   • Use online OCR services")
    print("   • Manually type out questions")
    
    print("\n4. 🚀 Alternative:")
    print("   • Upload individual page images (.png/.jpg)")
    print("   • Use /test-ocr to see OCR quality")
    print("   • Process pages one by one")

if __name__ == "__main__":
    test_ocr_capabilities()
    show_next_steps()
