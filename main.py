import sys
import os
from PyQt5 import QtWidgets, QtGui, QtCore
from yt_dlp import YoutubeDL
from PyQt5.QtCore import Qt

class YouTubeDownloader(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # UI Setup
        self.setWindowTitle("YouTube Video Downloader")
        self.setGeometry(100, 100, 500, 400)
        self.setWindowIcon(QtGui.QIcon("icon.png"))  # Program Icon (You can change it)

        # Widgets setup
        self.url_label = QtWidgets.QLabel("Video URL:")
        self.url_entry = QtWidgets.QLineEdit(self)
        self.url_entry.setPlaceholderText("Enter video URL here...")

        self.audio_checkbox = QtWidgets.QCheckBox("Download audio only (MP3)", self)

        self.folder_button = QtWidgets.QPushButton("Choose Save Location", self)
        self.folder_button.clicked.connect(self.choose_folder)

        self.download_button = QtWidgets.QPushButton("Download", self)
        self.download_button.clicked.connect(self.download_video)

        # Progress bar
        self.progress_bar = QtWidgets.QProgressBar(self)
        self.progress_bar.setAlignment(Qt.AlignCenter)
        self.progress_bar.setRange(0, 100)  # Set range from 0 to 100
        self.progress_bar.setValue(0)  # Start from 0

        # Information labels
        self.speed_label = QtWidgets.QLabel("Download Speed: 0 KB/s")
        self.progress_label = QtWidgets.QLabel("Download Progress: 0%")

        # Layout Setup
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.url_label)
        layout.addWidget(self.url_entry)
        layout.addWidget(self.audio_checkbox)
        layout.addWidget(self.folder_button)
        layout.addWidget(self.download_button)
        layout.addWidget(self.progress_label)  # Add progress percentage label
        layout.addWidget(self.speed_label)  # Add speed label
        layout.addWidget(self.progress_bar)  # Add progress bar

        self.setLayout(layout)

        self.download_folder = os.path.expanduser("~/Downloads")  # Default folder

    def choose_folder(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Choose Save Folder")
        if folder:
            self.download_folder = folder

    def download_video(self):
        url = self.url_entry.text()
        if not url:
            QtWidgets.QMessageBox.warning(self, "Error", "Please enter the video URL.")
            return
        
        is_audio = self.audio_checkbox.isChecked()

        # Set ffmpeg path for macOS (assuming it's installed via Homebrew)
        ffmpeg_path = '/usr/local/bin/ffmpeg'  # Update this if necessary

        if is_audio:
            # Download audio as MP3 (highest quality)
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(self.download_folder, '%(title)s.%(ext)s'),
                'ffmpeg_location': ffmpeg_path,  # macOS ffmpeg location
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',  # Correct postprocessor for audio conversion
                    'preferredcodec': 'mp3',  # Convert audio to mp3
                    'preferredquality': '192',  # Set preferred audio quality
                }],
                'progress_hooks': [self.progress_hook],
                'nocheckcertificate': True,
            }
        else:
            # Download video as MP4 (best quality)
            ydl_opts = {
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',  # Best quality MP4
                'outtmpl': os.path.join(self.download_folder, '%(title)s.%(ext)s'),
                'ffmpeg_location': ffmpeg_path,  # macOS ffmpeg location
                'progress_hooks': [self.progress_hook],
                'nocheckcertificate': True,
            }

        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            QtWidgets.QMessageBox.information(self, "Success", "Download completed successfully!")
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Error", f"An error occurred during download: {e}")

    def progress_hook(self, d):
        """ Update progress bar and show download speed and progress """
        if d['status'] == 'downloading':
            # Calculate progress percentage
            percent = d.get('percent', 0)
            self.progress_bar.setValue(percent)
            self.progress_label.setText(f"Download Progress: {percent}%")

            # Calculate download speed (in KB/s)
            speed = d.get('speed', 0) / 1024  # Convert from bytes to KB
            self.speed_label.setText(f"Download Speed: {speed:.2f} KB/s")

        elif d['status'] == 'finished':
            self.progress_bar.setValue(100)  # Set progress bar to 100% when finished
            self.progress_label.setText("Download Progress: 100%")
            self.speed_label.setText("Download Speed: Finished")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = YouTubeDownloader()
    window.show()
    sys.exit(app.exec_())
