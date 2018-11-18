import cv2
import numpy as np

def create(a,b):
    from Name import name
    user = name()
    filename = 'write_data.txt'
    with open(filename, 'a') as f:
        #id = input("Please input an id: ")
        #Sname = input("please input a name: ")
        id=a
        user.id.append(a)
        user.name.append(b)
        user.index = user.index + 1
        f.write((str)(user.id[user.index - 1])+" "+user.name[user.index - 1])
        f.write("\n")

    faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
    #cam = cv2.VideoCapture(0)
    sampleNum=0
    while (True):
        ret, img = self.cap.read()
        if len(img.shape) == 3 or len(img.shape) == 4:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            gray=img
        faces = faceDetect.detectMultiScale(gray, 1.3, 5);
        for (x, y, w, h) in faces:
            sampleNum = sampleNum + 1;
            cv2.imwrite("dataSet/User." +str(id)+ "." + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.waitKey(100);
        cv2.imshow("Face", img);
        cv2.waitKey(1);
        cv2.destroyAllwindows()
        if (sampleNum > 100):
            break
        #cv2.destroyAllWindows()
    cam.release()
    
