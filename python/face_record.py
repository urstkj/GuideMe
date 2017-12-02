# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 11:17:07 2017

@author: jaydeep thik
"""

import numpy as np
import cv2 

def capture(frame, iid):
    print("Saving")
    path = "C:\wamp64\www\guideme\images\guideimages\\"
    #path = "D:\\"
    full = path + 'face_' + str(iid) + '.png'
    print(full)
    cv2.imwrite(full, frame)

def record(iid):
    cam = cv2.VideoCapture(0)
    face_cas=cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
    
    #placeholder for storing data
    data = []
    ix =0
    
    while True:
        ret, frame = cam.read()
        
        
        if ret:
            #convert current frame to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            faces = face_cas.detectMultiScale(gray, 1.3, 5)
            
            #for each faces in the frame do
            for(x,y,w,h) in faces:
                face_component = frame[y:y+h, x:x+w,:]
                fc = cv2.resize(face_component, (50, 50))
                
                if  ix%10==0 and len(data) <20:
                    data.append(fc)
                    
                #display rect around face
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
            ix+=1
            cv2.imshow('frame', frame)
            
            if cv2.waitKey(1)==27 or len(data)>=20:
                ret, frame = cam.read()
                capture(frame,iid)
                break
        else:
            print('error')
            break
        
        
    cam.release()
    cv2.destroyAllWindows()
    
    data = np.asarray(data)
    print(data.shape)
    np.save('face_'+str(iid), data)            