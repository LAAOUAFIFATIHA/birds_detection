import cv2
import datetime
import os
from ultralytics import YOLO
import pygame
import random
import conArduino

# Loading pretrained YOLO model (will be downloaded on first run)
model = YOLO("model/yolov8n.pt", "v8")

# Set dimensions of screen frames
frame_width = 1280
frame_height = 720

# Open the camera
cap = cv2.VideoCapture(0)

# Only save an image on frame 0
frame_count = 0

# Ensure pygame mixer is initialized only once
pygame.mixer.init()

# List of sound files
sound_files = [
    # "source/bird_detected.mp3",
    "source/attention.wav",
    # "source/terror.wav"
]

# Preload sound files (optional)
sounds = [pygame.mixer.Sound(file) for file in sound_files]

# Ensure the 'images' folder exists
if not os.path.exists("images"):
    os.makedirs("images")

if not cap.isOpened():
    print("Cannot open video stream for the camera... ")
    exit()

while True:
    # the ret a boolean that indicate if the camera linked 
    ret, frame = cap.read()

    if not ret:
        print("Camera not linked ... ")
        break
    
    # Resize the frame
    frame = cv2.resize(frame, (frame_width, frame_height))

    # Do prediction on image, with confidence greater than 80%
    detect_params = model.predict(source=[frame], conf=0.8, save=False)

    # Process detections
    if len(detect_params[0]) != 0:
        for i in range(len(detect_params[0])):

            boxes = detect_params[0].boxes
            box = boxes[i]
            clsID = box.cls.numpy()[0]
            conf = box.conf.numpy()[0]
            bb = box.xyxy.numpy()[0]
            c = box.cls
            # Name of object detected (e.g. 'bird')
            class_name = model.names[int(c)]

            # If the class name contains the word 'bird'
            if 'bird' in class_name.lower():
                

                # Save image at frame_count == 0
                if frame_count == 0:
                    current_time = datetime.datetime.now()
                    filename = os.path.join("images", current_time.strftime("bird_%Y-%m-%d_%H-%M-%S-%f.jpg"))
                    success = cv2.imwrite(filename, frame)

                if frame_count == 10:
                    frame_count = 0
                else:
                    frame_count += 1
                
                print("Bird detected")
                # conArduino.conARD()  # Play sound or activate the buzzer

                # Play a random sound
                random_sound = random.choice(sounds)
                random_sound.play()

                # Draw green rectangle around the object
                cv2.rectangle(
                    frame,
                    (int(bb[0]), int(bb[1])),
                    (int(bb[2]), int(bb[3])),
                    (0, 255, 0),
                    3,
                )
                # Add some text labelling to the rectangle
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(
                    frame,
                    class_name + " " + str(round(conf, 3)) + "%",
                    (int(bb[0]), int(bb[1]) - 10),
                    font,
                    1,
                    (255, 255, 255),
                    2,
                )

    # Display the frame onscreen
    cv2.imshow("Object Detection", frame)

    # End program when q is pressed
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()













































# import cv2
# import datetime
# import os
# from ultralytics import YOLO
# import pygame
# import random
# import conArduino

# # Loading pretrained YOLO model (will be downloaded on first run)
# model = YOLO("model/yolov8n.pt", "v8")

# # Set dimensions of screen frames
# frame_width = 1280
# frame_height = 720

# # open and take the data from camera 
# cap = cv2.VideoCapture(0)

# # Only save an image on frame 0
# frame_count = 0

# if not cap.isOpened():
#     print("Cannot open video stream for the camera... ")
#     exit()

# while True:
#     # the ret a boolean that indicate if the camera linked 
#     ret, frame = cap.read()

#     if not ret:
#         print("No the camera does not linked ... ")
#         break
    
#     # Resize the screen
#     frame = cv2.resize(frame, (frame_width, frame_height))

#     # Do prediction on image, with confidence greater than 80%
#     detect_params = model.predict(source=[frame], conf=0.8, save=False)

#     DP = detect_params[0].numpy()

#     # List of sound files
#     sound_files = [
#         "source/bird_detected.mp3",
#         "source/attention.wav",
#         "source/terror.wav"
#     ]

#     if len(DP) != 0:
#         for i in range(len(detect_params[0])):

#             boxes = detect_params[0].boxes
#             box = boxes[i]
#             clsID = box.cls.numpy()[0]
#             conf = box.conf.numpy()[0]
#             bb = box.xyxy.numpy()[0]
#             c = box.cls
#             # Name of object detected (e.g. 'bird')
#             class_name = model.names[int(c)]

#         # If the class name contains the word 'bird'
#         if 'bird' in class_name.lower():
#             # play the sound of the buzzer 
#             for i in class_name.lower():
#                 if 'bird' in class_name.lower():
#                     conArduino.conARD()

#             ## SD FORMATOR 
#             ## raspberry loader 
#             ## tele image raspbe 


#             print("bird detected")
#             ## 
           

#             # choose randomlly the sound 
#             # random_sound_file = random.choice(sound_files)
#             # print("HHHHHHHHHH",random_sound_file)

#             # to play the sound
#             # Initialize pygame mixer
#             pygame.mixer.init()
           

#             # Load the sound file (ensure the path is correct)
#             sound = pygame.mixer.Sound(random_sound_file)

            
#             # sound.play()


#             if frame_count == 0:
#                 current_time = datetime.datetime.now()
#                 filename = os.path.join("images", current_time.strftime("bird_%Y-%m-%d_%H-%M-%S-%f.jpg"))
#                 success = cv2.imwrite(filename, frame)

#             if frame_count == 10:
#                 frame_count = 0
#             else:
#                 frame_count += 1

#             # Draw green rectangle around the object
#             cv2.rectangle(
#                 frame,
#                 (int(bb[0]), int(bb[1])),
#                 (int(bb[2]), int(bb[3])),
#                 (0, 255, 0),
#                 3,
#             )
#             # Add some text labelling to the rectangle
#             font = cv2.FONT_HERSHEY_SIMPLEX
#             cv2.putText(
#                 frame,
#                 class_name + " " + str(round(conf, 3)) + "%",
#                 (int(bb[0]), int(bb[1]) - 10),
#                 font,
#                 1,
#                 (255,255,255),
#                 2,
#             )
        
#             # Keep the program running to allow the sound to finish
#             #pygame.time.wait(int(sound.get_length()))


#     # Display the frame onscreen
#     cv2.imshow("Object Detection", frame)

#     # End program when q is pressed
#     if cv2.waitKey(1) == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

