from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os 

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        img=Image.open(r"collage_images\developer1.jpg")
        img=img.resize((1366,768),Image.AFFINE)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1366,height=768)

        title_lbl=Label(bg_img,text="DEVELOPER",font=("times new roman",35,"bold"),bg="black",fg="blue")
        title_lbl.place(x=0,y=0,width=1366,height=130)

if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()