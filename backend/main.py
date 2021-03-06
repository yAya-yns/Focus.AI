"""
This is the main application
"""
import cv2
from gaze_tracking import GazeTracking
from datetime import datetime, timedelta
from tabulate import tabulate

import time

timeout = 25*60   # [seconds]

timeout_start = time.time()

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
distract_time = 0
focus_time_period = 0
distract_time_period = 0
temp_time = timeout_start
while time.time() < timeout_start + timeout:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""

    if gaze.is_blinking():
        text = "Blinking"
    elif gaze.is_right():
        text = "Looking right"
    elif gaze.is_left():
        text = "Looking left"
    elif gaze.is_top():
        text = "Looking Up"
    elif gaze.is_bottom():
        text = "Looking bottom"
    else:
        distract_time += 1
    if distract_time == 0 and temp_time - 60 == time.time():
        focus_time_period += 1

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.8, (44, 87,
                                                                      166), 2)
    if distract_time > 5:
        distract_time = 0
        start = datetime.now()
        cpt = 0
        cv2.putText(frame, "please focus on your screen", (120, 120),
                    cv2.FONT_HERSHEY_DUPLEX, 1.8, (230, 204, 29), 2)
        cv2.imshow("Demo", frame)
        cv2.waitKey(600)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130),
                cv2.FONT_HERSHEY_DUPLEX, 1.2, (44, 87, 166), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165),
                cv2.FONT_HERSHEY_DUPLEX, 1.2, (44, 87, 166), 1)

    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27:
        break

webcam.release()
cv2.destroyAllWindows()

distract_time_period = 25*60 - focus_time_period

