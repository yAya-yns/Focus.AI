# Focus.AI 
## **1. Overall**<br/>
This webcam-based eye tracking system based on the python library **NumPy**, **OpenCV** and **Dlib**. It gives you the exact position of the pupils direction and the location where the eyes focus on.<br/>
<br/>
## **2. Install Dependency**<br/>
`< pip install -r dependency.txt >`<br/>
## **3. The basic direction idea** <br/>
We compute the number between 0.0 and 1.0 that indicates the horizontal/vertical direction of the gaze. The extreme right is 0.0, the center is 0.5 and the extreme left is 1.0. <br/>
`gaze.horizontal_ratio()` `gaze.vertical_ratio()` <br/>
## **4.The Specific Algorithm**<br/>
`pupil_left = self.eye_left.pupil.x / (self.eye_left.center[0] * 2 - 10)` <br/>
`pupil_right = self.eye_right.pupil.x / (self.eye_right.center[0] * 2 - 10)` <br/>
`(pupil_left + pupil_right) / 2` <br/>
## **5.Run the main function**<br/>
`python3 main.py` <br/>
![alt text](http://url/to/img.png)
