"""
camera detection haar
1. create harr detection instance
2. get video stream
3. detect face on each frame
4. draw bbox
"""

# imports:
import cv2
import numpy as np

capture = cv2.VideoCapture(0)

detector = cv2.CascadeClassifier('./face_detection/haarcascades/haarcascade_frontalface_default.xml')

while True:
    ret,frame = capture.read()

    # Flip capture
    frame = cv2.flip(frame,1)
    
    # Need grey scale image for detection
    gray_img = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)

    # detect face
    detection = detector.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=10)
    
    # Draw bbox on image
    for (x,y,w,h) in detection:
        #draw bbox on img
        cv2.rectangle(frame, (x,y), (x+w,y+h),(0,0,255),5)
    
    # Show capture 
    cv2.imshow('haar', frame)

    # Add exit condiction
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
 