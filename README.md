# YouTube Downloader for macOS

This is a simple YouTube Downloader application built using Python and PyQt5. The application allows users to download YouTube videos in the highest MP4 quality or extract audio in MP3 format. It features a user-friendly interface designed specifically for macOS.

---

## Features

- Download YouTube videos in **MP4** format at the best available quality.
- Extract audio in **MP3** format at high quality.
- Set custom save locations for downloads.
- Monitor download progress with a progress bar and speed display.
- Built-in macOS compatibility.

---

## Prerequisites

### 1. Python Installation
Ensure Python 3.x is installed on your macOS system. You can download it from [python.org](https://www.python.org/downloads/).

### 2. Required Libraries
Install the necessary Python libraries using pip:
```bash
pip install PyQt5 yt-dlp
```

### 3. FFmpeg Installation
Install FFmpeg via Homebrew:
```bash
brew install ffmpeg
```

---

## How to Run the Application

### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/youtube-downloader-macos.git
cd youtube-downloader-macos
```

### 2. Run the Application
Execute the script using Python:
```bash
python main.py
```

---

## Building the macOS App

### 1. Install PyInstaller
```bash
pip install pyinstaller
```

### 2. Create the Application
Generate a standalone macOS app:
```bash
pyinstaller --name "YouTubeDownloader" --windowed --onefile main.py
```

### 3. Add Resources
Ensure that the app includes all required resources (e.g., icons) by modifying the `.spec` file if needed. Rebuild the app with:
```bash
pyinstaller YouTubeDownloader.spec
```

### 4. Locate the App
The generated app will be in the `dist` folder.

---

## Screenshots
Add screenshots of your application here to showcase the interface and functionality.

---

## Known Issues
- Ensure a stable internet connection for downloading.
- Make sure FFmpeg is properly installed and accessible via the terminal.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contribution
Feel free to contribute to the project by submitting issues or pull requests.

---

## Acknowledgments
- [PyQt5 Documentation](https://riverbankcomputing.com/software/pyqt/intro)
- [yt-dlp Documentation](https://github.com/yt-dlp/yt-dlp)

