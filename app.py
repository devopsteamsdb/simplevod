import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)
VIDEO_FOLDER = os.path.join('static', 'videos')
THUMBNAIL_FOLDER = os.path.join('static', 'thumbnails')

@app.route('/')
def index():
    # Get the list of videos and thumbnails
    video_files = [f for f in os.listdir(VIDEO_FOLDER) if f.endswith(('.mp4', '.mov', '.avi', '.mkv'))]
    thumbnails = [f.replace('.mp4', '.jpg') for f in video_files]  # Assuming thumbnails are .jpg
    # Pass the zip() function to the template
    return render_template('index.html', videos=video_files, thumbnails=thumbnails, zip=zip)

@app.route('/stream/<filename>')
def stream_video(filename):
    return send_from_directory(VIDEO_FOLDER, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
