from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        # ========= Variables =========
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
    
        #====================================


        img=Image.open(r"collage_images\black_background.jpg")
        img=img.resize((1366,768),Image.AFFINE)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1366,height=768)

        # label title Student menegment System system
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="black",fg="blue")
        title_lbl.place(x=0,y=0,width=1366,height=130)

        # Creating Frame on the first label bg_img 
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=30,y=110,width=1300,height=600)

        # left label frame 
        Left_frame=LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text=("Student Details"),font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=625,height=580)

        img_left=Image.open(r"collage_images\student.png")
        img_left=img_left.resize((615,120),Image.AFFINE)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        bg_img=Label(Left_frame,image=self.photoimg_left)
        bg_img.place(x=5,y=0,width=610,height=90)

        # Current Course 
        current_course_frame=LabelFrame(Left_frame,bg="white",bd=2,relief=RIDGE,text=("Current Course Information"),font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=90,width=610,height=110)
        #Department 
        dep_lebel=Label(current_course_frame,text="Department:",font=("times new roman",13,"bold"),bg="white")
        dep_lebel.grid(row=0,column=0,padx=2,pady=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=20,state="readonly")
        dep_combo["values"]=("Select Department","Computer Science","IT","Civil","Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        # Course 
        course_lebel=Label(current_course_frame,text="Course:",font=("times new roman",13,"bold"),bg="white")
        course_lebel.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=20,state="readonly")
        course_combo["values"]=("Select Course","BCA","MCA","BTECH","MBA")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        # Year 
        year_lebel=Label(current_course_frame,text="Year:",font=("times new roman",12,"bold"),bg="white")
        year_lebel.grid(row=1,column=0,padx=2,pady=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=20,state="readonly")
        year_combo["values"]=("Select Year","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Semester 
        semester_lebel=Label(current_course_frame,text="Semester:",font=("times new roman",13,"bold"),bg="white")
        semester_lebel.grid(row=1,column=2,padx=10,pady=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=20,state="readonly")
        semester_combo["values"]=("Select Semester","Semeseter-1","Semester-2","Semester-3","Semester-4")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=10,pady=10,sticky=W)

        # Class Student Information  Frame
        class_student_frame=LabelFrame(Left_frame,bg="white",bd=2,relief=RIDGE,text=("Class Student Information"),font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=200,width=612,height=352)

        # Student Id
        studentId_lebel=Label(class_student_frame,text="Student ID:",font=("times new roman",13,"bold"),bg="white")
        studentId_lebel.grid(row=0,column=0,padx=2,pady=5,sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=17,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        # Student Name
        student_name_lebel=Label(class_student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
        student_name_lebel.grid(row=0,column=2,padx=2,pady=10,sticky=W)

        student_name__entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=19,font=("times new roman",13,"bold"))
        student_name__entry.grid(row=0,column=3,padx=2,pady=5,sticky=W)

        # Class Division
        class_div_lebel=Label(class_student_frame,text="Class Division:",font=("times new roman",13,"bold"),bg="white")
        class_div_lebel.grid(row=1,column=0,padx=2,pady=10,sticky=W)

        #class_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=17,font=("times new roman",13,"bold"))
        #class_div_entry.grid(row=1,column=1,padx=2,pady=5,sticky=W)

        devision_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),width=17,state="readonly")
        devision_combo["values"]=("Select Section:","A","B","C")
        devision_combo.current(0)
        devision_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)

        # Roll No
        rollno_lebel=Label(class_student_frame,text="Roll No:",font=("times new roman",13,"bold"),bg="white")
        rollno_lebel.grid(row=1,column=2,padx=2,pady=10,sticky=W)

        rollno_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=19,font=("times new roman",13,"bold"))
        rollno_entry.grid(row=1,column=3,padx=2,pady=5,sticky=W)

        # Gender
        gender_lebel=Label(class_student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        gender_lebel.grid(row=2,column=0,padx=2,pady=10,sticky=W)

        #gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=17,font=("times new roman",13,"bold"))
        #gender_entry.grid(row=2,column=1,padx=2,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=17,state="readonly")
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=5,sticky=W)



        #DOB
        dob_lebel=Label(class_student_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
        dob_lebel.grid(row=2,column=2,padx=2,pady=10,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=19,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=2,pady=5,sticky=W)

        #Email
        email_lebel=Label(class_student_frame,text="Email:",font=("times new roman",13,"bold"),bg="white")
        email_lebel.grid(row=3,column=0,padx=2,pady=10,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=17,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=2,pady=5,sticky=W)

        #Phone No
        phone_lebel=Label(class_student_frame,text="Phone No:",font=("times new roman",13,"bold"),bg="white")
        phone_lebel.grid(row=3,column=2,padx=2,pady=10,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=19,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=2,pady=5,sticky=W)

        #Address
        address_lebel=Label(class_student_frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
        address_lebel.grid(row=4,column=0,padx=2,pady=10,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=17,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=2,pady=5,sticky=W)

        # Teacher Tutor Name
        teacher_lebel=Label(class_student_frame,text="Class Teacher",font=("times new roman",13,"bold"),bg="white")
        teacher_lebel.grid(row=4,column=2,padx=2,pady=10,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=19,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=2,pady=5,sticky=W)

        # Radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,text="Take Photo Sampple",value="Yes",variable=self.var_radio1)
        radiobtn1.grid(row=6,column=0)

        
        radiobtn2=ttk.Radiobutton(class_student_frame,text="No Photo Sample",variable=self.var_radio1,value="No")
        radiobtn2.grid(row=6,column=1)

        # buttom frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=4,y=250,width=600,height=36)

        # save button
        save_btn=Button(btn_frame,command=self.add_data,text="Save",width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        # update button
        update_btn=Button(btn_frame,command=self.update_data,text="Update",width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        # delete button
        delete_btn=Button(btn_frame,command=self.delete_data,text="Delete",width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        # reset button
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        # button frame1
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=4,y=290,width=600,height=36)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=29,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=29,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)



        # right label frame
        Right_frame=LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text=("Student Details"),font=("times new roman",12,"bold"))
        Right_frame.place(x=650,y=10,width=635,height=580)

        img_right=Image.open(r"collage_images\student.png")
        img_right=img_right.resize((620,120),Image.AFFINE)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        bg_img=Label(Right_frame,image=self.photoimg_right)
        bg_img.place(x=5,y=0,width=620,height=90)

        # Search System 

        search_frame=LabelFrame(Right_frame,text="Search System",bd=2,relief=RIDGE,font=("times new roman",13,"bold"),bg="white")
        search_frame.place(x=4,y=100,width=620,height=70)

        search_lebel=Label(search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="red",fg="white")
        search_lebel.grid(row=0,column=0,padx=2,pady=10,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=10,state="readonly")
        search_combo["values"]=("Select","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=2,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=13,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showall_btn=Button(search_frame,text="Show All",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4,padx=4)

        # Table frame 
        table_frame=LabelFrame(Right_frame,bg="white",bd=2,relief=RIDGE,font=("times new roman",12,"bold"))
        table_frame.place(x=5,y=180,width=620,height=365)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x,yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photo")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    # ======= Function Decleration =======================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            #try:
                conn=mysql.connector.connect(host="localhost",username="root",password="root123",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_std_id.get(),
                                                                                                            self.var_std_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_radio1.get(),
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details added Successfully",parent=self.root)
   # except Exception as es:
     #   messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    # ============== FETCH DATA ====
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root123",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                  self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    # =============== get function ===============
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])


    # update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            #try:
                Update=messagebox.askyesno("Update","Do You want to update student details",parent=self.root)
                if Update > 0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="root123",database="face_recognition")
                    my_cursor=conn.cursor() 
                    my_cursor.execute("update student set Dep=%s,Course=%s,year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                                        self.var_std_id.get()
                                                                                                                                                                                                                ))
                else:
                     if not Update:
                          return
                messagebox.showinfo("Success","Student Details Successfully Updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            # except Exception as es:
             #   messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    # delete Data Function
    def delete_data(self):
        if self.var_std_id.get()=="":
              messagebox.showerror("Error","Student id must be requird",parent=self.root)
        else:
            #try:
            delete=messagebox.askyesno("Student Delete Page","Do you want to delete This Studete Data",parent=self.root)
            if delete>0:
                conn=mysql.connector.connect(host="localhost",username="root",password="root123",database="face_recognition")
                my_cursor=conn.cursor()
                sql="delete from student where Student_id=%s"
                val=(self.var_std_id.get(),)
                my_cursor.execute(sql,val)  
            else:
                if not delete:
                     return
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Delete","Successfully Delete Student Details",parent=self.root)

    # Reset data
    def reset_data(self):
         self.var_dep.set("Select Department")
         self.var_course.set("Select Course")
         self.var_year.set("Select Year")
         self.var_semester.set("Select Semester")
         self.var_std_id.set("")
         self.var_std_name.set("")
         self.var_div.set("Select Division")
         self.var_roll.set("")
         self.var_gender.set("Select Gender")
         self.var_dob.set("")
         self.var_email.set("")
         self.var_phone.set("")
         self.var_address.set("")
         self.var_teacher.set("")
         self.var_radio1.set("")
         
#============= Generate data set or take photo sample  ===========
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_id.get()=="" or self.var_std_name.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            #try:
            conn=mysql.connector.connect(host="localhost",username="root",password="root123",database="face_recognition")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from student") 
            myresult=my_cursor.fetchall()
            id=0
            for x in myresult:
                 id+=1
            my_cursor.execute("update student set Dep=%s,Course=%s,year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                                self.var_std_id.get()==id+1
                                                                                                                                                                                                                ))
            conn.commit()
            self.fetch_data()
            self.reset_data()
            conn.close()

            # Load pre define data on face frontals from opencv
            face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            def face_cropped(img):
                 gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                 faces=face_classifier.detectMultiScale(gray,1.3,5)
                 # Scaling Factor=1.3
                 # Minimum Neighbor=5 
                 for (x,y,w,h) in faces:
                      face_cropped=img[y:y+h,x:x+w]
                      return face_cropped
            cap=cv2.VideoCapture(0)
            img_id=0
            try:
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Croped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==40:
                        break
            except Exception as e:
                 print(f"Error: {e}")
            finally:
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Generating Data Sets Completed Successfully",parent=self.root)


if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()