from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
#from other_data.train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os 

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        img=Image.open(r"collage_images\developer1.jpg")
        img=img.resize((1366,768),Image.AFFINE)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1366,height=768)

        title_lbl=Label(bg_img,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1366,height=130)

        help_lbl=Label(bg_img,text="Email: manish905759@gmail.com",font=("times new roman",20,"bold"),bg="white",fg="blue")
        help_lbl.place(x=450,y=350,width=500,height=50)

        #help_lbl=Label(bg_img,text="Email: deekshantsharma36@gmail.com",font=("times new roman",20,"bold"),bg="white",fg="blue")
        #help_lbl.place(x=450,y=400,width=500,height=50)

if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()