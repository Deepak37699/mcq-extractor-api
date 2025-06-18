#!/usr/bin/env python3
"""
Debug the enhanced endpoint specifically
"""

import requests
import json
import os

API_URL = "http://localhost:8000"

def debug_enhanced_endpoint():
    """Debug the enhanced endpoint issue"""
    print("Debugging enhanced endpoint...")
    
    if os.path.exists("sample_test.txt"):
        with open("sample_test.txt", 'rb') as f:
            files = {'file': ('sample_test.txt', f, 'text/plain')}
            response = requests.post(f"{API_URL}/extract-mcq-enhanced", files=files, timeout=30)
            
            print(f"Status: {response.status_code}")
            print(f"Response: {response.json()}")
            
            # Check the raw response to see if there are any clues
            print(f"Headers: {response.headers}")

if __name__ == "__main__":
    debug_enhanced_endpoint()
