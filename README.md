# Scroll Controlled Video 🎥🚀

This project enables a **smooth scroll-based video control** where the video progresses as the user scrolls. The playback is dynamically mapped to the scroll position, ensuring a **lag-free, precise experience**.

## 🌟 Features
- **Smooth video time interpolation** to prevent jumps.
- **Dynamically scaled scroll range** based on video length.
- **Optimized with floating-point precision (3 decimal places).**
- **Works with any video source**.

## 📜 How It Works
- The page height is dynamically set based on the video duration.
- As you scroll, the video time updates smoothly.
- Uses **requestAnimationFrame()** to ensure fluid updates.

## 🚀 Setup & Usage
1. Clone the repository:
   ```sh
   git clone https://github.com/indrajithc/scroll-controlled-video.git
   cd scroll-controlled-video
   ```
2. Open `index.html` in your browser.
3. Replace the `<video>` source URL with your own video file.
4. Scroll to control the video!

## 📷 Demo
[Add a GIF or video link demonstrating the feature]

## 💡 Future Improvements
- Add **scroll-speed customization**.
- Implement **mobile touch controls**.
- Support for **multiple videos** on the same page.

## 📝 License
This project is open-source under the [MIT License](LICENSE).
