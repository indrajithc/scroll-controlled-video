# Scroll Controlled Video 🎥🚀

This project enables a **smooth scroll-based video control** where the video progresses as the user scrolls. The playback is dynamically mapped to the scroll position, ensuring a **lag-free, precise experience**.

## 🌟 Features
- **Smooth video time interpolation** to prevent jumps.
- **Dynamically scaled scroll range** based on video length.
- **Optimized with floating-point precision (3 decimal places).**
- **Works with any video source.**
- Also supports **scroll-controlled image frame sequences**.

## 📜 How It Works
- The page height is dynamically set based on the video duration.
- As you scroll, the video time (or image frame) updates smoothly.
- Uses **requestAnimationFrame()** to ensure fluid updates.

## 🛠️ Convert Video to Image Frames (Optional)

To use image sequences instead of a video element (for better cross-browser control or creative effects), you can extract frames using `ffmpeg`:

```sh
ffmpeg -i input.mp4 -vf "fps=30" frames/frame_%04d.jpg
```

- `fps=30`: Extract 30 frames per second.
- `frame_%04d.jpg`: Names frames as `frame_0001.jpg`, `frame_0002.jpg`, etc.
- Place extracted images into a folder (e.g., `/assets/frames`) and load them with JavaScript.

Update your JS to match the number of frames:
```js
const frameCount = 1800; // adjust based on your video FPS * duration
```

## 🚀 Setup & Usage
1. Clone the repository:
   ```sh
   git clone https://github.com/indrajithc/scroll-controlled-video.git
   cd scroll-controlled-video
   ```
2. Open `index.html` in your browser.
3. Replace the `<video>` source or point to your own image frames.
4. Scroll to control the video or animation!

## 📷 Demo
[Add a GIF or video link demonstrating the feature]

## 💡 Future Improvements
- Add **scroll-speed customization**.
- Implement **mobile touch controls**.
- Support for **multiple videos** or frame sets on the same page.

## 📝 License
This project is open-source under the [MIT License](LICENSE).
```

---

Let me know if you want to split the README into two sections — one for video and one for frame-based control — or include a sample `index.html` structure.