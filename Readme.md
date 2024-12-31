# 🅿️arking Space Detection 🚗

https://github.com/user-attachments/assets/efab3cb9-4d0f-49b5-9c56-11cc1d92c077

This project is a Parking Space Detection system that uses a machine learning model to identify whether parking spaces are occupied or empty in real-time. It involves:
- A trained CNN model based on the VGG16 architecture.
- Flask backend to serve the model and stream video.
- OpenCV for image processing.

---

## Features
- Detects parking spaces as **Empty** or **Full**.
- Streams video with overlaid parking space statuses.
- Provides endpoints for real-time parking space counts.

---

## Prerequisites
1. Python 3.7+
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate # For Linux/Mac
   venv\Scripts\activate # For Windows
   ```
4. Install TensorFlow, Keras, Flask, and OpenCV.

---

## Files Description

### 1. **assets/**
- Contains test video and sample images.

### 2. **data/**
- Contains `train` and `test` directories with images for model training.

### 3. **main.py**
- Entry point for the Flask application.
- Includes routes for:
  - Video streaming: `/video_feed`
  - Parking space count: `/space_count`

### 4. **train/train.py**
- Script to train the CNN model using VGG16 architecture.

---

## How to Run

### Step 1: Train the Model (Optional)
1. Add training and test images to `data/train` and `data/test` directories.
2. Run the training script:
   ```bash
   python train/train.py
   ```
3. The trained model will be saved as `model/model_final.h5`.

### Step 2: Run the Flask Application
1. Ensure the `model/model_final.h5` and `model/carposition.pkl` files are in place.
2. Start the Flask server:
   ```bash
   python main.py
   ```
3. Open your browser and navigate to `http://127.0.0.1:5000/`.

---

## Flask Endpoints
1. **Home**
   - `http://127.0.0.1:5000/`
   - Displays the live video feed with parking space detection.

2. **Video Feed**
   - `http://127.0.0.1:5000/video_feed`
   - Streams the video with detection.

3. **Space Count**
   - `http://127.0.0.1:5000/space_count`
   - Returns the number of free and occupied parking spaces as JSON.

---

## Key Parameters
- **Image Dimensions**: `48x48`
- **Model Architecture**: VGG16
- **Classes**: `Empty`, `Full`
- **Learning Rate**: `0.0001`
- **Batch Size**: `32`
- **Epochs**: `15`

---

## Libraries Used
1. Flask
2. OpenCV
3. TensorFlow/Keras
4. NumPy
5. Pickle

---

## Future Improvements
- Add a web-based dashboard for better visualization.
- Improve detection accuracy with more training data.
- Implement a notification system for parking updates.

---

## License
This project is licensed under the MIT License.
