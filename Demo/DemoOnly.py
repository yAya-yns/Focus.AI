import tkinter as tk
from tkinter import *
import cv2
from gaze_tracking import GazeTracking
import pyautogui

pyautogui.FAILSAFE

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
left_bound = 0.7198632140726614
right_bound = 0.5236326614565042
lower_bound = 0.7610776820079143
upper_bound = 0.922214460886336
h_diff = left_bound - right_bound
v_diff = upper_bound - lower_bound

v_buffer = []
h_buffer = []

root = tk.Tk()

def make_window(words):
    T = tk.Text(root, height=2, width=30)
    T.pack()
    T.insert(tk.END, words)
    tk.mainloop()

for i in range(15):
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
        cv2.putText(frame, "Outside", (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
        cv2.imshow("Demo", frame)
        if cv2.waitKey(1) == 27:
            break
        continue
    v_buffer.append(vr)
    h_buffer.append(hr)
    v_arg = sum(v_buffer)/len(v_buffer)
    h_arg = sum(h_buffer)/len(h_buffer)
    # print(v_arg, h_arg)
    box_center = [width * abs(h_arg - left_bound) / h_diff, height * abs(v_arg - lower_bound) / v_diff]
    pyautogui.moveTo(box_center[0], box_center[1])
    if box_center[0] < 700 and box_center[1] < 500:
        # root.destroy()
        # make_window("Youtube")
        cv2.putText(frame, "Camera", (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
    elif box_center[0] < 700 and box_center[1] > 500:
        cv2.putText(frame, "YouTube", (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (0, 0, 255), 2)
    elif box_center[0] > 700:
        cv2.putText(frame, "Paper", (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
    # print(box_center)
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
