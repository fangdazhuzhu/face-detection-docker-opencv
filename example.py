# -*- coding: utf-8 -*-
import sys 
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import time
import os
import cv2


global date_path
data_path="~/FaceRecognizer-master (4)/faceRecogination/dataSet/"


class Login(QDialog):
    def __init__(self,*args):
        super(Login,self).__init__(*args)
        loadUi('Login.ui',self)
        self.pushButtonOK.clicked.connect(self.slotLogin)
        self.pushButtonCancle.clicked.connect(self.slotCancle)
        self.lineEditPasswd.setEchoMode(QLineEdit.Password)
        #self.label_img.setPixmap(QPixmap('../图/2.jpg'))
        #self.pushButton.setStyleSheet('QPushButton{border-image:url(22.png)}')
        self.ncImage=QImage('../图/2.jpg')
        self.label_img.setPixmap(QPixmap.fromImage(self.ncImage).scaled(self.label_img.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation))
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('../图/3.jpg'))
        palette1 = QPalette()
        palette1.setBrush(self.backgroundRole(), QBrush(QPixmap('../图/1.jpg')))   # 设置背景图片
        self.setPalette(palette1)
        #self.setWindowFlags(Qt.WindowMinMaxButtonsHint)#######允许窗体最大最小化

    
    def slotLogin(self):
        if self.lineEditUser.text()!="admin" or self.lineEditPasswd.text()!="123":
            #self.labelTips.show()
            QMessageBox.information(self,"Information","密码错误!")
            self.lineEditUser.setText("")
            self.lineEditPasswd.setText("")
        else:
            self.accept()

    def minFunc(self,name):
        
        self.minAnimation = QtCore.QPropertyAnimation(self,"windowOpacity")
        self.minAnimation.finished.connect(self.showMinimized2)
        self.minAnimation.setDuration(200)
        self.minAnimation.setStartValue(1)
        self.minAnimation.setEndValue(0)
        self.minAnimation.start()
    def showMinimized2(self):
        self.showMinimized()
        self.setWindowOpacity(1)

    def slotCancle(self):
        self.reject()
    
    
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',"Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
 
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore() 
    
    
    def loginEvent(self):
        
        self.dia=_classfication()
        self.dia.show()



class _classfication(QDialog):
    def __init__(self):
        super(_classfication,self).__init__()
        loadUi('cv-keras.ui',self)
        self.pushButton_cv.clicked.connect(self.login_cv)
        #cvMap = QPixmap("../图/cv.jpg").scaled(self.label.width(),self.label.height())
        #self.pushButton_cv.setPixmap(cvMap)
        self.pushButton_cv.setStyleSheet('QPushButton{border-image:url(../图/cv.jpg)}')
        self.pushButton_keras.setStyleSheet('QPushButton{border-image:url(../图/keras.jpg)}')
        self.pushButton_keras.clicked.connect(self.login_keras)

    def login_cv(self):
        self.accept()
        self.l_cv=Face_cv()
        self.l_cv.show()
    


    def login_keras(self):
        self.accept()
        self.l_keras=Face_keras()
        self.l_keras.show()


sys.path.append('~/FaceRecognizer-master (4)/faceRecogination/')
from Name import name
import datasetCreator
import create
import trainer
class Input_(QDialog):
    def __init__(self):
        super(Input_,self).__init__()
        loadUi('Input.ui',self)
        self.pushButton.clicked.connect(self.clicke_)
        self.pushButton.clicked.connect(self.accept)
        self.pushButton_2.clicked.connect(self.reject)
        
        
    def clicke_(self):
        name=self.text_name.text()
        f=open('write_data.txt','r')
        lines = f.readlines()
        id = len(lines)
        f.close()       
        id+=1
        create.create(id,name)       
        trainer.train()



            
class Face_keras(QDialog):
    def __init__(self):
        super(Face_keras,self).__init__()
        loadUi('face_keras.ui',self)
        self.pushButton_exit.clicked.connect(self.logoutEvent)
        self.setWindowIcon(QIcon('../图/3.jpg'))
        palette1 = QPalette()
        palette1.setBrush(self.backgroundRole(), QBrush(QPixmap('../图/1.jpg')))    
        self.setPalette(palette1)


    def logoutEvent(self):
        self.accept()
        self.Log=_classfication()
        self.Log.show()
        _classfication()


    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',"Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
 
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()    


class Face_cv(QDialog):
    def __init__(self):
        super(Face_cv,self).__init__()
        loadUi('Face.ui',self)
        self.pushButtonInput.clicked.connect(self.showDialog)
        self.pushButtonSql.clicked.connect(self.showmySql)
        self.pushButtonExit.clicked.connect(self.logoutEvent)
        self.pushButtonDet.clicked.connect(self.Start)
        self.setWindowTitle('Icon')
        self.label_camera.setPixmap(QPixmap('../图/2.jpg'))
        self.setWindowIcon(QIcon('../图/3.jpg'))
        #palette1 = QPalette()
        #palette1.setBrush(self.backgroundRole(), QBrush(QPixmap('../图/1.jpg')))    
        #self.setPalette(palette1)
        self.timer = QTimer()
        self.timer2 = QTimer()
        self.timer2.start()
        self.timer.start()
        self.timer.setInterval(10)    
        self.timer2.setInterval(1000000)
        self.setWindowFlags(Qt.WindowMinMaxButtonsHint)#######允许窗体最大最小化


    def Start(self,event):
        self.cap=cv2.VideoCapture(0)
        self.timer.timeout.connect(self.capture)
        self.timer2.timeout.connect(self.release)

    def release(self):
       self.cap.release() 




    def minFunc(self,name):
        
        self.minAnimation = QtCore.QPropertyAnimation(self,"windowOpacity")
        self.minAnimation.finished.connect(self.showMinimized2)
        self.minAnimation.setDuration(200)
        self.minAnimation.setStartValue(1)
        self.minAnimation.setEndValue(0)
        self.minAnimation.start()
    def showMinimized2(self):
        self.showMinimized()
        self.setWindowOpacity(1)


    def capture(self):
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
        #cam = cv2.VideoCapture(0);
        rec =  cv2.createLBPHFaceRecognizer()
        rec.load('recognizer/trainningData.yml')
        id = 0
        font = cv2.FONT_HERSHEY_SIMPLEX
        while (True):
        #if (self.cap.isOpened()):
            ret, img = self.cap.read();
            if not ret: continue
            if len(img.shape) == 3 or len(img.shape) == 4:
              gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
              
            else:
              gray = img
            # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)            
            faces = faceDetect.detectMultiScale(gray, 1.3, 5);
            x=0
            y=0
            h=0
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                id, conf = rec.predict(gray[y:y + h, x:x + w])
                if (conf < 70):
                 id = user.name[id-1]
                else:
                 id = "stranger"
            cv2.putText(img, str(id), (x, y + h), font, 1,(0,255,255))
            height, width, bytesPerComponent = img.shape
            bytesPerLine = bytesPerComponent * width
            cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
            self.image=QImage(img.data,width,height,bytesPerLine,QImage.Format_RGB888)
            self.label_camera.setPixmap(QPixmap.fromImage(self.image).scaled(self.label_camera.width(),self.label_camera.height()))
            cv2.imshow("Face", img);
            if (cv2.waitKey(1) == ord('q')):
                break;
        #
            cv2.destroyAllWindows()
        

    #def showname_1(self):
        #self.name_1.setPixmap(QPixmap('/home/f/camera.png'))
    

    def showDialog(self):
        self.Cr=Input_()
        self.Cr.show()
        Input_()
	     
    
    
    def showmySql(self):
        openfile_name = QFileDialog.getExistingDirectory(self,'select','data_path')
    
    
    
    def logoutEvent(self):
        self.accept()
        self.Log=_classfication()
        self.Log.show()
        _classfication()
    
    
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',"Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
 
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
'''
    def keyPressEvent(self,event):
        # F11全屏切换
        
        if event.key()==QtCore.Qt.Key_F11:
            self.MaxAndNormal()
        if event.key()==QtCore.Qt.Key_F4:
            self.WebView.page().mainFrame().setScrollBarPolicy(Qt.Vertical, Qt.ScrollBarAlwaysOff)

'''






if __name__ == '__main__':
    app = QApplication(sys.argv)
    login= Login()
    Face=Face_cv()
    if login.exec_():
        login.loginEvent()
           #if Login.slotLogin():
                   #i=i+1 
    else:
       print("quit")
       sys.exit(1)

    sys.exit(app.exec_())


   
