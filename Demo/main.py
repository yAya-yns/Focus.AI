"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
from gaze_tracking import GazeTracking
import time

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
left_list = []
right_list = []
lower_list = []
upper_list = []
left_bound = None
right_bound = None
lower_bound = None
upper_bound = None
h_diff = None
v_diff = None

time_init = time.time()
while True:
    _, frame = webcam.read()
    gaze.refresh(frame)
    frame = gaze.annotated_frame()
    text = "Please Gaze at the upper-left corner of your screen"
    hr = gaze.horizontal_ratio()
    vr = gaze.vertical_ratio()
    if hr is None or vr is None:
        continue
    left_list.append(hr)
    upper_list.append(vr)
    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
    cv2.imshow("Calibration", frame)
    time_curr = time.time()
    if cv2.waitKey(1) == 27:
        break
    if time_curr - time_init > 10:
        left_bound = sum(left_list)/len(left_list)
        upper_bound = sum(upper_list)/len(upper_list)
        break
#
# webcam.release()
cv2.destroyAllWindows()

print("calibrating upper and left finished")

time_init = time.time()
while True:
    _, frame = webcam.read()
    gaze.refresh(frame)
    frame = gaze.annotated_frame()
    text = "Please Gaze at the lower-right corner of your screen"
    hr = gaze.horizontal_ratio()
    vr = gaze.vertical_ratio()
    if hr is None or vr is None:
        continue
    right_list.append(hr)
    lower_list.append(vr)
    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
    cv2.imshow("Calibration", frame)
    time_curr = time.time()
    if cv2.waitKey(1) == 27:
        break
    if time_curr - time_init > 10:
        right_bound = sum(right_list)/len(right_list)
        lower_bound = sum(lower_list)/len(lower_list)
        h_diff = right_bound - left_bound
        v_diff = upper_bound - lower_bound
        break

# webcam.release()
cv2.destroyAllWindows()

print("calibrating lower and right finished")

print(left_bound, right_bound, upper_bound, lower_bound)

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
    box_center = [width * (h_arg - left_bound) / h_diff, height * (v_arg - upper_bound) / v_diff]
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
