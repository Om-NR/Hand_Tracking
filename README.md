
# 🖐️ Hand Gesture Controlled Virtual Mouse

Control your computer using hand gestures!

A Python-based computer vision project that transforms hand movements into mouse actions using a webcam.

## ✨ Features

- 🖱️ Cursor movement
- 👆 Left click
- 👉 Right click
- 🤏 Double click
- ✊ Drag and drop
- 📜 Scrolling
- 🔍 Zoom in and zoom out
- ✋ Cursor freezing

## 🛠️ Technologies

- Python
- OpenCV
- MediaPipe
- PyAutoGUI

## 📂 Project Structure

```text
moew/
├── app.py
├── controller.py
├── hand_landmarker.task
├── requirements.txt
├── README.md
├── gestures/
└── fingers names.png
```

## 💻 Installation

### Requirements
- Windows 10 or Windows 11
- Python 3.11 (64-bit recommended)
- Working webcam

### 1. Clone or download this repository

Download the repository ZIP from GitHub and extract it.

### 2. Open the project folder

Open a terminal in the extracted folder.

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the environment

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the project

```bash
python app.py
```

Press ESC to exit the application.

## ⚠️ Notes

- Allow webcam access.
- Keep hand_landmarker.task in the same directory as app.py.
- Good lighting improves hand tracking.
- Save your work before testing gestures because this application controls your real mouse.

## 🚀 Future Improvements

- Better gesture accuracy
- Cursor smoothing
- Custom gestures
- Improved user interface

## 👨‍💻 Author

**Om**

Made with Python ❤️
