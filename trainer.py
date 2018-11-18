import os
import numpy as np
import cv2
from PIL import Image
def train():
 recognizer=cv2.createLBPHFaceRecognizer()
 path='dataSet'

 def getImagesWithID(path):
	    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
	    faces=[]
	    IDs=[]
	    for imagePath in imagePaths:
	     faceImg=Image.open(imagePath).convert('L');
	     faceNp=np.array(faceImg,'uint8')
	     ID=int( os.path.split(imagePath)[-1].split('.')[1])
	     faces.append(faceNp)
	     print (ID)
	     IDs.append(ID)
	     #cv2.imshow("training",faceNp)
	     #cv2.waitKey(10)
	    return IDs,faces


 Ids,faces=getImagesWithID(path)
 recognizer.train(faces,np.array(Ids))
 recognizer.save('recognizer/trainningData.yml')
 cv2.destroyAllWindows()
