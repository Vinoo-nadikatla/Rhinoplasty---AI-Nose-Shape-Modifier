# Rhinoplasty---AI-Nose-Shape-Modifier
I have developing a system that detects facial landmarks using MediaPipe, isolates the nose region, and applies reshaping styles like “Slim &amp; Board” through image warping.

# 🤖 AI-Powered Nose Reshaping (Rhinoplasty) Challenge

This project allows users to visualize different nose shapes on their uploaded photo using AI-based landmark detection and image warping techniques. Built with Streamlit and OpenCV, it provides a fun and intuitive way to simulate nose reshaping styles such as "Narrow & Pointed", "Broad & Rounded", and more.

## ✨ Features

- 🧠 **Facial Landmark Detection** using MediaPipe
- 👃 **Nose Isolation** and reshaping with custom landmark manipulation
- 🎭 **Style Transformations**:
  - Narrow & Pointed
  - Broad & Rounded
  - Upturned (Button Nose)
  - Downturned
  - Greek Straight
- 🔄 **Before & After Visualization**
- 🌐 Streamlit interface for real-time user interaction

## 🛠️ Technologies Used

- Python
- OpenCV
- MediaPipe
- NumPy
- Streamlit
- Google Colab (for prototyping)

## 📸 How It Works

1. **Upload a face image** via Streamlit.
2. **Detect facial landmarks** using MediaPipe's FaceMesh.
3. **Extract nose landmarks** and apply custom reshaping rules.
4. **Warp the nose region** using affine transformations and Delaunay triangulation.
5. **Display before and after images** side-by-side.

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- Install dependencies:

```bash
pip install opencv-python mediapipe streamlit numpy

**Project Structure**
├── app.py                # Streamlit app (UI)
├── nose_utils.py         # Landmark reshaping logic
├── assets/
│   └── sample_image.jpg  # Example input image
├── README.md             # Project documentation

**✅ To Do**

 Add more reshaping styles

 Integrate with GAN-based models

 Enable download option for output image

 Add drag-to-compare UI slider

