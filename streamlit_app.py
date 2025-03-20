import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("Upload Image for Processing")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Convert uploaded file to OpenCV format
    image = Image.open(uploaded_file)
    image = np.array(image)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # Display original and processed images
    st.image(image, caption="Original Image", use_column_width=True)
    st.image(gray, caption="Grayscale Image", use_column_width=True)
