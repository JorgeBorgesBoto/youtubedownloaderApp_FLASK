from flask import Flask, request, render_template, redirect, url_for
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    yt = YouTube(url)
    video_quality = request.form['video_quality']
    video = yt.streams.filter(progressive=True, file_extension='mp4', res=video_quality).first()
    video.download()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)