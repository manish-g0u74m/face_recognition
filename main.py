from tkinter import*
import tkinter
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
import os 
from time import strftime

class face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        img=Image.open(r"collage_images\black_background.jpg")
        img=img.resize((1366,768),Image.AFFINE)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1366,height=768)

        # label title face recognition system
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="black",fg="blue")
        title_lbl.place(x=0,y=0,width=1366,height=130)

        # time 
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(title_lbl,font = ('times new roman' ,14,'bold'),bg="white",fg="blue")
        lbl.place(x=0,y=(-15),width=110,height=50)
        time()

        #========= Student Buttons ==================
        img4=Image.open(r"collage_images\student.png")
        img4=img4.resize((220,220),Image.AFFINE)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=180,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=400,width=220,height=30)

        #========= Face Detecter ==================
        img5=Image.open(r"collage_images\facedetecter.jpg")
        img5=img5.resize((220,220),Image.AFFINE)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,command=self.face_data,image=self.photoimg5,cursor="hand2")
        b2.place(x=400,y=180,width=220,height=220)

        b2_1=Button(bg_img,command=self.face_data,text="Face Detecter",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_1.place(x=400,y=400,width=220,height=30)

        #========= Attendance ==================
        img6=Image.open(r"collage_images\attendance.jpg")
        img6=img6.resize((220,220),Image.AFFINE)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b3=Button(bg_img,command=self.attendance_details,image=self.photoimg6,cursor="hand2")
        b3.place(x=700,y=180,width=220,height=220)

        b3_1=Button(bg_img,command=self.attendance_details,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b3_1.place(x=700,y=400,width=220,height=30)

         #========= Help Desk ==================
        img7=Image.open(r"collage_images\helpdesk.jpg")
        img7=img7.resize((220,220),Image.AFFINE)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b4=Button(bg_img,command=self.help,image=self.photoimg7,cursor="hand2")
        b4.place(x=1000,y=180,width=220,height=220)

        b4_1=Button(bg_img,command=self.help,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b4_1.place(x=1000,y=400,width=220,height=30)

        #========= Train Data ==================
        img8=Image.open(r"collage_images\traindata.jpeg")
        img8=img8.resize((220,220),Image.AFFINE)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b5=Button(bg_img,command=self.train_data,image=self.photoimg8,cursor="hand2")
        b5.place(x=100,y=450,width=220,height=220)

        b5_1=Button(bg_img,command=self.train_data,text="Train DATA",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b5_1.place(x=100,y=650,width=220,height=30)

        #========= Photos ==================
        img9=Image.open(r"collage_images\collectionphotos.jpg")
        img9=img9.resize((220,220),Image.AFFINE)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b6=Button(bg_img,command=self.open_img,image=self.photoimg9,cursor="hand2")
        b6.place(x=400,y=450,width=220,height=220)

        b6_1=Button(bg_img,command=self.open_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b6_1.place(x=400,y=650,width=220,height=30)

        #========= Developer ==================
        img10=Image.open(r"collage_images\developer.jpg")
        img10=img10.resize((220,220),Image.AFFINE)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b7=Button(bg_img,image=self.photoimg10,command=self.developer,cursor="hand2")
        b7.place(x=700,y=450,width=220,height=220)

        b7_1=Button(bg_img,text="Developer",command=self.developer,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b7_1.place(x=700,y=650,width=220,height=30)

        #========= Exit ==================
        img11=Image.open(r"collage_images\exit.jpg")
        img11=img11.resize((220,220),Image.AFFINE)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b8=Button(bg_img,command=self.iExit,image=self.photoimg11,cursor="hand2")
        b8.place(x=1000,y=450,width=220,height=220)

        b8_1=Button(bg_img,command=self.iExit,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b8_1.place(x=1000,y=650,width=220,height=30)


    #====== Photo button
    def open_img(self):
        os.startfile("data")
    
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are You Sure Exit this Project")
        if self.iExit > 0:
            self.root.destroy()
        else:
            return

    #============ Function Buttons ============
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def attendance_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

   
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)


    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def help(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

    def developer(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)  

if __name__ == "__main__":
    root=Tk()
    obj=face_Recognition_System(root)
    root.mainloop()