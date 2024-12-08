**Wild Boar Detection**

This project utilizes YOLOv5 for real-time object detection on video files. It is designed to analyze videos, detect objects using a custom-trained YOLOv5 model, and display the results in a Tkinter-based GUI. The application allows users to select a video and a model weight file, and it will process the video, displaying the results in real-time.

**Features**
- Real-time object detection using YOLOv5
- GUI interface built with Tkinter
- Select video and model weight files using file dialogs
- Displays detection results in real-time on video frames
- Supports custom-trained YOLOv5 models (.pt files)

**Requirements**
- Python 3.x
- PyTorch (with CUDA support if using GPU)
- OpenCV
- PIL (Pillow)
- Tkinter

**Install Dependencies**
You can install the required dependencies using pip:

pip install torch opencv-python pillow tk

**Installation**

1. Clone the repository:
   git clone https://github.com/ryeoryang/test.git
   cd test

2. Install the dependencies as mentioned above.

3. **Download YOLOv5 Model Weights**:
   - Download your custom-trained YOLOv5 model weights file (best.pt), which was trained to detect wild boars.
   - **Place the best.pt file in the following directory**:
     yolov5/runs/train/
   - Alternatively, you can specify the path to the weights file when prompted in the GUI.

**Usage**

1. **Run the Application**:
   To run the application, simply execute the script:
   python detect_video.py
   This will open a GUI window.

2. **Select Video and Weights File**:
   - Click the "Browse" button next to the "Video File" field to select the video file you want to analyze.
   - Click the "Browse" button next to the "Weights File" field to select the YOLOv5 model weights file (best.pt) that you want to use.

3. **Run Detection**:
   - After selecting the video and weights file, click the "Run Detection" button.
   - The program will start processing the video, displaying the detection results in real-time.
   - The video will be shown in the GUI, and bounding boxes, class labels, and confidence scores will be overlayed on the video frames.

4. **Exit**:
   - Once the detection is complete, the program will notify you with a message box saying "Detection completed!"

**Code Explanation**
The code is a simple Tkinter-based GUI application that allows the user to:
- Select a video file and a YOLOv5 weights file using file dialogs.
- Load the YOLOv5 model, process the video, and display the detection results.

**Key Functions:**
- select_video(): Opens a file dialog for the user to select a video file.
- select_weights(): Opens a file dialog for the user to select a YOLOv5 model weights file (.pt).
- run_detection(): Loads the YOLOv5 model, processes the video, and displays the detection results.

**GUI Elements:**
- Video File: The user selects the video to analyze.
- Weights File: The user selects the custom YOLOv5 model weights file.
- Run Detection Button: Starts the detection process on the selected video.

**Example**
To run the application:
python detect_video.py
- Select a video (e.g., wild_boar_video.mp4).
- Select the YOLOv5 model weights (e.g., best.pt).
- Click Run Detection to start analyzing the video.

**Troubleshooting**
- Model Loading Error: Ensure that the path to your weights file (.pt) is correct and that it is placed in the yolov5/runs/train/ directory.
- Missing Dependencies: If you encounter missing package errors, make sure to install all the required dependencies.
- Video Display Issues: If the video does not display properly in the Tkinter window, try resizing the window or adjusting the video frame size.

**License**
This project is licensed under the MIT License.
