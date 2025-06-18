#!/usr/bin/env python3
"""
Quick test to get current app status and features
"""
import requests
import json
import os

def get_current_app_status():
    """Get comprehensive app status"""
    print("🔍 CURRENT MCQ EXTRACTOR API STATUS")
    print("="*50)
    
    # Test basic endpoint
    if os.path.exists("sample_test.txt"):
        with open("sample_test.txt", 'rb') as f:
            files = {'file': ('sample_test.txt', f, 'text/plain')}
            response = requests.post("http://localhost:8000/extract-mcq-enhanced", files=files, timeout=30)
            
        if response.status_code == 200:
            result = response.json()
            
            print("📊 CURRENT FEATURES:")
            print(f"✅ Basic Extraction: Working")
            print(f"✅ Enhanced Extraction: Working")
            print(f"✅ Mathematical Detection: {result.get('document_analysis', {}).get('has_mathematical_content', 'Unknown')}")
            print(f"✅ Visual Content Detection: {result.get('document_analysis', {}).get('has_visual_content', 'Unknown')}")
            
            print(f"\n📈 EXTRACTION SUMMARY:")
            summary = result.get('extraction_summary', {})
            for key, value in summary.items():
                print(f"   {key}: {value}")
            
            print(f"\n🔧 ENHANCED FEATURES:")
            enhanced = result.get('enhanced_features', {})
            for key, value in enhanced.items():
                status = "✅" if value else "❌"
                print(f"   {status} {key}: {value}")
            
            # Check response structure
            print(f"\n📋 RESPONSE STRUCTURE:")
            print(f"   Keys: {list(result.keys())}")
            
            if 'mcqs' in result and result['mcqs']:
                mcq_sample = result['mcqs'][0]
                print(f"   MCQ Keys: {list(mcq_sample.keys())}")
                
    print("\n" + "="*50)

if __name__ == "__main__":
    get_current_app_status()
