"""
Video Processing Module

This module handles the downloading and frame extraction of YouTube videos.
It uses yt-dlp for video downloading and ffmpeg for frame extraction.
The frame rate and other configurations are controlled via config.py.
"""

import yt_dlp
import ffmpeg
import os
import shutil
from src.config import FRAME_RATE

def process_video(video_url):
    """
    Download a YouTube video and extract frames at specified intervals.

    Args:
        video_url (str): URL of the YouTube video to process

    Returns:
        tuple: (video_path, frames_dir) where:
            - video_path (str): Path to the downloaded video file
            - frames_dir (str): Directory containing the extracted frames

    Raises:
        Exception: If video download fails or frame extraction fails
    """
    # Download the video with specific format preferences
    output_path = "downloaded_video.mp4"
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',  # Ensure we get MP4 format
        'outtmpl': output_path,
        'quiet': False,  # Show download progress
        'no_warnings': False,  # Show warnings
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
    except Exception as e:
        print(f"Error downloading video: {str(e)}")
        raise

    if not os.path.exists(output_path):
        raise Exception(f"Video download failed: {output_path} not found")

    # Clean and create frames directory
    frames_dir = "frames"
    if os.path.exists(frames_dir):
        shutil.rmtree(frames_dir)
    os.makedirs(frames_dir)

    # Extract frames using ffmpeg
    # FRAME_RATE of 0.5 means one frame every 2 seconds
    try:
        (
            ffmpeg
            .input(output_path)
            .output(f'{frames_dir}/frame_%04d.png', r=FRAME_RATE)
            .run(quiet=False, overwrite_output=True)
        )
    except ffmpeg.Error as e:
        print(f"Error extracting frames: {str(e)}")
        raise

    return output_path, frames_dir 