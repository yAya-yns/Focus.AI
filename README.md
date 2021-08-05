# Focus.AI 

## **Description**<br/>
Focus.AI is a web app designed to help users improve productivity. It tracks the user's focus through gaze, which informs the user when and how they are distracted during work. It also integrates with the pomodoro technique to help users achieve better focus. <br/>

## **Install Dependency**<br/>
`pip install -r dependency.txt`<br/>

## **Run**<br/>
```
conda create focus
conda activate focus
python3 main.py
``` 


## **Gaze Tracking Algorithm**<br/>
The webcam-based eye tracking system is able to track the user's gaze as they move their eyes. The program is based on the python library **NumPy**, **OpenCV** and **Dlib**. It gives you the exact position of the pupils direction and the location where the eyes focus on.<br/>
To get the basic direction, we compute the number between 0.0 and 1.0 that indicates the horizontal/vertical direction of the gaze. The extreme right is 0.0, the center is 0.5 and the extreme left is 1.0. <br/>
`gaze.horizontal_ratio()` `gaze.vertical_ratio()` <br/>

```
pupil_left = self.eye_left.pupil.x / (self.eye_left.center[0] * 2 - 10) 
pupil_right = self.eye_right.pupil.x / (self.eye_right.center[0] * 2 - 10)
(pupil_left + pupil_right) / 2
```
![](backend/images/gaze.png) <br/>
![](backend/images/eye.png) <br/>


## **Preview**<br/>
  * **Start work with Pomodoro timer**<br/>
  ![](backend/images/pomodoro.png) <br/>
  * **Finish work to view report**<br/>
  ![](backend/images/report-display.png) <br/>

## Product Video <br/>
https://user-images.githubusercontent.com/55170389/128225057-88c2d486-2f36-4cfe-a428-031d33714c36.mp4


## Reference <br/>
**Dataset** <br/>
>  `shape_predictor_68_face_landmarks.dat` <br/>
> The total number of individual identities in the dataset is *7485* <br/>
> The resulting model obtains a mean error of *0.993833* with a standard deviation of *0.00272732* on the LFW benchmark

