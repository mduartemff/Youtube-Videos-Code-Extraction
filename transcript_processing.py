import yt_dlp
import webvtt

def process_transcript(video_url):
    transcript_path = "transcript.vtt"
    ydl_opts = {
        'skip_download': True,
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitleslangs': ['en'],
        'subtitlesformat': 'vtt',
        'outtmpl': transcript_path,
        'quiet': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    # Parse the transcript
    captions = []
    for caption in webvtt.read(transcript_path):
        captions.append({
            'start': caption.start,
            'end': caption.end,
            'text': caption.text
        })
    return captions
