# YouTube Video Downloader (GUI)

This is a Python-based GUI application for downloading YouTube videos using the `yt-dlp` library. The application features a user-friendly interface created with `tkinter` and allows users to download videos by providing a URL and selecting a save location.

---

## Features

- Simple and intuitive graphical user interface (GUI).
- Downloads videos in the best available quality.
- Allows users to specify the save location.
- Provides real-time status updates during the download process.

---

## Requirements

### Python Version

- Python 3.7 or higher

### Python Libraries

The following libraries are required to run the project:

- `yt-dlp`
- `tkinter` (included with Python by default)

---

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/youtube-video-downloader.git
cd youtube-video-downloader
```

### Step 2: Set Up Virtual Environment (Optional but Recommended)

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
2. Activate the virtual environment:
   - **Windows**:
     ```bash
     .venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source .venv/bin/activate
     ```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### Run the Application

1. Execute the Python script:
   ```bash
   python youtube_gui_downloader.py
   ```
2. Enter the YouTube video URL in the input box.
3. Select the destination folder where the video will be saved.
4. Click "Download Video" to start downloading.
5. The status of the download will be displayed at the bottom of the GUI.

---

## Converting to an Executable (.exe)

To create a standalone executable file:

1. Install `PyInstaller`:
   ```bash
   pip install pyinstaller
   ```
2. Generate the `.exe` file:
   ```bash
   pyinstaller --onefile --windowed youtube_gui_downloader.py
   ```
3. The executable will be located in the `dist` folder.

---

## Screenshots

[URL=[[https://imgbox.com/kYINXxZ2\][IMG\]https://thumbs2.imgbox.com/0f/7e/kYINXxZ2\_t.png[/IMG](https://imgbox.com/kYINXxZ2]\[IMG]https://thumbs2.imgbox.com/0f/7e/kYINXxZ2_t.png\[/IMG)][/URL](https://imgbox.com/kYINXxZ2]\[IMG]https://thumbs2.imgbox.com/0f/7e/kYINXxZ2_t.png\[/IMG]\[/URL)]

---

## Contribution

Feel free to contribute to this project by submitting issues or pull requests. Ensure your contributions align with the overall project goals and follow the code style guidelines.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for providing an excellent YouTube downloading library.
- The Python community for the amazing tools and libraries.

