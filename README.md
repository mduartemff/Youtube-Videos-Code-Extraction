# YouTube Videos Code Extractor

## Overview
The **YouTube Code Extractor** is a Python-based tool designed to automate the process of extracting, processing, and consolidating code snippets displayed in YouTube videos. It uses advanced OCR and integrates with Groq's LLM API to enhance and contextualize extracted code snippets.

---

## Features
- **Automated Video Processing:**
  - Downloads YouTube videos using `yt-dlp`
  - Extracts frames at configurable intervals using `ffmpeg`
- **Transcript Processing:**
  - Downloads and parses video subtitles/captions
  - Supports both manual and auto-generated subtitles
- **OCR Processing:**
  - Preprocesses frames for optimal text recognition
  - Extracts text from frames using Tesseract OCR
- **Content Analysis:**
  - Uses Groq's LLMs for content understanding
  - Analyzes both transcript and extracted text
  - Identifies code snippets and technical content

---

## Requirements

### System Requirements
- Python 3.8 or later
- FFmpeg for video processing
- Tesseract OCR for text extraction

### Dependencies
All dependencies are listed in `requirements.txt`:
```bash
python-dotenv==1.0.0
yt-dlp==2023.12.30
ffmpeg-python==0.2.0
pytesseract==0.3.10
opencv-python==4.8.1.78
webvtt-py==0.4.6
groq==0.4.2
pytest==7.4.4
```

---

## Setup Instructions

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd youtube-code-extractor
```

### Step 2: Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\activate   # Windows
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment
Create a `.env` file with your settings:
```bash
GROQ_API_KEY=your_groq_api_key
VIDEO_URL=https://www.youtube.com/watch?v=your_video_id
FRAME_RATE=0.5  # Extract one frame every 2 seconds
```

---

## Project Structure
```
youtube-code-extractor/
├── src/                         # Source code
│   ├── video_processing.py      # Video download and frame extraction
│   ├── transcript_processing.py # Subtitle processing
│   ├── ocr_processing.py        # Frame OCR and text extraction
│   ├── groq_integration.py      # Groq API integration
│   ├── config.py                # Configuration management
│   └── main.py                  # Main application entry point
├── tests/                       # Test suite
│   ├── test_video_processing.py
│   ├── test_transcript_processing.py
│   └── test_ocr_processing.py
├── docs/                        # Documentation
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
```

---

## Usage

### Basic Usage
```bash
python -m src.main
```

The program will:
1. Download the video specified in your `.env` file
2. Extract frames at the configured frame rate
3. Process the video transcript
4. Perform OCR on extracted frames
5. Analyze content using Groq's language model

### Running Tests
```bash
python -m pytest tests/
```
All tests include proper cleanup of temporary files and artifacts.

---

## Error Handling

### Common Issues
1. **Environment Setup:**
   - Ensure `.env` file exists with required variables
   - Check that GROQ_API_KEY is valid
2. **Video Processing:**
   - Verify FFmpeg is installed and in PATH
   - Check video URL is accessible
3. **OCR Processing:**
   - Ensure Tesseract OCR is installed
   - Verify frame extraction was successful

### Debugging
Enable detailed logging by setting appropriate log levels in the code.

---

## Contributions
Contributions are welcome! Feel free to fork the repository, submit pull requests, or open issues.

