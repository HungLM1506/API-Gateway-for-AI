import streamlit as st
import requests
from PIL import Image

st.title("MNIST Digit Recognition")
st.write("Upload an image of a handwritten digit, and the model will predict it.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # Hiển thị ảnh đã tải lên
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Gửi request đến FastAPI backend
    if st.button("Predict"):
        with st.spinner("Predicting..."):
            response = requests.post(
                "http://localhost:8000/predict/",
                files={"file": uploaded_file.getvalue()},
            )
            if response.status_code == 200:
                st.success(f"Predicted digit: {response.json()['digit']}")
            else:
                st.error(f"Error: {response.json()['error']}")
