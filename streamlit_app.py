import streamlit as st
import cv2
import numpy as np

# Streamlit title
st.title("Live Camera Feed with Streamlit")

# Start video capture
cap = cv2.VideoCapture(0)

# Check if the webcam is opened
if not cap.isOpened():
    st.error("Error: Could not access the webcam.")
else:
    st.write("Webcam is active. Click 'Capture' to take a picture.")

# Display webcam feed
frame_placeholder = st.empty()

while True:
    ret, frame = cap.read()
    if not ret:
        st.error("Failed to capture image.")
        break

    # Convert frame to RGB for Streamlit
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Display the frame
    frame_placeholder.image(frame, channels="RGB", use_column_width=True)

    # Stop the loop when user closes the app
    if st.button("Stop Camera"):
        break

# Release the camera
cap.release()
st.write("Camera feed stopped.")
