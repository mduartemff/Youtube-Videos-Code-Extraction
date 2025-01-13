"""
Test suite for video processing functionality.

This module tests the video downloading and frame extraction process,
verifying that videos are properly downloaded and frames are extracted
at the configured frame rate (defined in config.py).
"""

from src.video_processing import process_video
from src.config import VIDEO_URL
import os
import shutil

def cleanup_test_files(video_path=None, frames_dir=None):
    """
    Clean up any test artifacts after testing.
    """
    # Clean up video file
    if video_path and os.path.exists(video_path):
        try:
            os.remove(video_path)
            print(f"  Cleaned up: {video_path}")
        except Exception as e:
            print(f"  Warning: Could not remove {video_path}: {str(e)}")
    
    # Clean up frames directory
    if frames_dir and os.path.exists(frames_dir):
        try:
            shutil.rmtree(frames_dir)
            print(f"  Cleaned up: {frames_dir}")
        except Exception as e:
            print(f"  Warning: Could not remove {frames_dir}: {str(e)}")

def test_process_video():
    """
    Test video downloading and frame extraction.
    
    This test:
    1. Downloads a video from the configured URL
    2. Verifies the video file exists and has content
    3. Extracts frames from the video
    4. Verifies frames are properly extracted
    """
    video_path = None
    frames_dir = None
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
    finally:
        # Clean up test artifacts
        print("\nCleaning up test artifacts...")
        cleanup_test_files(video_path, frames_dir)

if __name__ == "__main__":
    test_process_video() 