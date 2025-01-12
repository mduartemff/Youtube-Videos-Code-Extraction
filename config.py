import os

# Groq API Configuration
API_KEY = os.getenv("GROQ_API_KEY")
API_URL = "https://api.groq.com/openai/v1/chat/completions"

# Program Configuration
OUTPUT_FILE = "consolidated_code.py"
FRAME_RATE = 1  # Frames per second for extraction
MAX_TOKENS = 1000
TEMPERATURE = 0.2
