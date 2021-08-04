import cv2

webcam = cv2.VideoCapture(0)
_, frame = webcam.read()
height = frame.shape[0]
width = frame.shape[1]
print(height, width)
