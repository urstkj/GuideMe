# -*- coding: utf-8 -*-

import numpy as np
import cv2
import os

class FaceDetect:
    def __init__(self, filename):
        self.filename = filename

    def detect(self):
        f_ = []

        l = 0
        ll = len([name for name in os.listdir('npy')])

        labels = []
        for labelname in os.listdir("npy"):
            f_.append(np.load('npy/' + labelname))

            for it in range(20):
                ttt = labelname.split('.')[0].split('_')[1]
                #print(ttt)
                labels.append(int(ttt))
            l += 1

        face_cas = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

        # declare the type of font to be used on output window
        font = cv2.FONT_HERSHEY_SIMPLEX

        # the complete data required for image processing
        data = np.concatenate(f_)

        # new recognizer using LBPHFacerecognizer
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.train(data, np.array(labels))

        # input image "here"
        frame = cv2.imread(self.filename)

        # preprocessing and rescaling
        detection_width = 320
        scale = frame.shape[1] / float(detection_width)

        if (frame.shape[1] > detection_width):
            scaleHeight = round(frame.shape[0] / scale)
            frame = cv2.resize(frame, (detection_width, scaleHeight))

        # rescaling finished
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # equalize the brightmess and contrast
        gray = cv2.equalizeHist(gray)
        # gray = cv2.bilateralFilter(gray, 0,20.0,2.0)
        # cv2.imshow('gray',gray)
        faces = face_cas.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            face_component = gray[y:y + h, x:x + w]
            fc = cv2.resize(face_component, (100, 100))
            # cv2.imshow('face', fc)
            pred, conf = recognizer.predict(fc)  # predicted (pred) and the confidence(conf) value of the input

            text = str(pred)
            # pred is the id returned after matching

            print(text + "   " + str(conf))

            if conf <= 99:  # threshold
                return text
                #cv2.putText(frame, text, (x, y), font, 1, (0, 225, 0), 2)
                #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            else:
                print("UNKNOWN")  # rerurn -1 for an unknown face here, uncomment the line below
                #print "unknown"

        if len(faces) == 0:
            #print("no face detected click again")  # return 0 if no faces were found and promt to take a new photo
            return "zero"

        cv2.imshow('face recognition', frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == '__main__':
    a = FaceDetect("new_face_15.png")
    a.detect()