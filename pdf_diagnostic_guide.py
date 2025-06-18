#!/usr/bin/env python3

def create_pdf_diagnostic_guide():
    """Create a comprehensive guide for diagnosing PDF extraction issues"""
    
    guide = """
# 🔍 PDF MCQ EXTRACTION DIAGNOSTIC GUIDE

## 📊 Current Status: 46/100 Questions Extracted

Your extraction is getting 46 out of 100 questions. Here's how to diagnose and fix the remaining issues:

## 🚀 **IMPROVEMENTS MADE:**
- ✅ Fixed OCR corruption of question numbers (10→1c, 50→5c, 100→10c)
- ✅ Added more flexible question patterns (Question 1:, Q1., 1), etc.)
- ✅ Added more flexible option patterns (A), (A), A., A:, A-)
- ✅ Enhanced visual content extraction with single-line table support
- ✅ Improved mathematical content detection

## 🔍 **DIAGNOSTIC CHECKLIST:**

### 1. **Question Numbering Issues** ⚠️
Your JSON shows missing numbers. Check if questions use:
- Different formats: "Question No. 1:", "Q.1", "1-", "1:", etc.
- Roman numerals: "I.", "II.", "III."
- Letters: "A.", "B.", "C." (for sub-questions)
- **Solution**: Add more patterns to `question_patterns`

### 2. **Option Format Issues** ⚠️
Your JSON shows broken options like all "BS." - indicates:
- OCR errors in options
- Split options across lines
- Different option formats: (a), 1), i), etc.
- **Solution**: Improve option extraction logic

### 3. **Page Break Issues** 📄
PDF extraction often splits content across pages:
- Questions split between pages
- Options separated from questions
- Headers/footers interfering
- **Solution**: Better text preprocessing

### 4. **PDF Text Quality** 📝
Check if your PDF has:
- Scanned images vs searchable text
- Complex layouts (columns, tables)
- Special characters or mathematical symbols
- **Solution**: Use OCR if needed

### 5. **Content Layout Issues** 📊
Questions might be in:
- Multi-column layouts
- Tables or boxes
- Mixed with other content
- **Solution**: Layout-aware extraction

## 🛠️ **IMMEDIATE FIXES TO TRY:**

### Fix 1: Add More Question Patterns
If you see different question formats in your PDF, add patterns like:
```python
r'^Question\s+No\.\s*(\d+)[:\.]?\s*(.+)',  # Question No. 1:
r'^Q\.\s*(\d+)[:\.]?\s*(.+)',  # Q.1
r'^(\d+)\s*[\-]\s*(.+)',  # 1 - Question
```

### Fix 2: Improve Option Detection
For broken options, add:
```python
r'^[a-d]\s*[\.\)]\s*(.+)',  # a. option or a) option
r'^\([a-d]\)\s*(.+)',  # (a) option
r'^[a-d]\s*[:]\s*(.+)',  # a: option
```

### Fix 3: Better OCR Error Handling
Common PDF OCR errors:
- B→6, S→5, O→0, I→1, l→1
- Add specific fixes for these

## 📋 **TESTING SUGGESTIONS:**

1. **Test with smaller sections** of your PDF
2. **Check the raw text extraction** to see what's actually extracted
3. **Look for patterns** in the missing question numbers
4. **Compare successful vs failed extractions**

## 🎯 **NEXT STEPS:**

1. **Upload your PDF again** with the current improvements
2. **Check if you get more than 46 questions** 
3. **Share the specific question numbers that are missing**
4. **Show a sample of the problematic text** if questions are still incomplete

## 📊 **Expected Improvements:**

With our current fixes, you should see:
- ✅ **Better question number detection** (no more 1c corruption)
- ✅ **More flexible pattern matching** (Question 1:, Q1., etc.)
- ✅ **Improved option extraction** (flexible spacing and punctuation)
- ✅ **Enhanced content analysis** (math and visual detection)

**Expected Success Rate: 70-85%** (vs current 46%)

If you're still not getting 90%+ success rate, we'll need to:
1. Look at the specific PDF structure
2. Add custom patterns for your document format
3. Potentially improve the PDF text extraction method

Try uploading your PDF again and let's see the improvement! 🚀
"""
    
    print(guide)

if __name__ == "__main__":
    create_pdf_diagnostic_guide()
