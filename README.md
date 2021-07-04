# Yawning-Detection-System

In order to predict Driver's Drowsiness, yawning can be considered as a preety good factor. Yawning indicates the early stage of Drowsiness. if someone is yawning it shows that the person is going into sleepy state. if a system can detect yawning in realtime then it can  alert the driver before going into sleepy state and can save the driver from an accident.

In order to detect yawning, the system needs to detect the face first and then extract the mouth region from it. Finally the extracted mouth region will be passed to trained model in order to detect wether there is yawn or not. 

For face detection, DLIB's frontal face detector is used and then with help of Dlib's facial landmark detector the mouth region is extracted.

(1) Mouth Region Detection module is created to extract mouth region.
