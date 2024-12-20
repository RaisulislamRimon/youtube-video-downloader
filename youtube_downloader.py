import yt_dlp

def download_video(video_url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',  # Save file as the video title
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("YouTube Video Downloader (yt-dlp)")
    url = input("Enter the YouTube video URL: ")
    download_video(url)
