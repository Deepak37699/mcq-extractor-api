#!/usr/bin/env python3
"""
Complete solution for Tesseract OCR installation and testing
"""

import requests

BASE_URL = "http://127.0.0.1:8000"

def check_system_status():
    """Check the current status of the MCQ extraction system"""
    print("🔍 MCQ Extractor System Status")
    print("=" * 50)
    
    # Check API status
    try:
        response = requests.get(f"{BASE_URL}/health")
        api_status = "✅ Running" if response.status_code == 200 else "❌ Error"
    except:
        api_status = "❌ Not responding"
    
    print(f"API Server: {api_status}")
    
    # Check Tesseract status
    try:
        response = requests.get(f"{BASE_URL}/tesseract-status")
        if response.status_code == 200:
            data = response.json()
            tesseract_status = data.get('status', 'Unknown')
            ocr_ready = data.get('ocr_endpoints_ready', False)
            print(f"Tesseract OCR: {tesseract_status}")
            print(f"OCR Ready: {'✅ Yes' if ocr_ready else '❌ No'}")
            
            if not ocr_ready:
                print(f"\n📥 Download: {data.get('download_url', 'N/A')}")
        else:
            print("Tesseract OCR: ❌ Status check failed")
    except:
        print("Tesseract OCR: ❌ Cannot check status")

def show_installation_steps():
    """Show step-by-step installation guide"""
    print("\n🚀 TESSERACT INSTALLATION STEPS:")
    print("=" * 50)
    
    print("\n1. 📥 Download Tesseract:")
    print("   • Go to: https://github.com/UB-Mannheim/tesseract/wiki")
    print("   • Download latest Windows installer")
    print("   • File name like: tesseract-ocr-w64-setup-x.x.x.exe")
    
    print("\n2. 🔧 Install Tesseract:")
    print("   • Run installer as Administrator")
    print("   • Install to: C:\\Program Files\\Tesseract-OCR\\")
    print("   • ✅ CHECK: 'Add to PATH' option during install")
    
    print("\n3. ✅ Verify Installation:")
    print("   • Open new Command Prompt")
    print("   • Run: tesseract --version")
    print("   • Should show version info")
    
    print("\n4. 🧪 Test with API:")
    print("   • Restart VS Code/Terminal")
    print("   • Visit: http://127.0.0.1:8000/tesseract-status")
    print("   • Should show: ✅ Tesseract is working correctly")

def show_pdf_solution():
    """Show solution for the specific PDF"""
    print("\n📄 YOUR PDF SOLUTION:")
    print("=" * 50)
    
    print("\n🎯 Current Situation:")
    print("   • PDF: Apex Civil engineer objective 2080-04-06.pdf")
    print("   • Type: Scanned/Image-based (11 pages)")
    print("   • Status: OCR required for text extraction")
    print("   • API: Ready and waiting for Tesseract")
    
    print("\n🔄 After Installing Tesseract:")
    print("   1. Visit: http://127.0.0.1:8000/docs")
    print("   2. Use: /extract-mcq-ocr endpoint")
    print("   3. Upload: Your PDF file")
    print("   4. Get: Structured MCQ data extracted from all pages")
    
    print("\n⚡ Quick Alternative (No Installation):")
    print("   • Use online OCR: smallpdf.com, ilovepdf.com")
    print("   • Convert PDF to text")
    print("   • Save as .txt file")
    print("   • Upload to: /extract-mcq")

def show_testing_plan():
    """Show how to test after installation"""
    print("\n🧪 TESTING PLAN AFTER INSTALLATION:")
    print("=" * 50)
    
    print("\n1. ✅ Verify Tesseract:")
    print("   GET http://127.0.0.1:8000/tesseract-status")
    print("   Expected: tesseract_installed: true")
    
    print("\n2. 🧪 Test OCR Endpoint:")
    print("   POST http://127.0.0.1:8000/extract-mcq-ocr")
    print("   Upload: Apex Civil engineer objective 2080-04-06.pdf")
    print("   Expected: Extracted text and MCQ questions")
    
    print("\n3. 📊 Check Results:")
    print("   • total_questions > 0")
    print("   • extracted_text_preview shows actual text")
    print("   • mcqs array contains structured questions")

if __name__ == "__main__":
    check_system_status()
    show_installation_steps() 
    show_pdf_solution()
    show_testing_plan()
    
    print("\n" + "=" * 60)
    print("📋 SUMMARY: Install Tesseract → Test → Extract MCQs")
    print("🌐 Live API: http://127.0.0.1:8000/docs")
    print("=" * 60)
