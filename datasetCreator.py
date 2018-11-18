import cv2
import numpy as np
from Name import name


def add(id, name):
    user.id.append(id)
    user.name.append(name)
    user.index = user.index + 1

def input():
    user = name()
    filename = 'write_data.txt'

    with open(filename, 'a') as f:
        id = input("Please input an id: ")
        name = input("please input a name: ")
        add(id, name)
        f.write((str)(user.id[user.index - 1])+" "+user.name[user.index - 1])
        f.write("\n")


def cap():
    faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
    cam = cv2.VideoCapture(0);


    sampleNum = 0;
    while (True):
        ret, img = cam.read();
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetect.detectMultiScale(gray, 1.3, 5);
        for (x, y, w, h) in faces:
            sampleNum = sampleNum + 1;
            cv2.imwrite("dataSet/User." + str(id) + "." + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)
            cv2.waitKey(100);
        cv2.imshow("Face", img);
        cv2.waitKey(1);
        if (sampleNum > 20):
            break;
    cam.release() 
    cv2.destroyAllWindows()
