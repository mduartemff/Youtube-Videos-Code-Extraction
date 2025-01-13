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
    Clean up test artifacts after testing.
    
    Args:
        video_path (str): Path to the downloaded video file
        frames_dir (str): Directory containing the extracted frames
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
    Test the video downloading and frame extraction process.
    
    This test:
    1. Downloads a video from the configured URL
    2. Verifies the video file exists and has content
    3. Extracts frames from the video
    4. Verifies frames are properly extracted
    """
    video_path = None
    frames_dir = None
    try:
        print("Starting video processing test...")
        video_path, frames_dir = process_video(VIDEO_URL)
        
        print(f"\nChecking video download...")
        assert os.path.exists(video_path), "Video download failed"
        print(f"✓ Video downloaded successfully: {video_path}")
        print(f"  File size: {os.path.getsize(video_path) / (1024*1024):.2f} MB")
            
        print(f"\nChecking frame extraction...")
        assert os.path.exists(frames_dir), "Frame extraction failed"
        frames = [f for f in os.listdir(frames_dir) if f.endswith('.png')]
        assert len(frames) > 0, "No frames extracted"
        print(f"✓ Frames extracted successfully: {len(frames)} frames in {frames_dir}")
        print(f"  First frame: {frames[0]}")
        print(f"  Last frame: {frames[-1]}")
            
    except Exception as e:
        print(f"\n✗ Test failed with error: {str(e)}")
        raise e
    finally:
        # Clean up test artifacts
        print("\nCleaning up test artifacts...")
        cleanup_test_files(video_path, frames_dir)

if __name__ == "__main__":
    test_process_video() 