Here's a GitHub README template for your project, titled `ReadArea.py`:

---

# Unallowed Area Surveillance System

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![YOLOv8](https://img.shields.io/badge/YOLOv8-DeepLearning-green)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-orange)
![Telegram](https://img.shields.io/badge/Telegram-Integration-red)

## Overview

The **Unallowed Area Surveillance System** is a Python-based security application that uses YOLOv8 for real-time object detection. The system monitors a user-defined area within a video feed and triggers an alarm and Telegram alert when an unauthorized person enters the restricted zone.

## Features

- **Real-time Detection**: Monitors a specified area within a video feed using YOLOv8 object detection.
- **Polygonal Area Definition**: Allows users to define the restricted zone by drawing a polygon on the video frame.
- **Alarm System**: Triggers an audible alarm when an intrusion is detected.
- **Telegram Notifications**: Sends a snapshot of the intrusion to a predefined Telegram chat.
- **Customizable Monitoring**: Users can specify which object classes (e.g., "person") should be detected for intrusion.

## Technologies Used

- **[Python](https://www.python.org/)**: Programming language used for scripting the system.
- **[OpenCV](https://opencv.org/)**: Library for computer vision tasks such as video capture and image processing.
- **[YOLOv8](https://github.com/ultralytics/yolov8)**: Deep learning model for real-time object detection.
- **[Pygame](https://www.pygame.org/)**: Library used for handling the alarm sound.
- **[Telepot](https://github.com/nickoala/telepot)**: Library for integrating Telegram with Python.

## Setup and Installation

### Prerequisites

Ensure you have Python 3.8+ installed on your machine. Install the required Python packages using pip:

```bash
pip install opencv-python ultralytics numpy pygame telepot
```

### Configuration

1. **Project Directory**:
    - Update the `os.chdir()` path in `ReadArea.py` to match the directory where your project is located.
  
2. **Telegram Integration**:
    - Replace the placeholder `bot = telepot.Bot('YOUR_BOT_API_TOKEN')` and `chat_id = 'YOUR_CHAT_ID'` with your actual Telegram bot token and chat ID.

3. **Audio Alert**:
    - Ensure the `alarm.wav` file is in the project directory, or update the path in the script to point to your alarm sound file.

### Running the Application

1. Place your video file in the project directory or update the `cap = cv2.VideoCapture("your_video_file.mp4")` line in `ReadArea.py` to point to your video source.
2. Run the script:

```bash
python ReadArea.py
```

3. Define the restricted area by clicking points on the video frame. Right-click to clear and start over.
4. The system will monitor the defined area and trigger an alarm and Telegram alert if an intrusion is detected.

## How It Works

- The script loads the YOLOv8 model and captures video frames using OpenCV.
- Users can draw a polygonal region on the video frame, which defines the restricted area to be monitored.
- YOLOv8 detects objects in each frame, and the system checks if any detected objects are within the defined polygon.
- If an object is detected inside the polygon, an alarm sounds, and a photo of the intrusion is sent to a specified Telegram chat.

## Example Usage

```python
# Set the project directory
os.chdir(r"F:\YOLO Projects\UnallowedArea")

# Load the YOLO model
model = YOLO("yolov8n.pt")

# Set up Telegram bot
bot = telepot.Bot('YOUR_BOT_API_TOKEN')
chat_id = 'YOUR_CHAT_ID'
```
