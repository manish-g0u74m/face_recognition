from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from help import Help
from face_recognition import Face_Recognition
from attendance import Attendance
import os 
import tkinter
from tkinter import messagebox

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Student Window")

        img=Image.open(r"collage_images\developer1.jpg")
        img=img.resize((1366,768),Image.AFFINE)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1366,height=768)

        title_lbl=Label(bg_img,text="STUDENT ATTENDANCE WINDOW",font=("times new roman",35,"bold"),bg="black",fg="blue")
        title_lbl.place(x=0,y=0,width=1366,height=130)

        #========= Attendance ==================
        img6=Image.open(r"collage_images\attendance.jpg")
        img6=img6.resize((220,220),Image.AFFINE)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b3=Button(bg_img,command=self.face_data,image=self.photoimg6,cursor="hand2")
        b3.place(x=200,y=250,width=220,height=220)

        b3_1=Button(bg_img,command=self.face_data,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b3_1.place(x=200,y=470,width=220,height=30)

         #========= Help Desk ==================
        img7=Image.open(r"collage_images\helpdesk.jpg")
        img7=img7.resize((220,220),Image.AFFINE)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b4=Button(bg_img,command=self.help,image=self.photoimg7,cursor="hand2")
        b4.place(x=580,y=250,width=220,height=220)

        b4_1=Button(bg_img,command=self.help,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b4_1.place(x=580,y=470,width=220,height=30)
         #========= Exit ==================
        img11=Image.open(r"collage_images\exit.jpg")
        img11=img11.resize((220,220),Image.AFFINE)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b8=Button(bg_img,command=self.iExit,image=self.photoimg11,cursor="hand2")
        b8.place(x=950,y=250,width=220,height=220)

        b8_1=Button(bg_img,command=self.iExit,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b8_1.place(x=950,y=470,width=220,height=30)
    

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def help(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

    # Exit Butten
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are You Sure Exit this Project")
        if self.iExit > 0:
            self.root.destroy()
        else:
            return

if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()