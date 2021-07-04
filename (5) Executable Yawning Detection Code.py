import cv2 
import dlib
hog_face_detector = dlib.get_frontal_face_detector()
dlib_facelandmark = dlib.shape_predictor("C:\\Users\\Sanjay Dhundwal\\Yawning Detection\\shape_predictor_68_face_landmarks.dat")
import tensorflow as tf
from keras.models import load_model
model = tf.keras.models.load_model("C:\\Users\\Sanjay Dhundwal\\Yawning Detection\\Models\\cnn_from_scratch.h5")
from keras.preprocessing import image
import numpy as np

frame = cv2.VideoCapture(1)


print('frame capturing initiated')

def transform(roi):
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    IMG_SIZ=224
    roi= cv2.resize(roi,(IMG_SIZ,IMG_SIZ),3)    
    return roi
count=0



while True:
    ret, img = frame.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = hog_face_detector(gray)
    for face in faces:
        x1=face.left()
        y1=face.top()
        x2=face.right()
        y2=face.bottom()
        face_img=cv2.rectangle(img, (x1,y1), (x2,y2),(0,255,0),2)
        roi_color = face_img[y1:y2, x1:x2]
        face_landmarks = dlib_facelandmark(gray, face)
        
        X1=face_landmarks.part(48).x
        Y1=face_landmarks.part(33).y
        X2=face_landmarks.part(54).x
        Y2=face_landmarks.part(57).y
        
      
      
        roi = face_img[Y1:Y2, X1:X2]
        roi=transform(roi)
        font=cv2.FONT_HERSHEY_SIMPLEX
        
        
        test_image = roi 
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        
        result = model.predict(test_image)
        
        if result[0][0]==1:
            prediction="Yawning"
            count += 1
            if count > 8:
                cv2.putText(img,'yawning',(x1,y1),font,1,(0,0,255),2,cv2.LINE_AA)
               
                
        else:
            prediction="Not Yawning"
            count=1
       
        
                
        cv2.namedWindow('image',cv2.WINDOW_NORMAL)
        cv2.resizeWindow('image', 1100,700)
        cv2.imshow('image',img) 
        
    if cv2.waitKey(1)& 0xff==ord('x'):
  
        break

frame.release()
cv2.destroyAllWindows()
