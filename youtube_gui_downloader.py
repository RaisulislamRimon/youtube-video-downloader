import os
import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp

class YouTubeDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Video Downloader")
        self.root.geometry("500x200")

        # URL Label and Entry
        self.url_label = tk.Label(root, text="YouTube Video URL:")
        self.url_label.pack(pady=5)
        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack(pady=5)

        # Destination Folder Label and Button
        self.destination_label = tk.Label(root, text="Save Location:")
        self.destination_label.pack(pady=5)
        self.destination_button = tk.Button(
            root, text="Choose Folder", command=self.choose_folder
        )
        self.destination_button.pack(pady=5)
        self.destination_path = tk.StringVar()
        self.destination_path.set(os.getcwd())  # Default to current working directory

        # Download Button
        self.download_button = tk.Button(
            root, text="Download Video", command=self.download_video
        )
        self.download_button.pack(pady=10)

        # Status Label
        self.status_label = tk.Label(root, text="")
        self.status_label.pack(pady=5)

    def choose_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.destination_path.set(folder)

    def download_video(self):
        video_url = self.url_entry.get()
        save_path = self.destination_path.get()

        if not video_url:
            messagebox.showerror("Error", "Please enter a YouTube URL")
            return

        self.status_label.config(text="Downloading...", fg="blue")
        self.root.update()

        ydl_opts = {
            "format": "best",
            "outtmpl": os.path.join(save_path, "%(title)s.%(ext)s"),
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
            self.status_label.config(text="Download completed!", fg="green")
        except Exception as e:
            self.status_label.config(text="Download failed!", fg="red")
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloaderApp(root)
    root.mainloop()
