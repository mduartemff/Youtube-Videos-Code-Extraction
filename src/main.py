"""
Main Application Module

This is the main entry point for the YouTube Video Code Extractor application.
It orchestrates the video processing, transcript extraction, OCR, and content analysis
using Groq's language models.
"""

from src.video_processing import process_video
from src.transcript_processing import process_transcript
from src.ocr_processing import process_frames
from src.groq_integration import analyze_transcript, analyze_extracted_text
from src.config import VIDEO_URL

def main():
    """
    Main function to process a YouTube video and extract/analyze its content.
    
    The function:
    1. Downloads the video and extracts frames
    2. Extracts and processes the video transcript
    3. Performs OCR on extracted frames
    4. Analyzes content using Groq's language models
    
    Returns:
        dict: Results containing transcript and frame analysis
        
    Raises:
        Exception: If any processing step fails
    """
    try:
        print("Starting video processing...")
        video_path, frames_dir = process_video(VIDEO_URL)
        print("✓ Video processing complete")
        
        print("\nExtracting transcript...")
        captions = process_transcript(VIDEO_URL)
        print(f"✓ Transcript extraction complete: {len(captions)} captions")
        
        print("\nProcessing frames with OCR...")
        frame_texts = process_frames(frames_dir)
        print(f"✓ OCR processing complete: {len(frame_texts)} frames with text")
        
        print("\nAnalyzing content with Groq...")
        transcript_analysis = analyze_transcript(captions)
        frame_analysis = analyze_extracted_text(frame_texts)
        print("✓ Content analysis complete")
        
        return {
            'transcript_analysis': transcript_analysis,
            'frame_analysis': frame_analysis
        }
        
    except Exception as e:
        print(f"\n✗ Processing failed: {str(e)}")
        raise e

if __name__ == "__main__":
    main() 