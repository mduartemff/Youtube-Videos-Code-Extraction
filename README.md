
# YouTube Code Extractor

## Overview
The **YouTube Code Extractor** is a Python-based tool designed to automate the process of extracting, processing, and consolidating code snippets displayed in YouTube videos. It uses advanced OCR and integrates with Groq's LLM API (`llama-3.1-70b-versatile`) to enhance and contextualize extracted code snippets.

---

## Features
- **Automated Video Processing:**
  - Downloads YouTube videos and transcripts using `yt-dlp`.
- **Frame Extraction:**
  - Extracts video frames at a specified interval using `ffmpeg`.
- **OCR and Preprocessing:**
  - Reads and preprocesses extracted frames to identify code snippets using Tesseract OCR.
- **Code Consolidation:**
  - Uses Groq's LLM API to consolidate and improve extracted code snippets with contextual information from video transcripts.

---

## Requirements

### System Requirements
- Python 3.8 or later
- Internet connection (to download videos and interact with Groq's API)

### Dependencies
Install the following Python libraries using the provided `requirements.txt` file:
- `yt-dlp`
- `ffmpeg-python`
- `pytesseract`
- `opencv-python`
- `webvtt-py`
- `requests`

---

## Setup Instructions

### Step 1: Clone the Repository
Download the repository to your local machine:
```bash
git clone <repository-url>
cd yt_code_extractor
```

### Step 2: Set Up a Virtual Environment
Create and activate a virtual environment to manage dependencies:
```bash
python3 -m venv yt_code_extractor_env
source yt_code_extractor_env/bin/activate  # macOS/Linux
yt_code_extractor_env\Scripts\activate    # Windows
```

### Step 3: Install Dependencies
Install all required packages:
```bash
pip install -r requirements.txt
```

### Step 4: Install FFmpeg
Ensure `ffmpeg` is installed on your system and added to the PATH:
- **macOS/Linux:** Install via package manager:
  ```bash
  sudo apt install ffmpeg  # Debian/Ubuntu
  brew install ffmpeg      # macOS
  ```
- **Windows:** Download and install FFmpeg from [official website](https://ffmpeg.org/).

### Step 5: Install Tesseract OCR
Install Tesseract OCR on your system:
- **macOS:** Install via Homebrew:
  ```bash
  brew install tesseract
  ```
- **Linux:** Install via package manager:
  ```bash
  sudo apt install tesseract-ocr
  ```
- **Windows:** Download and install from [Tesseract GitHub](https://github.com/UB-Mannheim/tesseract).

### Step 6: Set the Groq API Key
Obtain your Groq API key and set it as an environment variable:
```bash
export GROQ_API_KEY="your_api_key"  # macOS/Linux
set GROQ_API_KEY=your_api_key       # Windows
```

---

## Usage

### Basic Usage
Run the program with a YouTube video URL:
```bash
python main.py <YouTube Video URL>
```

### Example
#### Input:
```bash
python main.py https://www.youtube.com/watch?v=example_video
```

#### Output:
The consolidated code will be saved in the `consolidated_code.py` file.

---

## Example Workflow
1. Provide a YouTube video URL containing coding examples.
2. The program downloads the video and transcript.
3. Frames are extracted, and OCR identifies code snippets.
4. The Groq LLM consolidates code snippets using transcript context.
5. The final code is saved to `consolidated_code.py`.

---

## Error Handling and Troubleshooting

### Common Errors
1. **`GROQ_API_KEY` Not Set:**
   - Ensure the API key is correctly set in your environment variables.
2. **FFmpeg Not Found:**
   - Verify FFmpeg is installed and added to your system PATH.
3. **Tesseract OCR Issues:**
   - Ensure Tesseract is installed and accessible via the command line.
4. **API Rate Limits:**
   - If the Groq API rate limit is exceeded, retry after some time.

### Debugging
Enable logging in the program to track errors and progress:
- Logs are saved in `yt_code_extractor.log`.

---

## Contributions
Contributions are welcome! Feel free to fork the repository, submit pull requests, or open issues.

---

## License
This project is licensed under the MIT License.
