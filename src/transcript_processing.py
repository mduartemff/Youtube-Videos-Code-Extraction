"""
Transcript Processing Module

This module handles the extraction of transcripts from YouTube videos.
It uses yt-dlp for subtitle downloading and webvtt for parsing VTT format subtitles.
The module provides functionality to download, parse, and structure video captions.
"""

import yt_dlp
import webvtt
import os
import glob

def process_transcript(video_url):
    """
    Download and process subtitles from a YouTube video.
    
    Args:
        video_url (str): URL of the YouTube video to extract subtitles from
        
    Returns:
        list: List of dictionaries containing caption information:
            - start (str): Caption start time
            - end (str): Caption end time
            - text (str): Caption text content
            
    Raises:
        Exception: If subtitle download fails or no subtitles are available
        FileNotFoundError: If the downloaded subtitle file cannot be found
    """
    base_path = "transcript"
    ydl_opts = {
        'skip_download': True,          # Don't download the video
        'writesubtitles': True,         # Download subtitles if available
        'writeautomaticsub': True,      # Download auto-generated subtitles if manual not available
        'subtitleslangs': ['en'],       # Download English subtitles
        'subtitlesformat': 'vtt',       # Use VTT format
        'outtmpl': base_path,           # Output template for subtitle file
        'quiet': True,                  # Suppress yt-dlp output
    }
    
    # Clean up any existing VTT files
    for vtt_file in glob.glob(f"{base_path}*.vtt"):
        try:
            os.remove(vtt_file)
        except:
            pass
            
    # Download subtitles
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
    except Exception as e:
        raise Exception(f"Failed to download subtitles: {str(e)}")
    
    # Find the downloaded VTT file
    vtt_files = glob.glob(f"{base_path}*.vtt")
    if not vtt_files:
        raise Exception("No subtitle file was downloaded. The video might not have subtitles available.")
    
    transcript_path = vtt_files[0]
    
    # Parse the transcript
    try:
        captions = []
        for caption in webvtt.read(transcript_path):
            captions.append({
                'start': caption.start,
                'end': caption.end,
                'text': caption.text.strip()
            })
        return captions
    except Exception as e:
        raise Exception(f"Failed to parse subtitle file: {str(e)}") 