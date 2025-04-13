import streamlit as st
import cv2
import numpy as np
import mediapipe as mp
from PIL import Image

# Initialize Mediapipe
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1)

# Nose landmark indices
nose_indices = [98, 327, 2, 5, 195, 4]

def get_landmarks(image):
    """Detect facial landmarks and return them in pixel coordinates."""
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result = face_mesh.process(rgb_image)
    if result.multi_face_landmarks:
        h, w = image.shape[:2]
        return np.array([[int(lm.x * w), int(lm.y * h)] for lm in result.multi_face_landmarks[0].landmark])
    return None

def slim_nose_warp(image, landmarks, factor=0.3):
    """Warp the nose inward (slim nose)."""
    modified_landmarks = landmarks.copy()

    # Calculate center of nostrils
    left = landmarks[98]
    right = landmarks[327]
    center = ((left[0] + right[0]) // 2, (left[1] + right[1]) // 2)

    # Move nostrils inward
    modified_landmarks[98][0] += int((center[0] - left[0]) * factor)
    modified_landmarks[327][0] += int((center[0] - right[0]) * factor)

    return modified_landmarks

# Streamlit App
st.title("Rhinoplasty Challenge")
st.write("AI Nose Shape Modification")
st.write("Upload your front-facing image and choose a nose shape.")

uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    image = np.array(image)

    # Show the original image
    st.image(image, caption="Original Image", use_column_width=True)

    # Get landmarks from image
    landmarks = get_landmarks(image)

    if landmarks is not None:
        # Let user choose the nose shape
        nose_shape = st.selectbox("Choose Nose Shape", ["Slim", "Broad", "Upturned"])

        # Apply transformation based on selected shape
        if nose_shape == "Slim":
            transformed_landmarks = slim_nose_warp(image, landmarks, factor=0.3)  # Adjust the factor for slim nose
        # Add other shapes here like Broad or Upturned with different transformations

        # Apply the transformation to the image (can add more logic here for different shapes)
        transformed_image = image.copy()
        # Update this part with more transformation logic as needed

        # Display modified image side by side
        st.image(np.hstack([image, transformed_image]), caption="Original vs Modified", use_column_width=True)

        # Optionally: allow users to download the modified image
        if st.button("Download Image"):
            output_image = Image.fromarray(transformed_image)
            output_image.save("modified_image.png")
            st.download_button("Download", "modified_image.png")
    else:
        st.write("No face detected. Please upload a clearer image.")
