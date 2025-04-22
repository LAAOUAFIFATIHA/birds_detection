# birds detection project
this project design to detect birds and scare tem away form famrers crops 
 # Bird Detection with Raspberry Pi

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Version](https://img.shields.io/badge/version-1.0.0-green.svg)

## Description

This project uses a Raspberry Pi to detect birds in real-time using a camera. The Raspberry Pi processes the camera feed with a pre-trained machine learning model to detect birds, and it plays a sound when a bird is detected in order to protect farms.

## Features

- Real-time bird detection using a Raspberry pi camera.
- Integration with Arduino for physical actions for primary test.
- Lightweight and efficient for edge devices like Raspberry Pi.
- Customizable detection threshold and actions.

## Hardware Requirements

- Raspberry Pi (with camera module)
- Arduino (Arduino Uno just for test you can use derectly Raspberry pi)

## Software Requirements

- Python 3.x
- OpenCV
- Arduino IDE
- `pyserial` library for Raspberry Pi-Arduino communication
- ultralytics for YOLO 

## Installation

### Raspberry Pi Setup

1. **Install dependencies**:
   ```bash
   sudo apt update
   sudo apt install python3-opencv python3-pip
   pip3 install tensorflow pyserial
   ```
2. **Create a new environment in Raspberry pi for libraries**:
   ```
   sudo apt install python3 python3-venv python3-pip
   python3 -m venv venv
   source venv/bin/activate
   pip install ultralytics
   pip install pygame 
   ```
4. **load the project in Raspberry pi**
   ```
  mkdir bird_detection
  cd bird_detection
  
  ```

6. **Test**

   
