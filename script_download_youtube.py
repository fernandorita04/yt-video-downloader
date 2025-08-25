import subprocess
from pathlib import Path
from pytubefix import YouTube
import tkinter as tk
from tkinter import filedialog, messagebox
import re

def progresso(stream, chunk, bytes_remaining):
    total = stream.filesize
    downloaded = total - bytes_remaining
    percent = downloaded / total * 100
    print(f"Baixado: {percent:.2f}%")

def baixar_video():
    url = entrada_url.get()
    if not url:
        messagebox.showerror("Erro", "Informe a URL do vídeo")
        return

    destino = Path(filedialog.askdirectory() or ".")
    try:
        yt = YouTube(url, on_progress_callback=progresso)
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao acessar o vídeo: {e}")
        return

    safe_title = re.sub(r'[\\/*?:"<>|]',"", yt.title)
    output_file = destino / f"{safe_title}.mp4"

    try:
        video_stream = yt.streams.filter(only_video=True, file_extension="mp4").order_by("resolution").desc().first()
        audio_stream = yt.streams.filter(only_audio=True, file_extension="mp4").order_by("abr").desc().first()

        video_file = destino / "temp_video.mp4"
        audio_file = destino / "temp_audio.mp4"

        video_stream.download(output_path=destino, filename=video_file.name)
        audio_stream.download(output_path=destino, filename=audio_file.name)

        subprocess.run([
            "ffmpeg", "-y",
            "-i", str(video_file),
            "-i", str(audio_file),
            "-c:v", "copy",
            "-c:a", "aac",
            "-strict", "experimental",
            str(output_file)
        ], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

        video_file.unlink()
        audio_file.unlink()
        messagebox.showinfo("Concluído", f"Vídeo salvo em:\n{output_file}")

    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao baixar ou processar o vídeo: {e}")

root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("400x150")

tk.Label(root, text="URL do vídeo:").pack(pady=5)
entrada_url = tk.Entry(root, width=50)
entrada_url.pack(pady=5)

btn = tk.Button(root, text="Baixar", command=baixar_video)
btn.pack(pady=10)

root.mainloop()
