from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import tkinter as tk
#import mysql.connector
import pymysql
from tkinter import filedialog
from tkcalendar import DateEntry
from datetime import datetime
import tkinter.messagebox
from tkinter import messagebox
class Reset:
    def __init__(self,root):
        self.root=root
        self.root.title("School Management System")
        self.root.geometry("1550x800+0+0")
        self.root.overrideredirect(True)
        #========================variables=======================

        self.var_email=StringVar()
        self.var_password1=StringVar()
        self.var_password2=StringVar()
        
        #=====================title=======================================================
        lbl_title=Label(self.root,text="RESET PASSWORD",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1355,height=50)
        #===================2st Image===log======================================================
        
        #===================labelframe====================================================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Password",font=("times new roman",18,"bold"),padx=2)
        labelframeleft.place(x=5,y=60,width=425,height=550)
        #====================labels and entrys=========================================
            
        email=Label(labelframeleft,text="Enter Your Email",font=("times new roman",12,"bold"),padx=2,pady=6)
        email.grid(row=1,column=0,sticky=W)
        txtemail=ttk.Entry(labelframeleft,textvariable=self.var_email,width=29,font=("times new roman",13,"bold"))
        txtemail.grid(row=2,column=0)
        
        label_password=Label(labelframeleft,text="New Password",font=("times new roman",12,"bold"),padx=2,pady=6)
        label_password.grid(row=3,column=0,sticky=W)
        entry_password = ttk.Entry(labelframeleft, textvariable=self.var_password1, width=29, font=("times new roman", 13, "bold"), show="*")
        entry_password.grid(row=4, column=0)
        
        lblpassword2=Label(labelframeleft,text="Confirm Password",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblpassword2.grid(row=5,column=0,sticky=W)
        txtpassword2=ttk.Entry(labelframeleft,textvariable=self.var_password2,width=29,font=("times new roman",13,"bold"), show="*")
        txtpassword2.grid(row=6,column=0)
        
        
        #================btn===========================================
        btn_frame=Frame(labelframeleft,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=700,height=50)
        
        btnAdd=Button(btn_frame,text="Update Password",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=18)
        btnAdd.grid(row=0,column=0,padx=1)
        
        btnExit=Button(btn_frame,text="Close",command=self.Exit,font=("arial",11,"bold"),bg="black",fg="gold",width=18)
        btnExit.grid(row=0,column=4,padx=1)
         
    def add_data(self):
        if self.var_email.get() == "" or self.var_password1.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.var_password1.get() != self.var_password2.get():
            messagebox.showerror("Error", "Passwords do not match", parent=self.root)
        else:
            try:
                conn = pymysql.connect(host="localhost", user="root", database="report2")
                my_cursor = conn.cursor()
                # Check if email exists
                my_cursor.execute("SELECT * FROM user WHERE email = %s", (self.var_email.get(),))
                existing_record = my_cursor.fetchone()

                if existing_record:
                    # Update password
                    my_cursor.execute("UPDATE user SET password1 = %s,password2 = %s WHERE email = %s", (self.var_password1.get(),self.var_password2.get(), self.var_email.get()))
                    conn.commit()
                    self.reset()
                    conn.close()
                    messagebox.showinfo("Success", "Password Updated successfully", parent=self.root)
                else:
                    messagebox.showerror("Error", "Email does not exist", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
    def reset(self):
        self.var_email.set("")
        self.var_password1.set("")
        self.var_password2.set("")
        
    def Exit(self):
           self.Exit= tkinter.messagebox.askyesno("Report Management System","confirm if you want to exit",parent=self.root)
           if self.Exit>0:
               self.root.destroy()

                    
if __name__=="__main__":
    root=Tk()
    obj=Reset(root)
    root.mainloop()