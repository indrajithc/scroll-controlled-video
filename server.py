from flask import Flask, send_file, send_from_directory, request, abort
import os

app = Flask(__name__)

# Set the folders
VIDEO_FOLDER = "assets"
STATIC_FOLDER = ""

@app.route("/")
def serve_static_files():
    """Serve the main static index file."""
    return send_from_directory(STATIC_FOLDER, "index.html")

@app.route("/blob-video")
def serve_video():
    """Serve a specific video file."""
    video_path = os.path.join(VIDEO_FOLDER, "web-animation-flow.mp4")
    if not os.path.exists(video_path):
        return "Video not found", 404
    return send_file(video_path, mimetype="video/mp4")

@app.route("/assets/<path:filename>")
def serve_asset_file(filename):
    """Serve any file from the assets folder and its subfolders."""
    full_path = os.path.join(VIDEO_FOLDER, filename)
    if not os.path.isfile(full_path):
        abort(404)
    return send_from_directory(VIDEO_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
