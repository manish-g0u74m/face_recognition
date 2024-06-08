from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        # ========== Variable =========
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()


        img=Image.open(r"collage_images\attendance.jpg")
        img=img.resize((1366,768),Image.AFFINE)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1366,height=768)

        # label title Student menegment System system
        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="black",fg="blue")
        title_lbl.place(x=0,y=0,width=1366,height=130)

        # Creating Frame on the first label bg_img 
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=30,y=110,width=1300,height=600)

        # left label frame 
        Left_frame=LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text=("Student Attendance Details"),font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=625,height=580)

        img_left=Image.open(r"collage_images\student.png")
        img_left=img_left.resize((615,120),Image.AFFINE)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        bg_img=Label(Left_frame,image=self.photoimg_left)
        bg_img.place(x=5,y=0,width=610,height=130)

        # Current Course 
        student_details_frame=LabelFrame(Left_frame,bg="white",bd=2,relief=RIDGE,text=("Current Course Information"),font=("times new roman",12,"bold"))
        student_details_frame.place(x=5,y=130,width=610,height=420)

        #  Roll no
        rollno_lebel=Label(student_details_frame,text="Roll No:",font=("times new roman",13,"bold"),bg="white")
        rollno_lebel.grid(row=0,column=0,padx=2,pady=5,sticky=W)

        rollno_entry=ttk.Entry(student_details_frame,textvariable=self.var_atten_roll,width=17,font=("times new roman",13,"bold"))
        rollno_entry.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        # Student Name
        student_name_lebel=Label(student_details_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
        student_name_lebel.grid(row=0,column=2,padx=2,pady=10,sticky=W)

        student_name__entry=ttk.Entry(student_details_frame,textvariable=self.var_atten_name,width=19,font=("times new roman",13,"bold"))
        student_name__entry.grid(row=0,column=3,padx=2,pady=5,sticky=W)

        # Department
        dep_lebel=Label(student_details_frame,text="Department:",font=("times new roman",13,"bold"),bg="white")
        dep_lebel.grid(row=1,column=0,padx=2,pady=10,sticky=W)

        dep_entry=ttk.Entry(student_details_frame,textvariable=self.var_atten_dep,width=17,font=("times new roman",13,"bold"))
        dep_entry.grid(row=1,column=1,padx=2,pady=5,sticky=W)

        # Attendance System
        attendance_status_lebel=Label(student_details_frame,text="Attendance Status:",font=("times new roman",13,"bold"),bg="white")
        attendance_status_lebel.grid(row=1,column=2,padx=2,pady=10,sticky=W)

        attendance_status_combo=ttk.Combobox(student_details_frame,textvariable=self.var_atten_attendance,font=("times new roman",12,"bold"),width=19,state="readonly")
        attendance_status_combo["values"]=("Status","Present","Absent")
        attendance_status_combo.current(0)
        attendance_status_combo.grid(row=1,column=3,padx=2,pady=5,sticky=W)

        # Time Status
        time_lebel=Label(student_details_frame,text="Time:",font=("times new roman",13,"bold"),bg="white")
        time_lebel.grid(row=2,column=0,padx=2,pady=10,sticky=W)

        time_entry=ttk.Entry(student_details_frame,textvariable=self.var_atten_time,width=17,font=("times new roman",13,"bold"))
        time_entry.grid(row=2,column=1,padx=2,pady=5,sticky=W)

        # Date Status
        date_lebel=Label(student_details_frame,text="Date:",font=("times new roman",13,"bold"),bg="white")
        date_lebel.grid(row=2,column=2,padx=2,pady=10,sticky=W)

        date_entry=ttk.Entry(student_details_frame,textvariable=self.var_atten_date,width=19,font=("times new roman",13,"bold"))
        date_entry.grid(row=2,column=3,padx=2,pady=5,sticky=W)

        # buttom frame
        btn_frame=Frame(student_details_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=4,y=250,width=600,height=36)

        # Import button
        save_btn=Button(btn_frame,command=self.importCsv,text="Import csv",width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        # Export button
        update_btn=Button(btn_frame,command=self.exportCsv,text="Export csv",width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        # Update button
        delete_btn=Button(btn_frame,text="Update",width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        # reset button
        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        

        # Right Label frame 
        Right_frame=LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text=("Attendance Details"),font=("times new roman",12,"bold"))
        Right_frame.place(x=650,y=10,width=635,height=580)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=620,height=545)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("roll","name","department","time","date","attendance"))

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("roll",text="Roll No")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
    # =============== Fetch data =================
        
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    #import csv 

    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #export csv 
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"Successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content["values"]
        self.var_atten_roll.set(rows[0])
        self.var_atten_name.set(rows[1])
        self.var_atten_dep.set(rows[2])
        self.var_atten_time.set(rows[3])
        self.var_atten_date.set(rows[4])
        self.var_atten_attendance.set(rows[5])

    def reset_data(self):
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")




if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()