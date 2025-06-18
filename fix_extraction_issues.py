#!/usr/bin/env python3
"""
Comprehensive diagnostic and fix script for MCQ extraction issues
"""

import json
import re
from typing import Dict, List, Tuple, Any

class ExtractionFixer:
    def __init__(self):
        self.issue_patterns = {
            'garbled_text': [
                r'[|}{]+',  # Multiple special characters
                r'[a-z]\s*[|]\s*[a-z]',  # Letters separated by pipes
                r'je\).*lelele',  # Specific garbled pattern found
                r'^[^A-Z0-9]*[a-z]{1,2}\s*[|]',  # Starting with lowercase and pipes
            ],
            'incomplete_options': [
                r'^(BS\.|Rs\.)$',  # Just BS. or Rs.
                r'^(A|B|C|D):\s*(BS\.|Rs\.)$',  # Option with just BS. or Rs.
                r'^[A-D]:\s*$',  # Empty option values
            ],
            'answer_patterns': [
                r'Answer[:\s]*([A-D])',
                r'Correct[:\s]*([A-D])',
                r'\b([A-D])\s*\)',
                r'^\s*([A-D])\s*$',
            ]
        }
    
    def analyze_extraction_issues(self, mcqs: List[Dict]) -> Dict[str, Any]:
        """Analyze all extraction issues in the MCQ data"""
        issues = {
            'garbled_questions': [],
            'incomplete_options': [],
            'missing_options': [],
            'duplicate_numbers': [],
            'missing_answers': 0,
            'corrupted_text_patterns': [],
            'option_analysis': {}
        }
        
        question_numbers = {}
        
        for i, mcq in enumerate(mcqs):
            q_num = mcq.get('question_number')
            question = mcq.get('question', '')
            options = mcq.get('options', {})
            
            # Check for duplicate question numbers
            if q_num in question_numbers:
                issues['duplicate_numbers'].append({
                    'number': q_num,
                    'indices': [question_numbers[q_num], i]
                })
            else:
                question_numbers[q_num] = i
            
            # Check for garbled text
            for pattern in self.issue_patterns['garbled_text']:
                if re.search(pattern, question):
                    issues['garbled_questions'].append({
                        'index': i,
                        'question_number': q_num,
                        'question': question,
                        'pattern': pattern
                    })
                    break
            
            # Check for incomplete options
            incomplete_opts = []
            for opt_key, opt_value in options.items():
                for pattern in self.issue_patterns['incomplete_options']:
                    if re.search(pattern, str(opt_value)):
                        incomplete_opts.append({
                            'option': opt_key,
                            'value': opt_value,
                            'pattern': pattern
                        })
            
            if incomplete_opts:
                issues['incomplete_options'].append({
                    'index': i,
                    'question_number': q_num,
                    'incomplete_options': incomplete_opts
                })
            
            # Check for missing options (A, B, C, D)
            expected_options = {'A', 'B', 'C', 'D'}
            actual_options = set(options.keys())
            missing = expected_options - actual_options
            
            if missing:
                issues['missing_options'].append({
                    'index': i,
                    'question_number': q_num,
                    'missing': list(missing)
                })
            
            # Count missing answers
            if not mcq.get('correct_answer'):
                issues['missing_answers'] += 1
        
        return issues
    
    def suggest_fixes(self, issues: Dict[str, Any]) -> Dict[str, List[str]]:
        """Suggest fixes for identified issues"""
        suggestions = {
            'immediate_fixes': [],
            'pattern_improvements': [],
            'answer_extraction_fixes': [],
            'ocr_improvements': []
        }
        
        if issues['garbled_questions']:
            suggestions['immediate_fixes'].extend([
                "Fix OCR cleaning logic to prevent text corruption",
                "Add better regex patterns for question identification",
                "Implement text validation before processing"
            ])
            suggestions['ocr_improvements'].extend([
                "Improve OCR post-processing for special characters",
                "Add text confidence scoring",
                "Implement multiple OCR engine fallback"
            ])
        
        if issues['incomplete_options']:
            suggestions['pattern_improvements'].extend([
                "Enhance option extraction patterns",
                "Add context-aware option parsing",
                "Implement option completion from surrounding text"
            ])
        
        if issues['missing_answers'] > 0:
            suggestions['answer_extraction_fixes'].extend([
                "Add answer key detection patterns",
                "Look for answer patterns at end of document",
                "Implement answer extraction from separate sections"
            ])
        
        if issues['duplicate_numbers']:
            suggestions['immediate_fixes'].extend([
                "Fix question numbering detection",
                "Add sequential validation",
                "Implement duplicate detection and correction"
            ])
        
        return suggestions
    
    def generate_improved_patterns(self) -> Dict[str, List[str]]:
        """Generate improved regex patterns for extraction"""
        return {
            'question_patterns': [
                r'^\s*(\d+)\.\s*(.+?)(?=\n\s*[A-D][\.\)]|$)',
                r'^\s*Q[\.\s]*(\d+)[\.\s]*(.+?)(?=\n\s*[A-D][\.\)]|$)',
                r'^\s*(\d+)\)\s*(.+?)(?=\n\s*[A-D][\.\)]|$)',
                r'^\s*(\d+)[\.\s]+([^A-D\n].+?)(?=\n\s*A[\.\)]|$)',
            ],
            'option_patterns': [
                r'^([A-D])[\.\)]\s*(.+?)(?=\n[A-D][\.\)]|\n\d+\.|\n\n|$)',
                r'^([A-D])[\.\)]\s+(.+?)(?=\s*[A-D][\.\)]|\n\d+\.|\n\n|$)',
                r'([A-D])[\.\)]\s*([^A-D\n].+?)(?=\s+[A-D][\.\)]|\n|$)',
            ],
            'answer_patterns': [
                r'Answer\s*[:\-]?\s*([A-D])',
                r'Correct\s*Answer\s*[:\-]?\s*([A-D])',
                r'Ans\s*[:\-]?\s*([A-D])',
                r'\b([A-D])\s*\)\s*$',
                r'^\s*([A-D])\s*$',
            ]
        }

def main():
    # Sample MCQ data from the extraction result
    sample_mcqs = [
        {
            "question_number": 3,
            "question": "s 1 je) a|e]?| jelelelele,",
            "options": {"A": "3", "B": "4", "C": ", -2", "D": "1"},
            "correct_answer": None
        },
        {
            "question_number": 6,
            "question": "When was Sati Practice eliminated from Nepal?",
            "options": {"A": "BS.", "B": "BS.", "C": "BS.", "D": "BS."},
            "correct_answer": None
        },
        {
            "question_number": 40,
            "question": "Aperson incurs a loss of 5% by selling a watch for Rs. 1140. At what price should the watch be sold to earn 5% profit?",
            "options": {"A": "Rs.", "B": "Rs.", "C": "Rs.", "D": "Rs."},
            "correct_answer": None
        }
    ]
    
    fixer = ExtractionFixer()
    
    print("=== MCQ EXTRACTION ISSUES ANALYSIS ===\n")
    
    issues = fixer.analyze_extraction_issues(sample_mcqs)
    
    print("🔍 IDENTIFIED ISSUES:")
    print(f"• Garbled questions: {len(issues['garbled_questions'])}")
    print(f"• Incomplete options: {len(issues['incomplete_options'])}")
    print(f"• Missing options: {len(issues['missing_options'])}")
    print(f"• Duplicate numbers: {len(issues['duplicate_numbers'])}")
    print(f"• Missing answers: {issues['missing_answers']}")
    
    print("\n📋 DETAILED ANALYSIS:")
    
    if issues['garbled_questions']:
        print("\n🔧 GARBLED QUESTIONS:")
        for item in issues['garbled_questions']:
            print(f"  Question {item['question_number']}: '{item['question'][:50]}...'")
            print(f"    Pattern matched: {item['pattern']}")
    
    if issues['incomplete_options']:
        print("\n🔧 INCOMPLETE OPTIONS:")
        for item in issues['incomplete_options']:
            print(f"  Question {item['question_number']}:")
            for opt in item['incomplete_options']:
                print(f"    {opt['option']}: '{opt['value']}'")
    
    print("\n💡 SUGGESTED FIXES:")
    suggestions = fixer.suggest_fixes(issues)
    
    for category, fixes in suggestions.items():
        if fixes:
            print(f"\n{category.upper().replace('_', ' ')}:")
            for fix in fixes:
                print(f"  • {fix}")
    
    print("\n🎯 IMPROVED PATTERNS:")
    patterns = fixer.generate_improved_patterns()
    
    for category, pattern_list in patterns.items():
        print(f"\n{category.upper().replace('_', ' ')}:")
        for i, pattern in enumerate(pattern_list, 1):
            print(f"  {i}. {pattern}")
    
    print("\n✅ NEXT STEPS:")
    print("1. Implement improved OCR cleaning logic")
    print("2. Add enhanced regex patterns for extraction")
    print("3. Implement answer key detection")
    print("4. Add text validation and corruption detection")
    print("5. Test with the actual PDF to verify improvements")

if __name__ == "__main__":
    main()
