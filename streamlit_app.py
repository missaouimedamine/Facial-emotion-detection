import streamlit as st
import cv2
import numpy as np
from streamlit_webrtc import webrtc_streamer

def main():
    st.title("Live Camera Stream")
    st.write("This app opens your camera and displays the video feed.")
    
    # Start the webcam stream
    webrtc_streamer(key="camera")

if __name__ == "__main__":
    main()
