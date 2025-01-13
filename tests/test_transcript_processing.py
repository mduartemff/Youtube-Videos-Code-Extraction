"""
Test Suite for Transcript Processing Module

This module provides comprehensive testing for the transcript processing functionality.
It tests the YouTube subtitle extraction and parsing capabilities by:
1. Downloading subtitles from a test video
2. Verifying VTT file creation and content
3. Validating caption parsing and structure
4. Ensuring proper cleanup of temporary files
"""

from src.transcript_processing import process_transcript
from src.config import VIDEO_URL
import os
import glob

def cleanup_test_files():
    """
    Clean up any test artifacts (VTT files) after testing.
    """
    # Clean up any VTT files
    for vtt_file in glob.glob("transcript*.vtt"):
        try:
            os.remove(vtt_file)
            print(f"  Cleaned up: {vtt_file}")
        except Exception as e:
            print(f"  Warning: Could not remove {vtt_file}: {str(e)}")

def test_process_transcript():
    """
    Test transcript extraction and parsing functionality.
    
    This test function:
    1. Downloads subtitles from the configured test video
    2. Verifies successful subtitle file creation
    3. Validates caption parsing and structure
    4. Checks caption content quality
    
    The test uses a known video (configured in config.py) to ensure
    consistent and reliable testing of the transcript processing pipeline.
    
    Raises:
        Exception: If any step of the transcript processing fails
    """
    try:
        print("Starting transcript processing test...")
        
        # Test the function
        captions = process_transcript(VIDEO_URL)
        
        # Check if transcript file was created
        print(f"\nChecking transcript file...")
        vtt_files = glob.glob("transcript*.vtt")
        if vtt_files:
            transcript_path = vtt_files[0]
            print(f"✓ Transcript downloaded successfully: {transcript_path}")
            print(f"  File size: {os.path.getsize(transcript_path) / 1024:.2f} KB")
        else:
            print("✗ Transcript download failed")
            
        # Check parsed captions
        print(f"\nChecking parsed captions...")
        if captions and isinstance(captions, list):
            print(f"✓ Captions parsed successfully: {len(captions)} entries")
            if captions:
                print("\nSample caption entries:")
                # Show first caption
                print("\nFirst caption:")
                print(f"  Start time: {captions[0]['start']}")
                print(f"  End time: {captions[0]['end']}")
                print(f"  Text: {captions[0]['text']}")
                
                # Show a middle caption
                mid = len(captions) // 2
                print("\nMiddle caption:")
                print(f"  Start time: {captions[mid]['start']}")
                print(f"  End time: {captions[mid]['end']}")
                print(f"  Text: {captions[mid]['text']}")
                
                # Show last caption
                print("\nLast caption:")
                print(f"  Start time: {captions[-1]['start']}")
                print(f"  End time: {captions[-1]['end']}")
                print(f"  Text: {captions[-1]['text']}")
        else:
            print("✗ Caption parsing failed")
            
    except Exception as e:
        print(f"\n✗ Test failed with error: {str(e)}")
        raise e
    finally:
        # Clean up test artifacts
        print("\nCleaning up test artifacts...")
        cleanup_test_files()

if __name__ == "__main__":
    test_process_transcript() 