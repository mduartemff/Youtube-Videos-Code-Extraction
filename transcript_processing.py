import yt_dlp
import webvtt
import os
import glob

def process_transcript(video_url):
    base_path = "transcript"
    ydl_opts = {
        'skip_download': True,
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitleslangs': ['en'],
        'subtitlesformat': 'vtt',
        'outtmpl': base_path,
        'quiet': True,
    }
    
    # Clean up any existing VTT files
    for vtt_file in glob.glob(f"{base_path}*.vtt"):
        try:
            os.remove(vtt_file)
        except:
            pass
            
    # Download subtitles
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    
    # Find the downloaded VTT file
    vtt_files = glob.glob(f"{base_path}*.vtt")
    if not vtt_files:
        raise Exception("No subtitle file was downloaded")
    
    transcript_path = vtt_files[0]
    
    # Parse the transcript
    captions = []
    for caption in webvtt.read(transcript_path):
        captions.append({
            'start': caption.start,
            'end': caption.end,
            'text': caption.text
        })
    return captions
