# README

## Overview

This project provides a deep learning service for recognizing handwritten digits using the MNIST dataset. The service leverages a pre-trained ResNet-18 model, which has been fine-tuned for MNIST digit classification. It includes:

- A trained model (`mnist_resnet.pth`).
- Utility scripts (`model.py`) for loading the model and performing predictions.
- Services built with FastAPI and Streamlit for deploying the model and providing a user interface.

---

## File Contents

### 1. `training_mnist_classification.ipynb`
- **Description**: Provide file for training model.
### 2. `app/model.py`

- **Description**: Provides functions to load the trained model and make predictions.
- **Key Functions**:
  - `load_model(model_path)`: Loads the ResNet-18 model and its weights from the specified path.
  - `predict(model, image)`: Processes an input image and predicts the digit class.

### 3. `app/mnist_resnet.pth`

- **Description**: Stores the weights of the trained ResNet-18 model.
- **Usage**: Used in `model.py` to load the pre-trained model.

### 4. `app/main.py`

- **Description**: Implements a FastAPI service for serving the model as an API.
- **Key Features**:
  - Endpoint for predicting digits from an uploaded image.

### 5. `streamlit_app/appapp.py`

- **Description**: Implements a Streamlit-based user interface for interacting with the model.
- **Key Features**:
  - Allows users to upload an image and view predictions.

### 6. `requirements.txt`

- **Description**: Lists all Python dependencies required for running the project.

---

### Running the Services

#### FastAPI Service

1. Start the FastAPI server:
   ```bash
   uvicorn app/main:app --host 0.0.0.0 --port 8000
   ```
2. Open your browser and visit `http://127.0.0.1:8000/docs` to interact with the API.

#### Streamlit Interface

1. Start the Streamlit app:
   ```bash
   streamlit run streamlit_app/app.py
   ```
2. Open your browser and visit the URL provided in the terminal (e.g., `http://127.0.0.1:8501`).

---

## Project Workflow

1. Use the pre-trained model (`mnist_resnet.pth`) for predictions via FastAPI or Streamlit.

2. Deploy the services for real-time usage:

   - FastAPI for API integration.
   - Streamlit for user-friendly visualization.

---

## Additional Notes

- Ensure you have a GPU setup for faster training and inference (optional).
- The model expects grayscale images resized to 224x224 pixels.
- For deployment, consider containerizing the application using Docker or deploying to cloud services.

---

## Contact

For questions or issues, feel free to contact leminhhung933@gmail.

