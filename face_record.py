# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 11:06:08 2017

@author: jaydeep thik
"""

import numpy as np
import cv2 

def capture(frame, iid):
    print("Saving")
    
    cv2.imwrite('png/face_'+str(iid)+'.png', frame)

def record(iid):#iid = randomly genereated id given to the function
    cam = cv2.VideoCapture(0)
    face_cas=cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
    
    #placeholder for storing data
    data = []
    ix =0
    
    while True:
        ret, frame = cam.read()
        
        
        if ret == True:
            #convert current frame to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray=cv2.equalizeHist(gray)
            
            faces = face_cas.detectMultiScale(gray, 1.1, 5)
            
            #for each faces in the frame do
            for(x,y,w,h) in faces:
                face_component = gray[y:y+h, x:x+w]
                fc = cv2.resize(face_component, (100, 100))
                
                if  ix%10==0 and len(data) <20:
                    if len(data)==10:
                        print_face = frame[y-80:y+h+30, x-30:x+w+30]
                        capture(print_face, iid)
                    data.append(np.array(fc))
                    cv2.imshow('frames', face_component)
                    
                #display rect around face
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
            ix+=1
            cv2.imshow('frame', frame)
            
            if cv2.waitKey(1)==27 or len(data)>=20:
                break
        else:
            print('error')
            break
        
        
    cam.release()
    cv2.destroyAllWindows()
    
    #data = np.asarray(data)
    
    np.save('npy/face_'+str(iid), data)

if __name__ == '__main__':
    record(17)