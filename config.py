import os

# Groq API Configuration
API_KEY = os.getenv("GROQ_API_KEY")
API_URL = "https://api.groq.com/openai/v1/chat/completions"

# Program Configuration
OUTPUT_FILE = "transcribed_code.py"
FRAME_RATE = 0.5  # One frame every 2 seconds
    
# LLM Configuration
MAX_TOKENS = 1000
TEMPERATURE = 0.2

# Video Configuration
VIDEO_URL = "https://www.youtube.com/watch?v=zdmz81_gn2I"  # URL of the YouTube video to process
