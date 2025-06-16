# MCQ Extractor API

This is a FastAPI application that extracts Multiple Choice Questions (MCQ) from uploaded files.

## Features

- Extract MCQ questions from various file formats (PDF, DOCX, XLSX, TXT, Images)
- OCR support for image files (JPG, PNG, BMP, TIFF)
- Image preprocessing for improved OCR accuracy
- Automatic detection of question patterns
- Support for different option formats (A), (A), A.
- Extraction of correct answers when available
- RESTful API with interactive documentation

## Supported File Formats

- **PDF** (.pdf) - Portable Document Format
- **Word Document** (.docx) - Microsoft Word Document
- **Excel Spreadsheet** (.xlsx) - Microsoft Excel Spreadsheet
- **Text File** (.txt) - Plain Text File
- **JPEG Image** (.jpg, .jpeg) - JPEG images with OCR text extraction
- **PNG Image** (.png) - PNG images with OCR text extraction
- **BMP Image** (.bmp) - BMP images with OCR text extraction
- **TIFF Image** (.tiff) - TIFF images with OCR text extraction

## Running the application

To run the application, use the following command:

```bash
uv run uvicorn main:app --reload
```

The API will be available at:

- Main application: `http://127.0.0.1:8000`
- Interactive API docs: `http://127.0.0.1:8000/docs`
- Alternative API docs: `http://127.0.0.1:8000/redoc`

## API Endpoints

### POST /extract-mcq

Upload a file to extract MCQ questions.

**Request**: Multipart form with file upload
**Response**: JSON containing extracted MCQ questions

### GET /supported-formats

Get list of supported file formats.

### GET /health

Health check endpoint.

## Important Note for Image Processing

**Tesseract OCR Engine Required**: For image processing functionality to work, you need to install Tesseract OCR on your system:

### Windows:

1. Download Tesseract from: https://github.com/UB-Mannheim/tesseract/wiki
2. Install it (usually to `C:\Program Files\Tesseract-OCR\`)
3. Add the installation path to your system PATH environment variable

### Alternative (if Tesseract is not in PATH):

You may need to specify the Tesseract path in your code:

```python
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

## Example MCQ Format

The API can detect MCQ questions in various formats:

```
1. What is the capital of France?
A) London
B) Berlin
C) Paris
D) Madrid
Answer: C

Q2: Which planet is closest to the Sun?
(A) Venus
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
   ```

2. **🧪 Test All Features:**

   ```bash
   python final_test.py
   ```

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
