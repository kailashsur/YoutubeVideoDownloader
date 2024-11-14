from django.http import StreamingHttpResponse
from django.shortcuts import render
import subprocess

def download_video(request):
    if request.method == "POST":
        url = request.POST.get("url")
        if url:
            response = StreamingHttpResponse(stream_video(url), content_type="video/mp4")
            response['Content-Disposition'] = 'attachment; filename="video.mp4"'
            return response
    return render(request, 'downloader/home.html')

def stream_video(url):
    yt_dlp_cmd = ['yt-dlp', '-f', 'best', '-o', '-', url]
    process = subprocess.Popen(yt_dlp_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for chunk in iter(lambda: process.stdout.read(1024), b""):
        yield chunk
