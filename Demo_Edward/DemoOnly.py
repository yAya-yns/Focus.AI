"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
from gaze_tracking import GazeTracking
import pyautogui
pyautogui.FAILSAFE
import time
# 0.7198632140726614 0.5236326614565042 0.7610776820079143 0.922214460886336
gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
left_bound = 7198632140726614
right_bound = 5236326614565042
lower_bound = 0.7610776820079143
upper_bound = 0.922214460886336
h_diff = left_bound - right_bound
v_diff = upper_bound - lower_bound

v_buffer = []
h_buffer = []

for i in range(20):
    _, frame = webcam.read()
    height = frame.shape[0]
    width = frame.shape[1]
    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)
    frame = gaze.annotated_frame()

    hr = gaze.horizontal_ratio()
    vr = gaze.vertical_ratio()
    if hr is None or vr is None:
        i = i - 1
        continue
    v_buffer.append(vr)
    h_buffer.append(hr)

# print(h_buffer, v_buffer)

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()
    height = frame.shape[0]
    width = frame.shape[1]
    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)
    frame = gaze.annotated_frame()

    hr = gaze.horizontal_ratio()
    vr = gaze.vertical_ratio()
    if hr is None or vr is None:
        cv2.imshow("Demo", frame)
        continue
    v_buffer.append(vr)
    h_buffer.append(hr)
    v_arg = sum(v_buffer)/len(v_buffer)
    h_arg = sum(h_buffer)/len(h_buffer)
    # print(v_arg, h_arg)
    # box_center = [100, 100]
    box_center = [width * abs(h_arg - left_bound) / h_diff, height * abs(v_arg - lower_bound) / v_diff]
    pyautogui.moveTo(box_center[0], box_center[1])
    print(box_center)
    # top_left_corner = (int(box_center[0]) - 40, int(box_center[1]) - 40)
    # lower_right_corner = (int(box_center[0]) + 40, int(box_center[1]) + 40)

    # cv2.rectangle(frame, top_left_corner, lower_right_corner, (255, 0, 0), 2)

    v_buffer.pop(0)
    h_buffer.pop(0)

    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27:
        break

webcam.release()
cv2.destroyAllWindows()
