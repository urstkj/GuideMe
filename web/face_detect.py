# -*- coding: utf-8 -*-
import numpy as np
import cv2
import os

class FaceDetect:
    def __init__(self, filename):
        self.filename = filename

    def distance(self, x1, x2):
        return np.sqrt(((x1 - x2) ** 2).sum())

    def knn(self, x, train, targets, k=3):
        m = train.shape[0]
        dist = []
        for ix in range(m):
            # compute distance from each point and store in dist
            dist.append(self.distance(x, train[ix]))
        dist = np.asarray(dist)
        indx = np.argsort(dist)
        sorted_labels = targets[indx][:k]
        # print(sorted_labels)
        counts = np.unique(sorted_labels, return_counts=True)
        return counts[0][np.argmax(counts[1])], np.max(counts[1]) / k

    def detect(self):
        f_ = []
        l = 0
        ll = len([name for name in os.listdir('npy')])
        labels = np.zeros((20 * ll, 1))

        for labelname in os.listdir("npy"):
            f_.append(np.load("npy/" + labelname).reshape((20, 50 * 50 * 3)))
            labels[20 * l:20 * (l + 1), :] = int(labelname.split('.')[0].split('_')[1])
            l += 1
            print(labelname)

        face_cas = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

        data = np.concatenate(f_)

        frame = cv2.imread(self.filename)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cas.detectMultiScale(gray, 1.3, 5)


        for (x, y, w, h) in faces:
            face_component = frame[y:y + h, x:x + w, :]

            fc = cv2.resize(face_component, (50, 50))

            lab, tot = self.knn(fc.flatten(), data, labels)
            text = str(lab)

            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,225), 2)

            cv2.imshow('lassan', frame)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            return(text)

if __name__ == '__main__':
    p = FaceDetect("test/my.jpg")
    print("Answer : " + p.detect())

