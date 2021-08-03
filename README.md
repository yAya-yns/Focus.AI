# Focus.AI 
## **1. Overall**<br/>
This webcam-based eye tracking system based on the python library **NumPy**, **OpenCV** and **Dlib**. It gives you the exact position of the pupils direction and the location where the eyes focus on.<br/>
<br/>
## **2. Install Dependency**<br/>
`< pip install -r dependency.txt >`<br/>
## **The basic direction idea** <br/>
We compute the number between 0.0 and 1.0 that indicates the horizontal/vertical direction of the gaze. The extreme right is 0.0, the center is 0.5 and the extreme left is 1.0. <br/>
`ratio = gaze.horizontal_ratio()` `ratio = gaze.vertical_ratio()` <br/>
