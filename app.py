from __future__ import unicode_literals
from flask import Flask, redirect, request, render_template, send_file
import youtube_dl
import time


app = Flask(__name__)

@app.route("/out/<filename>", methods=["GET", "POST"])
def dossya(filename):
    return send_file(rf"out\{filename}", as_attachment=True)


@app.route("/", methods=["POST"])
def indir():
    if request.method == "POST":
        link = request.form.get("uri")
        fileName = str(time.time())
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
        'outtmpl': rf'out\{fileName}.mp3'
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            a = ydl.download([link])

        return f'<a href="/out/{fileName}.mp3" style="font-size: 15px;color: red;font-family: \'Rubik\';transition: 0.5s;text-decoration: none;" class="download" download="/out/{fileName}.mp3">DOWNLOAD</a>  '

@app.route("/", methods=["GET"])
def anasayfa():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
