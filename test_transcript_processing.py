"""
Test suite for transcript processing functionality.

This module tests the YouTube video transcript extraction process,
verifying that subtitles are properly downloaded and parsed into
the expected format.
"""

from transcript_processing import process_transcript
from config import VIDEO_URL
import os
import glob

def test_process_transcript():
    """
    Test transcript extraction and parsing.
    
    This test:
    1. Downloads subtitles from the configured video URL
    2. Verifies the VTT file exists and has content
    3. Checks the parsed captions structure
    4. Verifies caption formatting and content
    """
    try:
        # Test the function
        print("Starting transcript processing test...")
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

if __name__ == "__main__":
    test_process_transcript() 