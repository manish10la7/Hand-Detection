# Hand Gesture Detection README

## Project Overview

This project implements a hand gesture recognition system using OpenCV in Python. It captures the hand's movements and detects specific gestures such as waving, pointing, and common gestures like rock, paper, and scissors. The system segments the hand from the background, tracks its movement, and counts the number of visible fingers to determine the gesture.

### Features:
- Hand segmentation using background subtraction
- Hand gesture recognition (waving, pointing, rock, scissors)
- Counting visible fingers
- Real-time camera input

## Requirements

Before running the project, you need to install the required libraries and dependencies.

### 1. **Python 3.x**
Ensure that you have Python 3.x installed on your machine. You can download it from the official website: [Python Downloads](https://www.python.org/downloads/).

### 2. **Python Libraries**

The project requires the following Python libraries:

- `numpy`: For handling numerical operations and arrays.
- `opencv-python` (`cv2`): For handling image processing and camera input.

### Install the required libraries using `pip`:

```bash
pip install numpy opencv-python or opencv-contrib-python 
```

### Library Breakdown:
- **NumPy**: Used for numerical operations and array manipulations, such as handling image matrices.
- **OpenCV**: Used for capturing video frames from the webcam, performing background subtraction, hand segmentation, and gesture recognition.

## Project Structure

The main components of the project are as follows:

1. **HandData Class**: A class used to store the position and state of the detected hand (top, bottom, left, right points, center of the palm, and whether the hand is waving).

2. **Main Functions**:
   - `write_on_image(frame)`: Writes the current gesture or status (e.g., "Calibrating...", "Waving") on the camera feed.
   - `get_region(frame)`: Extracts the region of interest (ROI) from the frame, prepares it for further processing by converting it to grayscale and applying Gaussian blur.
   - `get_average(region)`: Performs background averaging to create a background model.
   - `segment(region)`: Segments the hand from the background using background subtraction and contour detection.
   - `get_hand_data(thresholded_image, segmented_image)`: Extracts information about the hand, such as position and finger count, and updates the `HandData` object.
   - `count_fingers(thresholded_image)`: Counts the number of visible fingers based on the segmented hand.

3. **Main Program**:
   - Captures the video feed from the webcam.
   - Continuously processes each frame to segment the hand and detect gestures.
   - Displays the result on the screen with annotations about the detected gesture.

## How to Run

1. Ensure you have all the dependencies installed as mentioned above.
2. Run the program:

```bash
python Hand Detection(all code executable program).py
```

3. The program will open your webcam feed and start detecting hand gestures in real-time.

### Controls:

- The program will continuously analyze the region of interest and detect gestures.
- Press **'x'** to exit the program.

## Region of Interest (ROI)

- The system focuses on the top-right part of the frame to detect the hand. The user should move their hand into this region for detection.

## Customization

You can adjust the following parameters in the code to fine-tune the system based on your environment and needs:
- **Calibration Time** (`CALIBRATION_TIME`): Adjusts the number of frames to be used for background calibration.
- **Background Weight** (`BG_WEIGHT`): Determines how much the background model should adapt to changes.
- **Object Threshold** (`OBJ_THRESHOLD`): The threshold for differentiating the hand from the background.
- **Region of Interest**: The part of the frame that is being used for hand detection. This can be adjusted by modifying `region_top`, `region_bottom`, `region_left`, and `region_right`.



