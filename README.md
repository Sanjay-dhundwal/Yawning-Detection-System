# Yawning-Detection-System

In order to predict Driver's Drowsiness, yawning can be considered as a preety good factor. Yawning indicates the early stage of Drowsiness. if someone is yawning it shows that the person is going into sleepy state. if a system can detect yawning in realtime then it can  alert the driver before going into sleepy state and can save the driver from an accident.

In order to detect yawning, the system needs to detect the face first and then extract the mouth region from it. Finally the extracted mouth region will be passed to trained model in order to detect wether there is yawn or not. 

For face detection, DLIB's frontal face detector is used and then with help of Dlib's facial landmark detector the mouth region is extracted.

(1) Mouth Region Detection module is created to extract mouth region.

(2) Data Preprocessing module is created to pre-process the data before training process. Like in machine learning the data preprocessing is also important in Deep Learning. If we pass a good preprocessed data for training the model, obviously the model will be trained good and accuracy will also increase. So, here in data preprocessing we have genrated a code which will crop the images of dataset and produce a new image dataset containing only mouth region images.

TRAINING Part: As yawning is not a regular event so, very few datasets are availabel on yawn. I have taken the dataset from Kaggel(https://www.kaggle.com/serenaraju/yawn-eye-dataset-new) and produced new dataset using Data preprocessing module. 
Finally created two modles: 
                            (3) CNN from scratch 
                            (4) VGG16 (pretrained on Imagenet data set) using transfer learing technique.

After training these models on our final processed dataset , Models are saved as .h5 file.

(5) Executable yawning detection code module contains the code for real time Yawning detection.  
     > First the video frames are taken from live cam footage using OpenCV.
     
     > Then these frames are passed to the trained model for yawning detection.
     
     > If yawning found for some continous frames, then with help of opencv "Yawning" is printed on the screen
