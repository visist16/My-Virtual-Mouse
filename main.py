import cv2
import mediapipe as mp
import pyautogui
cap = cv2.VideoCaptur(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 0
while True:
  _, frame = cap.read()
  cv2.imshow('Virtual Mouse', frame)
  cv2.waitKey(1)
  
  

