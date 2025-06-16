#!/usr/bin/env python3
"""
Test Tesseract OCR installation
"""

import subprocess
import requests

BASE_URL = "http://127.0.0.1:8000"

def test_tesseract_installation():
    """Test if Tesseract is properly installed"""
    print("🔍 Testing Tesseract OCR Installation")
    print("=" * 50)
    
    # Test 1: Check if tesseract command is available
    print("\n1. 🧪 Testing Tesseract Command...")
    try:
        result = subprocess.run(['tesseract', '--version'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            version_info = result.stdout.split('\n')[0]
            print(f"   ✅ Tesseract found: {version_info}")
        else:
            print(f"   ❌ Tesseract command failed: {result.stderr}")
    except FileNotFoundError:
        print("   ❌ Tesseract command not found in PATH")
    except Exception as e:
        print(f"   ❌ Error testing Tesseract: {e}")
    
    # Test 2: Check pytesseract import
    print("\n2. 🐍 Testing pytesseract Python library...")
    try:
        import pytesseract
        print("   ✅ pytesseract library imported successfully")
        
        # Try to get tesseract version through pytesseract
        try:
            version = pytesseract.get_tesseract_version()
            print(f"   ✅ Tesseract version via pytesseract: {version}")
        except Exception as e:
            print(f"   ⚠️  pytesseract can't access Tesseract: {e}")
    except ImportError:
        print("   ❌ pytesseract library not found")
    
    # Test 3: Test API endpoints
    print("\n3. 🌐 Testing API OCR endpoints...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            print("   ✅ API server is running")
        else:
            print("   ❌ API server not responding")
    except Exception as e:
        print(f"   ❌ API connection error: {e}")

def test_simple_ocr():
    """Test OCR with the API using a simple test"""
    print("\n4. 🖼️ Testing OCR functionality...")
    
    # Check if there are any sample images to test with
    import os
    sample_files = [f for f in os.listdir('.') if f.endswith(('.png', '.jpg', '.jpeg'))]
    
    if sample_files:
        print(f"   📄 Found sample images: {sample_files[:3]}")
        print("   💡 You can test OCR by uploading these to /test-ocr")
    else:
        print("   📄 No sample images found in current directory")
        print("   💡 Create a simple text image to test OCR functionality")

if __name__ == "__main__":
    test_tesseract_installation()
    test_simple_ocr()
    
    print("\n" + "=" * 60)
    print("🎯 NEXT STEPS:")
    print("=" * 60)
    
    print("\n✅ If Tesseract is working:")
    print("  1. Upload your PDF to http://127.0.0.1:8000/docs")
    print("  2. Try /extract-mcq endpoint (auto-detects OCR need)")
    print("  3. Or use /extract-mcq-ocr for forced OCR")
    
    print("\n⚠️ If Tesseract failed:")
    print("  1. Restart your terminal/command prompt")
    print("  2. Check if Tesseract is in your PATH")
    print("  3. Try running 'tesseract --version' manually")
    print("  4. Reinstall Tesseract if needed")
    
    print("\n🚀 Ready to test your PDF:")
    print("  • File: Apex Civil engineer objective 2080-04-06.pdf")
    print("  • Expected: MCQ questions extracted via OCR")
    print("  • Endpoint: /extract-mcq or /extract-mcq-ocr")
    
    print("=" * 60)
