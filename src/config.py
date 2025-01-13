"""
Configuration Module

This module contains all configuration variables and settings
for the YouTube Video Code Extractor application.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Video processing settings
VIDEO_URL = os.getenv('VIDEO_URL', 'https://www.youtube.com/watch?v=your_default_video_id')
FRAME_RATE = float(os.getenv('FRAME_RATE', '0.5'))  # Extract one frame every 2 seconds by default

# Groq API settings
GROQ_API_KEY = os.getenv('GROQ_API_KEY', '') 