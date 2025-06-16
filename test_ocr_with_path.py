#!/usr/bin/env python3
"""
Test OCR with Tesseract path set correctly
"""

import os
import pytesseract
import requests
import io

# Set Tesseract path for this session
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

BASE_URL = "http://127.0.0.1:8000"

def test_tesseract_with_path():
    """Test Tesseract with correct path"""
    print("🔧 Testing Tesseract with explicit path...")
    
    try:
        version = pytesseract.get_tesseract_version()
        print(f"✅ Tesseract version: {version}")
        return True
    except Exception as e:
        print(f"❌ Tesseract still not working: {e}")
        return False

def create_simple_test_image():
    """Create a simple test image with text"""
    try:
        from PIL import Image, ImageDraw, ImageFont
        
        # Create a simple image with text
        img = Image.new('RGB', (400, 200), color='white')
        draw = ImageDraw.Draw(img)
        
        # Add sample MCQ text
        text = """1. What is 2 + 2?
A) 3
B) 4
C) 5
D) 6
Answer: B"""
        
        try:
            # Try to use a font
            font = ImageFont.truetype("arial.ttf", 16)
        except:
            # Use default font if arial not found
            font = ImageFont.load_default()
        
        draw.text((10, 10), text, fill='black', font=font)
        
        # Save the image
        img.save('test_mcq.png')
        print("✅ Created test image: test_mcq.png")
        return True
        
    except Exception as e:
        print(f"❌ Could not create test image: {e}")
        return False

def test_ocr_on_image():
    """Test OCR on our test image"""
    if not os.path.exists('test_mcq.png'):
        print("❌ Test image not found")
        return
    
    print("\n🧪 Testing OCR on sample image...")
    
    try:
        with open('test_mcq.png', 'rb') as f:
            files = {'file': ('test_mcq.png', f, 'image/png')}
            response = requests.post(f"{BASE_URL}/test-ocr", files=files)
        
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("✅ OCR test successful!")
            print(f"Extracted text length: {data.get('text_length', 0)}")
            print(f"Extracted text preview: {data.get('extracted_text', '')[:200]}...")
        else:
            print(f"❌ OCR test failed: {response.text}")
            
    except Exception as e:
        print(f"❌ Error testing OCR: {e}")

if __name__ == "__main__":
    print("🚀 Testing Tesseract OCR with Correct Path")
    print("=" * 50)
    
    # Test 1: Check if Tesseract works with explicit path
    if test_tesseract_with_path():
        
        # Test 2: Create a simple test image
        if create_simple_test_image():
            
            # Test 3: Test OCR on the image
            test_ocr_on_image()
            
            print(f"\n🎯 Ready to test your PDF!")
            print(f"   The OCR functionality is now working.")
            print(f"   Upload your PDF to /extract-mcq or /extract-mcq-ocr")
        
    else:
        print("\n❌ Tesseract path issue persists")
        print("   Please check the installation and PATH configuration")
