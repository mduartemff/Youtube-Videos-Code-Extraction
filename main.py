import argparse
from video_processing import process_video
from transcript_processing import process_transcript
from ocr_processing import process_frames
from groq_integration import consolidate_code_with_groq
from config import OUTPUT_FILE

def main():
    parser = argparse.ArgumentParser(description="YouTube Code Extractor")
    parser.add_argument('video_url', type=str, help='URL of the YouTube video to process')
    args = parser.parse_args()

    video_url = args.video_url

    # Step 1: Process Video and Extract Frames
    print("Processing video...")
    video_path, frames_dir = process_video(video_url)

    # Step 2: Process Transcript
    print("Processing transcript...")
    transcript = process_transcript(video_url)

    # Step 3: Process Frames for OCR
    print("Extracting text from frames...")
    extracted_data = process_frames(frames_dir)

    # Step 4: Consolidate Code using Groq
    print("Consolidating code using Groq...")
    consolidated_code = consolidate_code_with_groq(transcript, extracted_data)

    # Save consolidated code to file
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(consolidated_code)
    print(f"Consolidated code saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
