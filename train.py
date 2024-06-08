from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import cv2.face    #pip install opencv-contrib-python
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="black",fg="blue")
        title_lbl.place(x=0,y=0,width=1366,height=130)

        img_top=Image.open(r"collage_images\train.jpg")
        img_top=img_top.resize((1366,700),Image.AFFINE)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=130,width=1366,height=650)

        b1_1=Button(self.root,command=self.train__classifier,text="TRAIN DATA",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=260,y=400,width=220,height=50)

    # Creating Function for train data

    def train__classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]


        faces=[]
        ids=[]

        for image in path:
            img =Image.open(image).convert('L') #Gray sale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Traing",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        # ======== Train the classifire  and save the data ========

        clf=cv2.face.LBPHFaceRecognizer.create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Datasets Completed Successfully",parent=self.root)

if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()