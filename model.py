import yt_dlp
import os
import subprocess

class YouTubeModel:
    def __init__(self, output_dir="Descargas"):
        self.output_dir = output_dir

    def download_video(self, video_url, select_format):
        ydl_opts = {
            'format': 'bestaudio/best',  # descargar solo el audio en el mejor formato posible
            'outtmpl': os.path.join(self.output_dir, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': select_format,
                'preferredquality': '192',
            }]
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
            return True, "DESCARGADO"
        except Exception as e:
            return False, str(e)

    def convert_video(self, input_file, output_file):
        command = ['ffmpeg', '-i', input_file, output_file]
        try:
            subprocess.run(command, check=True)
            return True, "CONVERTIDO"
        except Exception as e:
            return False, str(e)
