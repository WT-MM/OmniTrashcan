from modules.Motors import PWMControl
from modules.OmniDrive import OmniDrive
from modules.Detection import *
import cv2

dt = OmniDrive(PWMControl([1,2,3]),
               PWMControl([1,2,3]),
               PWMControl([1,2,3]))

translation = []
rotation = 0

cap = cv2.VideoCapture(0) #Figure out
while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Empty camera frame")
        continue
    
    
    updateMotors()
    
    k = cv2.waitKey(10)
    if(k == ord('esc')):
        break



def updateMotors():
    global translation, rotation
    dt.drive(translation, rotation)
    translation = [0,0]
    rotation = 0