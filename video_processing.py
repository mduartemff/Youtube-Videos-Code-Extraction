import yt_dlp
import ffmpeg
import os

def process_video(video_url):
    # Download the video
    output_path = "downloaded_video.mp4"
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': output_path,
        'quiet': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    # Extract frames
    frames_dir = "frames"
    os.makedirs(frames_dir, exist_ok=True)
    (
        ffmpeg
        .input(output_path)
        .output(f'{frames_dir}/frame_%04d.png', r=1)
        .run(quiet=True, overwrite_output=True)
    )
    return output_path, frames_dir
