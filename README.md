# MCQ Extractor API

A robust FastAPI application that extracts Multiple Choice Questions (MCQ) from uploaded files with advanced features including mathematical content detection, visual content analysis, and enhanced OCR processing.

## 🚀 Current Status: v1.0.0 (Fully Operational)

✅ **All Core Features Working**  
✅ **Enhanced Mathematical & Visual Content Detection**  
✅ **Improved Error Handling & PDF Processing**  
✅ **Advanced OCR with Image Preprocessing**  
✅ **PyMuPDF API Fixed & Optimized**

## 🌟 Key Features

### Core Extraction Capabilities

- **Multi-format Support**: PDF, DOCX, XLSX, TXT, Images (JPG/PNG/BMP/TIFF)
- **Advanced OCR**: Improved image preprocessing for better text extraction
- **Robust PDF Processing**: Multi-method extraction with PyMuPDF and PyPDF2 fallbacks
- **Flexible Question Patterns**: Supports various numbering formats (1., Q1:, 1), etc.)
- **Enhanced Answer Detection**: Recognizes "Answer: A", "Ans. B", standalone letters

### Advanced Content Analysis

- **Mathematical Content Detection**: Symbols (∫, ∑, √, π), equations, formulas
- **Visual Content Analysis**: Tables, charts, diagrams, images
- **Content Classification**: mathematical, visual_content, mathematical_with_visual, standard
- **Table Extraction**: Automatic detection and formatting of tabular data

### Technical Improvements

- **Clean Error Messages**: No more nested error responses
- **Fixed PyMuPDF API**: Proper use of `load_page()` method
- **Improved OCR**: OTSU thresholding for better image text extraction
- **Enhanced Answer Patterns**: Support for period-separated answers ("Answer. B")

## 📊 Supported File Formats

| Format | Extension                                | Processing Method               | Status              |
| ------ | ---------------------------------------- | ------------------------------- | ------------------- |
| PDF    | `.pdf`                                   | PyMuPDF + PyPDF2 + OCR fallback | ✅ Fixed & Enhanced |
| Word   | `.docx`                                  | python-docx                     | ✅ Working          |
| Excel  | `.xlsx`, `.xls`                          | openpyxl                        | ✅ Working          |
| Text   | `.txt`                                   | Direct text processing          | ✅ Working          |
| Images | `.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff` | OCR with preprocessing          | ✅ Enhanced         |

## 🛠 Installation & Setup

### Prerequisites

- Python 3.8+
- Tesseract OCR (for image processing)

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Tesseract Setup (Windows)

```bash
# Download and install from: https://github.com/UB-Mannheim/tesseract/wiki
# Default path: C:\Program Files\Tesseract-OCR\tesseract.exe
```

## 🚀 Running the Application

### Start the Server

```bash
uvicorn main:app --reload
```

### Access Points

- **Main API**: `http://localhost:8000`
- **Interactive Docs**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 📡 API Endpoints

### Core Endpoints

#### `GET /`

Welcome message and API status

#### `GET /health`

Health check endpoint

#### `POST /extract-mcq`

Basic MCQ extraction with standard processing

**Request**: Multipart form with file upload  
**Response**: JSON with extracted MCQs and basic statistics

#### `POST /extract-mcq-enhanced`

Advanced MCQ extraction with mathematical and visual content analysis

**Request**: Multipart form with file upload  
**Response**: Enhanced JSON with detailed content analysis

## 📋 Response Format

### Basic Response (`/extract-mcq`)

```json
{
  "success": true,
  "file_info": {
    "filename": "test.txt",
    "file_type": "TXT",
    "file_size_mb": 0.01
  },
  "extraction_summary": {
    "total_questions": 2,
    "complete_questions": 2,
    "questions_with_answers": 2
  },
  "mcqs": [
    {
      "question_number": 1,
      "question": "What is the capital of France?",
      "options": {
        "A": "London",
        "B": "Berlin",
        "C": "Paris",
        "D": "Madrid"
      },
      "correct_answer": "C"
    }
  ]
}
```

### Enhanced Response (`/extract-mcq-enhanced`)

```json
{
  "success": true,
  "file_info": {...},
  "extraction_summary": {
    "total_questions": 2,
    "mathematical_questions": 0,
    "visual_content_questions": 0,
    "complete_questions": 2,
    "questions_with_answers": 2,
    "question_type_distribution": {"standard": 2}
  },
  "document_analysis": {
    "has_mathematical_content": false,
    "has_visual_content": false,
    "mathematical_elements": {...},
    "visual_elements": {...}
  },
  "mcqs": [
    {
      "question_number": 1,
      "question": "What is the capital of France?",
      "options": {...},
      "correct_answer": "C",
      "question_type": "standard",
      "has_math_content": false,
      "has_visual_content": false,
      "content_analysis": {
        "mathematics": {...},
        "visual_elements": {...}
      }
    }
  ],
  "enhanced_features": {
    "mathematical_notation_support": true,
    "visual_content_detection": true,
    "table_extraction": true,
    "equation_parsing": true,
    "content_type_classification": true
  }
}
```

## 🔧 Supported Question & Answer Formats

### Question Patterns

- `1. Question text`
- `Q1: Question text`
- `1) Question text`
- `Question: 1 Question text`

### Option Patterns

- `A) Option text`
- `(A) Option text`
- `A. Option text`
- `A Option text`

### Answer Patterns

- `Answer: A`
- `Ans: B`
- `Answer. C` (period supported)
- `Correct: D`
- Standalone letters

## 🚨 Error Handling

The API provides clean, informative error messages:

- **Invalid PDF**: "Could not extract text from PDF using any method..."
- **Unsupported Format**: "Unsupported file type: xyz"
- **No Content**: "No text could be extracted from the file"
- **No MCQs**: "No MCQs found in the text"

## 🧪 Testing

Run comprehensive tests:

```bash
python test_comprehensive.py
```

## 📈 Recent Improvements

### v1.0.0 (Current)

- ✅ Fixed PyMuPDF API error ("Document object has no attribute 'page'")
- ✅ Enhanced image OCR with improved preprocessing
- ✅ Clean error messages (no more nested errors)
- ✅ Enhanced answer detection patterns
- ✅ Mathematical and visual content analysis
- ✅ Robust multi-method PDF extraction

## 🔗 Dependencies

See `requirements.txt` for full list. Key dependencies:

- FastAPI & Uvicorn
- PyMuPDF & PyPDF2 (PDF processing)
- Pytesseract & OpenCV (OCR & image processing)
- SymPy & Matplotlib (mathematical analysis)
- python-docx & openpyxl (Office documents)
  (B) Mercury
  (C) Earth
  (D) Mars
  Ans: B

```

## 🎉 Your API is Ready!

✅ **STATUS: FULLY FUNCTIONAL** - All tests passed!

### 🚀 **Quick Start:**

1. **📤 Upload Your PDF:**

```

Open: http://127.0.0.1:8000/docs
Try: /extract-mcq endpoint
Upload: "Apex Civil engineer objective 2080-04-06.pdf"

````

2. **🧪 Test All Features:**

```bash
python final_test.py
````

3. **🔍 Debug PDFs (if needed):**
   ```
   Use: /debug-pdf endpoint
   Analyzes: PDF extraction capabilities
   Recommends: Best extraction method
   ```

### 🎯 **For Your Scanned PDF:**

- **File:** `Apex Civil engineer objective 2080-04-06.pdf`
- **Method:** OCR extraction (Tesseract installed ✅)
- **Endpoint:** `/extract-mcq` or `/extract-mcq-ocr`
- **Expected:** MCQ questions extracted and parsed automatically

---

**🚀 Your MCQ Extractor API is production-ready!**
