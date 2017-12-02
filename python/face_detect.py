# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 11:45:58 2017

@author: jaydeep thik
"""

import numpy as np
import cv2
import os



cam = cv2.VideoCapture(0)
face_cas = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

# declare the type of font to be used on output window
font = cv2.FONT_HERSHEY_SIMPLEX

f_01 = np.load('face_01.npy').reshape((20, 50*50*3)) 
f_02 = np.load('face_02.npy').reshape((20, 50*50*3))	
f_03 = np.load('face_03.npy').reshape((20, 50*50*3))

print(f_01.shape, f_02.shape, f_03.shape)

names = {0:'jaydeep',
         1:'shivam',
         2:'nirav',}

labels = np.zeros((60, 1))
labels[:20, :] = 0.0	
labels[20:40, :] = 1.0
labels[40:, :] = 2.0

data  = np.concatenate([f_01, f_02, f_03])

def distance(x1, x2):
    return np.sqrt(((x1-x2)**2).sum())

def knn(x, train, targets, k=5):
    m = train.shape[0]
    dist = []
    for ix in range(m):
        # compute distance from each point and store in dist
        dist.append(distance(x, train[ix]))
    dist = np.asarray(dist)
    indx = np.argsort(dist)
    sorted_labels = labels[indx][:k]
    #print(sorted_labels)
    counts = np.unique(sorted_labels, return_counts=True)
    return counts[0][np.argmax(counts[1])], np.max(counts[1])/k







while(True):
    
    ret, frame = cam.read() 
      
    if ret==True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cas.detectMultiScale(gray, 1.3, 5)
        
        for (x, y, w, h) in faces:
            face_component = frame[y:y+h, x:x+w, :]
            
            fc = cv2.resize(face_component, (50, 50))
            
            lab, tot =knn(fc.flatten(), data, labels)
            #lab, tot =log_pred(fc.flatten())
            text = names[int(lab)]
            
            cv2.putText(frame, text+ str(tot*100)+'%', (x,y), font ,1, (255,255,255), 2)
            
            cv2.rectangle(frame, (x, y),(x+w, y+h), (0,0,255), 2)
            
        cv2.imshow('face recognition', frame)
        
        if cv2.waitKey(1)==27:
            break
    else:
        print('error')
        
cam.release()
cv2.destroyAllWindows()

