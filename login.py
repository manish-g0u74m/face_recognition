from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk  #pip install pillow
from tkinter import messagebox 
import mysql.connector          #pip install mysql-connector-python
from main import face_Recognition_System
import re   # for mail validaion
def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1366x768+0+0")

        self.bg=ImageTk.PhotoImage(file=r"image\blue_background.jpg")
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=510,y=170,width=340,height=450)

        img1=Image.open(r"image\user.png")
        img1=img1.resize((100,100),Image.AFFINE)
        self.photoImage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoImage1,bg="black",borderwidth=0)
        lblimg1.place(x=630,y=175,width=100,height=100)

        get_str=Label(frame,text="Admin Login",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #label

        username=lbl=Label(frame, text="Email", font=("times new roman", 15, "bold"), fg="white", bg="black") 
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame, font=("times new roman", 15, "bold"),validate="key") 
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black") 
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame, font=("times new roman", 15, "bold"),show="*") 
        self.txtpass.place(x=40,y=250,width=270)

        # ======Icon Images==============

        img2=Image.open(r"image\username.png") 
        img2=img2.resize((25,25), Image.AFFINE)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black", borderwidth=0)
        lblimg1.place(x=550,y=323, width=25, height=25)

        img3=Image.open(r"image\password.png")
        img3=img3.resize((25,25), Image.AFFINE)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black", borderwidth=0)
        lblimg1.place(x=550,y=395, width=25, height=25)

        #Login Button 
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        #registerbutton
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)

        #forgetpassbtn
        
        registerbtn=Button(frame,command=self.forget_password_window,text="Forget Password",font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=10,y=370,width=160)
    # ======= Register Window Button Function ==========
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)



    # ============= Reset Password========
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select security Question")
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer")
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please Enter the New Password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root123",database="mydata")
            my_curser=conn.cursor()
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_curser.execute(qury,value)
            row=my_curser.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter Correct Answer")
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_curser.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your Password has been Reset,Please login with new Password")
                self.root2.destroy()


    # ====== Forgot password Window function ===
    def forget_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root123",database="mydata")
            my_curser=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_curser.execute(query,value)
            row=my_curser.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror("My Error","Please Enter the valid mail for forget password")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")
                
                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Question",font=("time new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)
                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place?","Your Girlfriend Name?","Your Pet Name?")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)


                security_A=Label(self.root2,text="Security Question Answer",font=("time new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("time new roman",15))
                self.txt_security.place(x=50,y=180,width=250)
                
                new_password=Label(self.root2,text="Enter New Password",font=("time new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("time new roman",15),show="*")
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,command=self.reset_pass,text="Reset",font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=135,y=290)




    # Login Function
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="manish" and self.txtpass.get()=="sharma":
            messagebox.showinfo("Success","Welcome Manish")
        else:
           # messagebox.showerror("Invalid","Invalid username & password")
            conn=mysql.connector.connect(host="localhost",user="root",password="root123",database="mydata")
            my_curser=conn.cursor()
            my_curser.execute("select * from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
                                                                                       ))
            row=my_curser.fetchone()

            # Print Row
            if row==None:
                messagebox.showerror("Error","Invalid username & Password")
            else:
                #open_main=messagebox.askyesno("YesNo","Access only Authority Persion")
                #if open_main>0:
                self.new_window=Toplevel(self.root)
                self.app=face_Recognition_System(self.new_window )
            #else:
                    #if not open_main:
                #return
                    #messagebox.showinfo("Success","Login Successfully")
                
            conn.commit()
            conn.close()


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1366x768+0+0")

        # ================= variable ===========
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contect=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=IntVar()
        
        # ================= bg Image =============
        self.bg=ImageTk.PhotoImage(file=r"image\blue_background.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)


        # ======= left image ========
        self.bg1=ImageTk.PhotoImage(file=r"image\register1.png")
        #self.bg1=img.resize()
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=90,y=100,width=400,height=550)

        # =========== main frame =================
        frame=Frame(self.root,bg="white")
        frame.place(x=490,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("time new roman",20,"bold"),fg="black",bg="white")
        register_lbl.place(x=20,y=20)


        # ============== label and entry ==========

        #=========row1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",14,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)

        #===========row2
        contact=Label(frame,text="Contact No",font=("time new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contect,font=("time new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("time new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("time new roman",15))
        self.txt_email.place(x=370,y=200,width=250)
        email = self.var_email.get()
        #===========row3
        security_Q=Label(frame,text="Select Security Question",font=("time new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place?","Your Girlfriend Name?","Your Pet Name?")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)


        security_A=Label(frame,text="Select Security Question",font=("time new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("time new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

        #==========row4
        pswd=Label(frame,text="Password",font=("time new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("time new roman",15),show="*")
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("time new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("time new roman",15),show="*")
        self.txt_confirm_pswd.place(x=370,y=340,width=250)


        #============ check Button ===========
        
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Condition",font=("times new roman",12,"bold"))
        checkbtn.place(x=50,y=380)

        #=========== Register or login button ===========
        img=Image.open(r"image\registerlogo.png")
        img=img.resize((200,50),Image.AFFINE)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,command=self.register_data,image=self.photoimage,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white",bg="white")
        b1.place(x=10,y=420,width=300)

        img1=Image.open(r"image\loginlogo.png")
        img1=img1.resize((200,55),Image.AFFINE)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),fg="white",bg="white")
        b1.place(x=330,y=420,width=300)


#=================== function declaration =================
    def register_data(self):
        if self.var_fname.get()=="" or self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif len(self.var_contect.get())<10 or len(self.var_contect.get())>10:
            messagebox.showerror("Error","Please Enter a Valid Number")
        elif validate_email(self.var_email.get()) == False:
            messagebox.showerror("Error","Please Enter Valid Email Address")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error","Password and Confirm Password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and condition")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root123",database="mydata")
            my_curser=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_curser.execute(query,value)
            row=my_curser.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exits. Please try Again")
            else:
                my_curser.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contect.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()
                                                                                    ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Register Successfully")

    def return_login(self):
        self.root.destroy()

#======== main file function ======
def main_function(self):
            self.new_window=Toplevel(self.root)
            self.app=face_Recognition_System(self.new_window)

# email validation function
 
def validate_email(email):
    # Email validation regex
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return True
    else:
        return False

if __name__ == "__main__":
    main()