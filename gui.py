# PyQt5 GUI Libraries
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5 import QtCore
from PIL.ImageQt import ImageQt
import face_recognition as fr
import cv2
import numpy as np
from keras.models import load_model
import time
import imutils
from imutils.video import VideoStream
from PIL import Image
model1 = load_model("Models/gender.h5")
model2 = load_model("Models/age1.h5")
Gen = ['Male','Female']
age = ['Kid','Youth','Middle Age','Senior']
class Application(QWidget):
   
    def __init__(self, parent=None):
        
        super().__init__()
        #super(Application, self).__init__(parent)
        # Setting window parameters (Here self represents 'QWidget' object)
        self.title = "Age and Gender Classification"
        self.left = 0   # Original value: 365
        self.top = 0
        self.width = 1920   # Original value: 650
        self.height = 1080
        
        # A call to the user interface window to build and render the UI
        self.buildUI()
        
     
    def buildUI(self):
        """This function builds the entire GUI window."""
        self.imageLabel = QLabel(self)

        
        browseButton = QPushButton('Browse', self)
        browseButton.setStyleSheet("QPushButton {background-color: #192A56; color: white; border-radius: 5px;font-size:17px;border: 2px solid #4CAF50}" + 
                                   "QPushButton:pressed {background-color: white;}" + 
                                   "QPushButton:hover:!pressed {background-color: #50f8ef;border: 2px solid #4CAF50}")
        browseButton.move(1400,420)
        browseButton.resize(160,50)
        browseButton.clicked.connect(self.browse)   # Connection to the image browsing function
        
        
        webButton = QPushButton('Open WebCam', self)
        webButton.setStyleSheet("QPushButton {background-color: #192A56; color: white; border-radius: 5px;font-size:17px;border: 2px solid #4CAF50}" + 
                                   "QPushButton:pressed {background-color: white;}" + 
                                   "QPushButton:hover:!pressed {background-color: #50f8ef;border: 2px solid #4CAF50}")
        webButton.move(1400,520)
        webButton.resize(160, 50)
        webButton.clicked.connect(self.openWebCam)  # Connection to the openWebCam function
        
        vsButton = QPushButton('Open Video', self)
        vsButton.setStyleSheet("QPushButton {background-color: #192A56; color: white; border-radius: 5px;font-size:17px;border: 2px solid #4CAF50}" + 
                                   "QPushButton:pressed {background-color: white;}" + 
                                   "QPushButton:hover:!pressed {background-color: #50f8ef;border: 2px solid #4CAF50}")
        vsButton.move(1400,620)
        vsButton.resize(160, 50)
        vsButton.clicked.connect(self.openVideo)  # Connection to the openWebCam function
        
        
        
        
        # Set window background color (white is the default colour)
        self.setAutoFillBackground(True)
        palette = QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("bg.jpg"))) # Haha, aren't I so funny??
        self.setPalette(palette)
        #p = self.palette()
        #p.setStyleSheet("background-image: url(background.jpg); background-attachment: fixed")
        #p.setColor(self.backgroundRole(), Qt.black)
        #self.setPalette(p)


        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
        
    
    def browse(self):
        """This function opens the document browser window"""
        fname = QFileDialog.getOpenFileName(self, 'Open file',"D://Project/Final Project/Outputss/TestImages/" , 'Image files (*.jpg)')        
        my_im1 = cv2.cvtColor(cv2.imread(fname[0]),cv2.COLOR_BGR2RGB)
        my_im = cv2.imread(fname[0],cv2.IMREAD_GRAYSCALE)
        #my_im = image_resize(my_im,height=640)
        face_locations = fr.face_locations(my_im)
        for (top, right, bottom, left) in face_locations:
            face_image = my_im[top:bottom,left:right]
            face_image=cv2.resize(face_image,(180,180),interpolation = cv2.INTER_AREA)
            face_image=np.array(face_image).reshape(-1,180,180,1)
            my_res = model1.predict_classes(face_image)
            my_age = model2.predict_classes(face_image)
            gen = str(Gen[int(my_res)])+":"+age[int(my_age)]
            cv2.rectangle(my_im1, (left, top), (right, bottom), (255, 0, 0), 2)
            #cv2.rectangle(my_im1, (left, bottom+20 ), (right, bottom), (255, 0, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            frame = cv2.putText(my_im1, gen, (left, top - 10), font, 1, (255, 0,0), 1)
            #frame = image_resize(frame,height=1024)
            final=Image.fromarray(frame)
        final.show()
        #imageq = ImageQt(final) #convert PIL image to a PIL.ImageQt object
        #qimage = QImage(imageq) #cast PIL.ImageQt object to QImage object -that´s the trick!!!
        #dis_image = QPixmap(qimage)
        #self.imageLabel.setPixmap(dis_image)
        #self.imageLabel.resize(1024, 1024)
        #self.imageLabel.move(20,20)
        
        
    def openWebCam(self):
        """This function opens the webcam"""
        
        cap = cv2.VideoCapture(0)
        while(True):
            ret, frame = cap.read()
            rgb_small_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            face_locations = fr.face_locations(frame)
            # Saves image of the current frame in jpg file
            for (top, right, bottom, left) in face_locations:
                face_image = frame[top:bottom,left:right]
                face_image=cv2.resize(face_image,(180,180),interpolation = cv2.INTER_AREA)
                face_image=cv2.cvtColor(face_image,cv2.COLOR_BGR2GRAY)
                face_image=np.array(face_image).reshape(-1,180,180,1)
                my_res = model1.predict_classes(face_image)
                my_age = model2.predict_classes(face_image)
                gen = str(Gen[int(my_res)])+":"+age[int(my_age)]
                cv2.rectangle(frame, (left-5, top-5), (right+5, bottom+5), (0, 0, 255), 2)
                cv2.rectangle(frame, (left, bottom+20 ), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_TRIPLEX
                cv2.putText(frame, gen, (left, bottom+10), font, 0.75, (255, 255, 255), 1)
            # Display the resulting image
            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1) & 0xFF

            # if the `q` key was pressed, break from the loop
            if key == ord("q"):
                break
            if key == 27: # press 'ESC' to quit
                break
                
                
    def openVideo(self):
        """This function opens the webcam"""
        fname = QFileDialog.getOpenFileName(self, 'Open file',"D://Project/Final Project/" , 'Video File (*.mp4 *.mkv *.3gp *.wmv *.* )')
        cap = cv2.VideoCapture(fname[0])
        while(True):
            ret, frame = cap.read()
            rgb_small_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            face_locations = fr.face_locations(frame)
            # Saves image of the current frame in jpg file
            for (top, right, bottom, left) in face_locations:
                face_image = frame[top:bottom,left:right]
                face_image=cv2.resize(face_image,(180,180),interpolation = cv2.INTER_AREA)
                face_image=cv2.cvtColor(face_image,cv2.COLOR_BGR2GRAY)
                face_image=np.array(face_image).reshape(-1,180,180,1)
                my_res = model1.predict_classes(face_image)
                my_age = model2.predict_classes(face_image)
                gen = str(Gen[int(my_res)])+":"+age[int(my_age)]
                cv2.rectangle(frame, (left-5, top-5), (right+5, bottom+5), (0, 0, 255), 2)
                cv2.rectangle(frame, (left-5, bottom+20 ), (right, bottom-10), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_TRIPLEX
                cv2.putText(frame, gen, (left, bottom+10), font, 0.75, (255, 255, 255), 1)
            # Display the resulting image
            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1) & 0xFF

            # if the `q` key was pressed, break from the loop
            if key == ord("q"):
                break
            if key == 27: # press 'ESC' to quit
                break
application = QCoreApplication.instance()
if application is None:
    application = QApplication([])
example = Application()
application.exec_()