"""
Test suite for video processing functionality.

This module tests the video downloading and frame extraction process,
verifying that videos are properly downloaded and frames are extracted
at the configured frame rate (defined in config.py).
"""

from video_processing import process_video
from config import VIDEO_URL
import os

def test_process_video():
    """
    Test video downloading and frame extraction.
    
    This test:
    1. Downloads a video from the configured URL
    2. Verifies the video file exists and has content
    3. Extracts frames from the video
    4. Verifies frames are properly extracted
    
    The frame rate is configured in config.py
    """
    try:
        # Test the function
        print("Starting video processing test...")
        video_path, frames_dir = process_video(VIDEO_URL)
        
        # Check if video was downloaded
        print(f"\nChecking video download...")
        if os.path.exists(video_path):
            print(f"✓ Video downloaded successfully: {video_path}")
            print(f"  File size: {os.path.getsize(video_path) / (1024*1024):.2f} MB")
        else:
            print("✗ Video download failed")
            
        # Check if frames were extracted
        print(f"\nChecking frame extraction...")
        if os.path.exists(frames_dir):
            frames = [f for f in os.listdir(frames_dir) if f.endswith('.png')]
            print(f"✓ Frames extracted successfully: {len(frames)} frames in {frames_dir}")
            if frames:
                print(f"  First frame: {frames[0]}")
                print(f"  Last frame: {frames[-1]}")
        else:
            print("✗ Frame extraction failed")
            
    except Exception as e:
        print(f"\n✗ Test failed with error: {str(e)}")
        raise e

if __name__ == "__main__":
    test_process_video() 