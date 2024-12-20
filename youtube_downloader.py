from pytube import YouTube

def download_video(video_url):
    try:
        # Create YouTube object
        yt = YouTube(video_url)

        # Display video title
        print(f"Downloading: {yt.title}")

        # Get the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()

        # Download the video
        video_stream.download()

        print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("YouTube Video Downloader")
    url = input("Enter the YouTube video URL: ")
    download_video(url)
