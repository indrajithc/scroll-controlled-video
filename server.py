from flask import Flask, send_file, send_from_directory, request
import os

app = Flask(__name__)

# Set the folder where video files and static files are stored
VIDEO_FOLDER = "assets"
STATIC_FOLDER = ""

@app.route("/")
def serve_static_files():
    """Serve static files from the 'static' folder."""
    return send_from_directory(STATIC_FOLDER, "index.html")

@app.route("/blob-video")
def serve_video():
    """Serve a video as a blob URL."""
    video_path = os.path.join(VIDEO_FOLDER, "web-animation-flow.mp4")
    
    # Check if the file exists
    if not os.path.exists(video_path):
        return "Video not found", 404
    
    return send_file(video_path, mimetype="video/mp4")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
