# -*- coding: utf-8 -*-
import sys 
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time
import os
import cv2
import pickle,getpass
global date_path
data_path="~/face-detection-docker-opencv/dataSet/"
global count_cap,cap
count_cap=1

class Login(QDialog):

    def __init__(self,*args):
        super(Login,self).__init__(*args)
        loadUi('Login.ui',self)
        self.pushButtonOK.clicked.connect(self.slotLogin)
        self.pushButtonCancle.clicked.connect(self.signUp)
        self.lineEditPasswd.setEchoMode(QLineEdit.Password)
        #self.label_img.setPixmap(QPixmap('./图/2.jpg'))
        #self.pushButton.setStyleSheet('QPushButton{border-image:url(22.png)}')
        self.ncImage=QImage('./图/2.jpg')
        self.label_img.setPixmap(QPixmap.fromImage(self.ncImage).scaled(self.label_img.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation))
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('./图/3.jpg'))
        palette1 = QPalette()
        palette1.setBrush(self.backgroundRole(), QBrush(QPixmap('./图/1.jpg')))   # 设置背景图片
        self.setPalette(palette1)
        #self.setWindowFlags(Qt.WindowMinMaxButtonsHint)#######允许窗体最大最小化

    def userName_(self):
        try:
           with open('./user/username.pickle','rb') as f:
               return pickle.load(f)
        except EOFError:
           return None

    def slotLogin(self):
        A=Login()
        userName=A.userName_()
        print userName
        if self.lineEditUser.text() not in userName.keys():
            QMessageBox.information(self,"Information","用户不存在")
            self.lineEditUser.setText("")
            self.lineEditPasswd.setText("")
        elif userName.get(self.lineEditUser.text()) == self.lineEditPasswd.text():
            QMessageBox.information(self,"Information","Welcome!")
            self.accept()
        else:
            QMessageBox.information(self,"Information","密码错误!")

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

    def signUp(self):
        B=Login()
        userName=B.userName_()
        usr_dic={}
        if self.lineEditUser.text() in userName.keys():
            QMessageBox.information(self,"Information","用户已存在!")
        elif len(self.lineEditPasswd.text()) < 3:
            QMessageBox.information(self,"Information","密码太短!")     
        else:
            usr_dic.clear()
            usr_dic[self.lineEditUser.text()]=self.lineEditPasswd.text()
            with open('./user/username.pickle','wb') as f:
                pickle.dump(usr_dic,f)
            QMessageBox.information(self,"Information","注册成功!")
      
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
        self.pushButton_cv.setStyleSheet('QPushButton{border-image:url(./图/cv.jpg)}')
        self.pushButton_keras.setStyleSheet('QPushButton{border-image:url(./图/keras.jpg)}')
        self.pushButton_keras.clicked.connect(self.login_keras)

    def login_cv(self):
        self.accept()
        self.l_cv=Face_cv()
        self.l_cv.show()
    
    def login_keras(self):
        self.accept()
        self.l_keras=Face_keras()
        self.l_keras.show()

sys.path.append('~/face-detection-docker-opencv/')
from Name import name
import datasetCreator
import create
#import trainer

class Input_(QDialog):

    def __init__(self):
        super(Input_,self).__init__()
        loadUi('Input.ui',self)
        self.pushButton.clicked.connect(self.clicke_)
        self.pushButton.clicked.connect(self.accept)
        self.pushButton_2.clicked.connect(self.reject)            

    def clicke_(self):
        global path3
        name=self.text_name.text()
        if name.strip()!='':            
            f=open('write_data.txt','r')
            lines = f.readlines()
            id = len(lines)
            f.close()       
            id+=1
            create.create(id,name)
            path2=os.path.join("dataSet/"+str(id))
            path3=os.path.join(path2,name)
            Exist=os.path.exists(path3)
            print "Exist",Exist
            if not Exist:
                os.makedirs(path3)
            else:
                print "创建失败"
            Exist=os.path.exists(path3)
            if  Exist:
                print "不存在"
                path3=os.path.join(path2,"Sql/")
                os.makedirs(path3)
            Exist=os.path.exists(path3)
            if  Exist:
                print "已建立"            
                self.accept()
                A=Face_cv()
                A.show()
                A.cap_() 
        else:
            QMessageBox.information(self,"无输入","请输入姓名：")

            
class Face_keras(QDialog):

    def __init__(self):
        super(Face_keras,self).__init__()
        loadUi('face_keras.ui',self)
        self.pushButton_exit.clicked.connect(self.logoutEvent)
        self.setWindowIcon(QIcon('./图/3.jpg'))
        palette1 = QPalette()
        palette1.setBrush(self.backgroundRole(), QBrush(QPixmap('./图/1.jpg')))    
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

import trainer
class Face_cv(QDialog):

    def __init__(self):
        super(Face_cv,self).__init__()
        loadUi('Face.ui',self)
        self.pushButtonInput.clicked.connect(self.showDialog)
        self.pushButtonDet.setStyleSheet('QPushButton{border-image:url(./图/2.jpg)}')
        #self.pushButtonInput.clicked.connect(self.cap_)
        self.pushButtonSql.clicked.connect(self.showmySql)
        self.pushButtonExit.clicked.connect(self.logoutEvent)
        self.pushButtonDet.clicked.connect(self.Start)
        self.setWindowTitle('Icon')
        self.label_camera.setPixmap(QPixmap('../图/2.jpg'))
        self.setWindowIcon(QIcon('../图/3.jpg'))
        palette1 = QPalette()
        palette1.setBrush(self.backgroundRole(), QBrush(QPixmap('./图/8.jpg')))   # 设置背景图片
        self.setPalette(palette1)
        self.timer = QTimer()
        self.timer.start()
        self.timer.setInterval(10)    


    def Start(self):
        global count_cap,cap
        if count_cap==1:
            cap=cv2.VideoCapture(0)
        self.timer.timeout.connect(self.capture) 

   # def minFunc(self,name):        
    #    self.minAnimation = QtCore.QPropertyAnimation(self,"windowOpacity")
    #    self.minAnimation.finished.connect(self.showMinimized2)
    #    self.minAnimation.setDuration(200)
     #   self.minAnimation.setStartValue(1)
    #    self.minAnimation.setEndValue(0)
     #   self.minAnimation.start()

    #def showMinimized2(self):
     #   self.showMinimized()
      #  self.setWindowOpacity(1)

    def capture(self):
        from Name import name
        user = name()
        with open('write_data.txt') as f:
            for line1 in f:
                info = line1.split()
                user.id.append(info[0])
                user.name.append(info[1])
        print user.id        
        print user.name
        faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
        rec =  cv2.createLBPHFaceRecognizer()
        rec.load('recognizer/trainningData.yml')
        ids = 0
        font = cv2.FONT_HERSHEY_SIMPLEX
        while (True):
            ret, img = cap.read();
            if not ret: continue
            if len(img.shape) == 3 or len(img.shape) == 4:
              gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)              
            else:
              gray = img         
            faces = faceDetect.detectMultiScale(gray, 2, 5);
            x=0
            y=0
            w=0
            h=0
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                ids, conf = rec.predict(gray[y:y + h, x:x + w])
                idss=ids
                #print ids,":",conf
                if (conf < 70):
                 ids = user.name[ids-1]
                else:
                 ids = "stranger"
                print ids,":",conf
                names=ids
                path_img=os.path.join('dataSet/'+str(idss),names)
                print path_img
                Exist2=os.path.exists(path_img)
                if Exist2:
                  img2=cv2.imread(path_img+ids+'.jpg')
                #cv2.cvtColor(img2, cv2.COLOR_BGR2RGB, img)
                  cv2.imshow('face',img2)
                #self.image2=QImage()
                #self.label_img.setPixmap(QPixmap.fromImage(self.image2).scaled(self.label_img.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation))
        #self.ncImage=QImage('../图/2.jpg')
        #self.label_img.setPixmap(QPixmap.fromImage(self.ncImage).scaled(self.label_img.size(),Qt.KeepAspectRatio,Qt.SmoothTransformation))                 
            cv2.putText(img, str(ids), (x, y + h), font, 1,(0,255,255))
            height, width, bytesPerComponent = img.shape
            bytesPerLine = bytesPerComponent * width
            cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
            self.image=QImage(img.data,width,height,bytesPerLine,QImage.Format_RGB888)
            self.label_camera.setPixmap(QPixmap.fromImage(self.image).scaled(self.label_camera.width(),self.label_camera.height()))
            #cv2.imshow("Face", img);
            if (cv2.waitKey(1) == ord('q')):
                break
            cv2.destroyAllWindows()
      
  
    def cap_(self):
            global path3
            f=open('write_data.txt','r')
            lines = f.readlines()
            id = len(lines)
            f.close()          
            faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
            sampleNum=0
            while (True):
                ret, img = cap.read()
                if len(img.shape) == 3 or len(img.shape) == 4:
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                else:
                    gray=img
                faces = faceDetect.detectMultiScale(gray, 2.5, 5)
                x=0
                y=0
                w=0
                h=0
                for (x, y, w, h) in faces:
                    sampleNum = sampleNum + 1;
                    cv2.imwrite(path3+"/User." +str(id)+ "." + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                height, width, bytesPerComponent = img.shape
                bytesPerLine = bytesPerComponent * width
                cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
                self.image=QImage(img.data,width,height,bytesPerLine,QImage.Format_RGB888)
                self.label_camera.setPixmap(QPixmap.fromImage(self.image).scaled(self.label_camera.width(),self.label_camera.height()))
                cv2.waitKey(200);
                if (sampleNum > 100):
                    QMessageBox.information(self,"成功","录入完毕")
                    break
                cv2.destroyAllWindows()
            trainer.train(id)
        #cv2.destroyAllWindows()
        #self.cap.release() 
   
    def showDialog(self):
        self.Cr=Input_()
        self.Cr.show()
        Input_() 
        
    def showmySql(self):
        openfile_name = QFileDialog.getExistingDirectory(self,'select','data_path')    
    
    def logoutEvent(self):
        global count_cap
        count_cap+=1
        #self.cap.release()
        cv2.destroyAllWindows()
        self.accept()
        self.Log=_classfication()
        self.Log.show()
        _classfication()
  
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',"Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No) 
        if reply == QMessageBox.Yes:
            self.accept()
            cv.insho()
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
    else:
       print("quit")
       sys.exit(1)

    sys.exit(app.exec_())


   
