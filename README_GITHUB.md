# 🚀 MCQ Extractor API

A powerful FastAPI-based application for extracting Multiple Choice Questions (MCQs) from various file formats including PDFs, Word documents, Excel files, text files, and images. Features advanced OCR support for scanned documents and intelligent parsing for different MCQ formats.

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com)
[![OCR](https://img.shields.io/badge/OCR-Tesseract-orange.svg)](https://github.com/tesseract-ocr/tesseract)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## ✨ Features

### 📄 **Multi-Format Support**
- **PDF**: Text-based and scanned documents (with OCR)
- **Word Documents**: `.docx` files
- **Excel Spreadsheets**: `.xlsx` files  
- **Text Files**: `.txt` files
- **Images**: `.jpg`, `.png`, `.bmp`, `.tiff` with OCR

### 🧠 **Intelligent MCQ Parsing**
- Multiple question formats: `1.`, `1)`, `Q1:`, `Question: 1`
- Various option styles: `a.`, `(a)`, `A)`, `A.`
- Different answer patterns: `Answer: A`, `Ans: A`, `Correct: A`
- Handles split options and multi-line questions
- Support for high question counts (100+ questions)

### 👁️ **Advanced OCR Integration**
- Tesseract OCR for scanned documents
- Automatic fallback to OCR for image-based PDFs
- OCR error correction and text cleaning
- Handles common scanning artifacts

### 🛡️ **Robust Error Handling**
- Comprehensive file validation
- Detailed error messages and recommendations
- Debug endpoints for troubleshooting
- Graceful degradation for unsupported content

### 📋 **Rich API Documentation**
- Interactive OpenAPI documentation
- Multiple endpoints for different use cases
- Detailed response schemas
- Built-in testing interface

## 🚀 Quick Start

### Prerequisites

- **Python 3.11+**
- **UV Package Manager** (recommended) or pip
- **Tesseract OCR** (for scanned document support)

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/mcq-extractor-api.git
cd mcq-extractor-api
```

### 2. Install Dependencies

**Using UV (Recommended):**
```bash
uv sync
```

**Using pip:**
```bash
pip install -r requirements.txt
```

### 3. Install Tesseract OCR

**Windows:**
```bash
# Download from: https://github.com/UB-Mannheim/tesseract/wiki
# Add to system PATH
```

**macOS:**
```bash
brew install tesseract
```

**Linux:**
```bash
sudo apt-get install tesseract-ocr
```

### 4. Run the API

```bash
uv run python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

### 5. Access the API

- **API Documentation**: http://127.0.0.1:8000/docs
- **Alternative Docs**: http://127.0.0.1:8000/redoc
- **Health Check**: http://127.0.0.1:8000/health

## 📚 API Endpoints

### Core Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Welcome message |
| `/health` | GET | Health check |
| `/supported-formats` | GET | List supported file formats |
| `/extract-mcq` | POST | Extract MCQs (auto-detects method) |
| `/extract-mcq-ocr` | POST | Force OCR extraction |
| `/extract-mcq-detailed` | POST | Detailed extraction with statistics |

### Debug & Analysis Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/debug-pdf` | POST | Analyze PDF extraction capabilities |
| `/test-ocr` | POST | Test OCR on images |

## 💡 Usage Examples

### Basic MCQ Extraction

```python
import requests

# Upload and extract MCQs
with open("questions.pdf", "rb") as f:
    files = {"file": ("questions.pdf", f, "application/pdf")}
    response = requests.post("http://127.0.0.1:8000/extract-mcq", files=files)

result = response.json()
print(f"Found {result['total_questions']} questions")

for mcq in result['mcqs']:
    print(f"Q{mcq['question_number']}: {mcq['question']}")
    for letter, option in mcq['options'].items():
        print(f"  {letter}: {option}")
    if mcq['correct_answer']:
        print(f"  Answer: {mcq['correct_answer']}")
```

### Detailed Analysis

```python
# Get detailed extraction statistics
response = requests.post("http://127.0.0.1:8000/extract-mcq-detailed", files=files)
result = response.json()

print(f"Extraction Method: {result['extraction_method']}")
print(f"Complete Questions: {result['complete_questions']}")
print(f"Text Quality: {result['text_analysis']}")
```

## 🧪 Testing

The project includes comprehensive tests:

```bash
# Run basic API tests
python test_api.py

# Test OCR functionality
python test_tesseract.py

# Test comprehensive extraction
python test_final_extraction.py

# Test OCR error handling
python test_ocr_errors.py
```

## 📊 Supported MCQ Formats

### Question Formats
- `1. What is the capital of France?`
- `1) What is the capital of France?`
- `Q1: What is the capital of France?`
- `Question: 1 What is the capital of France?`

### Option Formats
- Single line: `a. Paris b. London c. Berlin d. Madrid`
- Multi-line:
  ```
  a. Paris
  b. London
  c. Berlin
  d. Madrid
  ```
- Parentheses: `(a) Paris (b) London (c) Berlin (d) Madrid`

### Answer Formats
- `Answer: A`
- `Ans: A`
- `Correct: A`

## 🔧 Configuration

### Environment Variables

Create a `.env` file (optional):

```env
# API Configuration
HOST=127.0.0.1
PORT=8000

# OCR Configuration (Windows)
TESSERACT_PATH=C:\Program Files\Tesseract-OCR\tesseract.exe
```

### Tesseract Configuration

The API automatically detects Tesseract installation. For custom paths:

```python
# In main.py
pytesseract.pytesseract.tesseract_cmd = r'C:\path\to\tesseract.exe'
```

## 📈 Performance

- **Text-based PDFs**: ~100 questions/second
- **OCR Processing**: ~10-20 questions/second (depends on image quality)
- **Memory Usage**: ~100MB base + file size
- **Supported File Size**: Up to 50MB per file

## 🐛 Troubleshooting

### Common Issues

**OCR Not Working:**
```bash
# Check Tesseract installation
tesseract --version

# Install if missing (Windows)
# Download from: https://github.com/UB-Mannheim/tesseract/wiki
```

**Poor OCR Quality:**
- Use higher resolution scans (300+ DPI)
- Ensure good contrast and clear text
- Use the `/debug-pdf` endpoint to analyze extraction quality

**Missing Questions:**
- Check question numbering format
- Use `/extract-mcq-detailed` for statistics
- Verify file isn't corrupted or password-protected

### Debug Endpoints

Use the debug endpoints to diagnose issues:

```python
# Analyze PDF structure
response = requests.post("http://127.0.0.1:8000/debug-pdf", files=files)
print(response.json()['recommendation'])

# Test OCR quality
response = requests.post("http://127.0.0.1:8000/test-ocr", files=image_files)
print(response.json()['confidence'])
```

## 🚀 Deployment

### Docker Deployment

```dockerfile
FROM python:3.11-slim

# Install Tesseract
RUN apt-get update && apt-get install -y tesseract-ocr

WORKDIR /app
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Production Considerations

- Use a production ASGI server (e.g., Gunicorn with Uvicorn workers)
- Configure proper logging
- Set up rate limiting
- Use environment variables for configuration
- Monitor OCR processing resources

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

### Development Setup

```bash
# Clone and setup development environment
git clone https://github.com/yourusername/mcq-extractor-api.git
cd mcq-extractor-api

# Install development dependencies
uv sync --dev

# Run tests
python -m pytest

# Run with auto-reload
uv run python -m uvicorn main:app --reload
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) - OCR engine
- [PyMuPDF](https://github.com/pymupdf/PyMuPDF) - PDF processing
- [OpenCV](https://opencv.org/) - Image processing
- [Pillow](https://python-pillow.org/) - Image handling

## 📞 Support

- **Documentation**: Check the `/docs` endpoint when running the API
- **Issues**: Open an issue on GitHub
- **Discussions**: Use GitHub Discussions for questions

---

**Made with ❤️ for developers who need reliable MCQ extraction**
