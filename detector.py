#-*-coding:utf8-*-
import cv2
import numpy as np

from Name import name
user = name()
with open('write_data.txt') as f:
    for line1 in f:
        info = line1.split()
        user.id.append(info[0])
        user.name.append(info[1])

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam = cv2.VideoCapture(0);
rec =  cv2.createLBPHFaceRecognizer()
rec.load('/home/zsf/桌面/FaceRecognizer-master (3)/faceRecogination/recognizer/trainningData.yml')
id = 0
font = cv2.FONT_HERSHEY_SIMPLEX
while (True):
    ret, img = cam.read();
    if not ret: continue
    if len(img.shape) == 3 or len(img.shape) == 4:
     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
     gray = img
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5);
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        id, conf = rec.predict(gray[y:y + h, x:x + w])
        if (conf < 140):
            id = user.name[id-1]
        else:
            id = "stranger"
        cv2.putText(img, str(id), (x, y + h), font, 3,(100,100,100));

    cv2.imshow("Face", img);
    if (cv2.waitKey(1) == ord('q')):
        break;
cam.release()
cv2.destroyAllWindows()
