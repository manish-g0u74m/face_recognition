from tkinter import*
from tkinter import ttk
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import cv2.face    #pip install opencv-contrib-python
import os
import numpy as np
import csv
from time import strftime
from datetime import datetime
#import other_data.face_recognition as face_recognition
#import pygame
from speech_recog import  Speech_Recognition
import pyttsx3



class Face_Recognition:
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="black",fg="blue")
        title_lbl.place(x=0,y=0,width=1366,height=80)

        img_top=Image.open(r"collage_images\facerecognition.jpg")
        img_top=img_top.resize((1366,660),Image.AFFINE)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=80,width=1366,height=660)

        b1_1=Button(self.root,text="FACE RECOGNITION",command=self.face_recog,cursor="hand2",font=("times new roman",15,"bold"),bg="red",fg="white")
        b1_1.place(x=560,y=665,width=225,height=40)

    #============= Face Recognition Function ============
    
   
    # Attendance 
    def mark_attendance(self, r, n, d):
        now = datetime.now()
        manish = now.strftime("%Y-%m-%d")
    
        with open(f"present-{manish}.csv", "a+", newline="\n") as f:
            f.seek(0)  # Move the file pointer to the beginning
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split(",")
                name_list.append(entry[0])

            if r not in name_list:  # Check if the roll number is not already present
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.write(f"{r},{n},{d},{dtString},{d1},Present\n")
    #========================= g0u74m

    def face_recog(self):
       # obj = Speech_Recognition()
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []
            conn = mysql.connector.connect(host="localhost", username="root", password="root123",database="face_recognition")
            my_cursor = conn.cursor()

            # my_cursor.execute("select ID from student where Student_id=" + str(id))
                # i = my_cursor.fetchone()
                # i = "+".join(n)

           
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                if confidence > 80:
                    my_cursor.execute("select Name from student where Student_id=" + str(id))
                    n = my_cursor.fetchone()
                    n = "+".join(n)
                        

                    my_cursor.execute("select Roll from student where Student_id=" + str(id))
                    r = my_cursor.fetchone()
                    r = "+".join(r)

                    my_cursor.execute("select Dep from student where Student_id=" + str(id))
                    d = my_cursor.fetchone()
                    d = "+".join(d)
                    #cv2.putText(img, f"Roll:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll:{r}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 2)
                    cv2.putText(img, f"Name:{n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 2)
                    cv2.putText(img, f"Department:{d}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 2)
                    cv2.putText(img, f"Status: Presant", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 2)
                    self.mark_attendance(r, n, d)
                    speak("Your Status Has Been Recorded")
                    
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, f"UnKnown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    speak("Unknown Person")
                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer.create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        timeout = 9  #10 Secons open camera 

        start_time = cv2.getTickCount()

        message_timeout = 5000  # 5 seconds for the messagebox

        root = tk.Tk()
        root.withdraw()
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to face Recognition", img)

            if ((cv2.getTickCount() - start_time) / cv2.getTickFrequency()) > timeout:
                break

            if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
                break
                
                
        # except Exception as e:
        #     print(f"Error: {e}")
        # finally:
        video_cap.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Status","Your Status Has Been Recorded")
        #After 5 seconds, close the messagebox
        root.after(message_timeout, root.destroy)
         
#=============================================    
def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()
  


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()