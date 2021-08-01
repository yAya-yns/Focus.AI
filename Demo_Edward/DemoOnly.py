"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
from gaze_tracking import GazeTracking
import time

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
left_bound = 0.7
right_bound = 0.46
lower_bound = 0.81
upper_bound = 0.89
h_diff = left_bound - right_bound
v_diff = upper_bound - lower_bound

v_buffer = []
h_buffer = []

for i in range(10):
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
        continue
    v_buffer.append(vr)
    h_buffer.append(hr)
    v_arg = sum(v_buffer)/len(v_buffer)
    h_arg = sum(h_buffer)/len(h_buffer)
    # print(v_arg, h_arg)
    # box_center = [100, 100]
    box_center = [width * abs(h_arg - left_bound) / h_diff, height * abs(v_arg - upper_bound) / v_diff]
    print(box_center)
    top_left_corner = (int(box_center[0]) - 40, int(box_center[1]) - 40)
    lower_right_corner = (int(box_center[0]) + 40, int(box_center[1]) + 40)

    cv2.rectangle(frame, top_left_corner, lower_right_corner, (0, 255, 0), 2)

    v_buffer.pop(0)
    h_buffer.pop(0)

    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27:
        break

webcam.release()
cv2.destroyAllWindows()
