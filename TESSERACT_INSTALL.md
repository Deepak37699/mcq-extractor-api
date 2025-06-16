# Tesseract OCR Installation Guide 🔧

## Windows Installation

### Method 1: Direct Download (Recommended)

1. **Download Tesseract:**

   - Go to: https://github.com/UB-Mannheim/tesseract/wiki
   - Download the latest Windows installer (e.g., `tesseract-ocr-w64-setup-5.3.3.20231005.exe`)

2. **Install Tesseract:**

   - Run the installer as Administrator
   - Install to default location: `C:\Program Files\Tesseract-OCR\`
   - ✅ **IMPORTANT:** Check "Add to PATH" during installation

3. **Verify Installation:**
   ```cmd
   tesseract --version
   ```

### Method 2: Using Package Manager

```powershell
# Using Chocolatey
choco install tesseract

# Using Scoop
scoop install tesseract
```

### Method 3: Manual PATH Setup

If Tesseract is installed but not in PATH:

1. **Add to System PATH:**

   - Open System Properties → Environment Variables
   - Add to PATH: `C:\Program Files\Tesseract-OCR\`
   - Restart terminal/VS Code

2. **Or specify in code (temporary fix):**
   - API will handle this automatically

## After Installation

### Test Tesseract:

```bash
tesseract --version
tesseract --list-langs
```

### Test with API:

1. Visit: http://127.0.0.1:8000/docs
2. Try `/extract-mcq-ocr` with your PDF
3. Should now extract text from scanned pages

---

## Alternative Solutions (If you can't install Tesseract)

### Option 1: Online OCR

1. Use online OCR services to convert PDF to text
2. Save as .txt file
3. Upload to `/extract-mcq`

### Option 2: Manual Conversion

1. Extract pages as images from PDF
2. Use online OCR tools
3. Copy-paste text into .txt file

### Option 3: PDF Text Conversion

1. Use online PDF converters
2. Convert scanned PDF to text-based PDF
3. Re-upload to API

---

## Troubleshooting

### Common Issues:

- **"tesseract not found"** → Install Tesseract or add to PATH
- **"Permission denied"** → Run as Administrator
- **"Poor OCR quality"** → PDF images may be low resolution

### API Error Messages:

- `tesseract is not installed` → Follow installation guide above
- `OCR extraction failed` → Check Tesseract installation
- `No text could be extracted` → PDF may have very poor image quality

---

## Next Steps After Installation

1. **Restart VS Code/Terminal**
2. **Test installation:** `tesseract --version`
3. **Try your PDF again:** Upload to `/extract-mcq-ocr`
4. **Verify results:** Should extract MCQ questions from scanned pages

Your PDF: `Apex Civil engineer objective 2080-04-06.pdf` will work perfectly once Tesseract is installed! 🚀
