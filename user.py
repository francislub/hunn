from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import tkinter as tk
#import mysql.connector
import pymysql
import random
from tkinter import filedialog
from tkcalendar import DateEntry
from datetime import datetime
import tkinter.messagebox
from tkinter import messagebox
class User:
    def __init__(self,root):
        self.root=root
        self.root.title("Report Management System")
        self.root.geometry("900x750+250+0")
        self.root.overrideredirect(True)
        #========================variables=======================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_username=StringVar()
        self.var_email=StringVar()
        self.var_role=StringVar()
        self.var_password1=StringVar()
        self.var_password2=StringVar()
        self.var_image=StringVar()
        
        #=====================title=======================================================
        lbl_title=Label(self.root,text="CREATE USER'S ACCOUNTS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1355,height=50)
        
        #===================labelframe====================================================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="User Details",font=("times new roman",18,"bold"),padx=2)
        labelframeleft.place(x=5,y=60,width=425,height=550)
        #====================labels and entrys=========================================
        lbl_student_ref = Label(labelframeleft, text="User Ref", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_student_ref.grid(row=0, column=0, sticky=W)
        
        entry_ref = ttk.Entry(labelframeleft, textvariable=self.var_ref, width=29, font=("times new roman", 13, "bold"), state="readonly")
        entry_ref.grid(row=0, column=1)
        
        last_reference = self.get_last_reference()  # Function to get the last reference
        
        if last_reference is not None:
            next_reference = str(int(last_reference) + 1)
        else:
            next_reference = "1001"  # Initial reference
        
        self.var_ref.set(next_reference)

            
        uname=Label(labelframeleft,text="User Name",font=("times new roman",12,"bold"),padx=2,pady=6)
        uname.grid(row=1,column=0,sticky=W)
        txtuname=ttk.Entry(labelframeleft,textvariable=self.var_username,width=29,font=("times new roman",13,"bold"))
        txtuname.grid(row=1,column=1)
        
        label_email=Label(labelframeleft,text="email",font=("times new roman",12,"bold"),padx=2,pady=6)
        label_email.grid(row=2,column=0,sticky=W)
        entry_email = ttk.Entry(labelframeleft, textvariable=self.var_email, width=29, font=("times new roman", 13, "bold"))
        entry_email.grid(row=2, column=1)
        
        label_role=Label(labelframeleft,text="Role",font=("times new roman",12,"bold"),padx=2,pady=6)
        label_role.grid(row=3,column=0,sticky=W)
        combo_role=ttk.Combobox(labelframeleft,textvariable=self.var_role,width=27,font=("times new roman",13,"bold"),state="readonly")
        combo_role["value"]=("Select","Teacher","Secretory")
        combo_role.current(0)
        combo_role.grid(row=3,column=1)
        
        lblpassword1=Label(labelframeleft,text="Password",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblpassword1.grid(row=4,column=0,sticky=W)
        txtpassword1=ttk.Entry(labelframeleft,textvariable=self.var_password1,width=29,font=("times new roman",13,"bold"), show="*")
        txtpassword1.grid(row=4,column=1)
        
        lblpassword2=Label(labelframeleft,text="Confirm Password",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblpassword2.grid(row=5,column=0,sticky=W)
        txtpassword2=ttk.Entry(labelframeleft,textvariable=self.var_password2,width=29,font=("times new roman",13,"bold"), show="*")
        txtpassword2.grid(row=5,column=1)
        
        #================btn===========================================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=760,height=100)
        
        btnAdd=Button(btn_frame,text="Register",command=self.add_data,font=("arial",11,"bold"),width=8)
        btnAdd.grid(row=0,column=0,padx=1)
        
        label_account=Label(btn_frame,text="Already Have account",font=("times new roman",12,"bold"),padx=2,pady=6)
        label_account.grid(row=1,column=0,sticky=W)
        
        btnExit=Button(btn_frame,text="Login",command=self.Exit,font=("arial",11,"bold"),width=8)
        btnExit.grid(row=1,column=1,padx=1)
         
    def add_data(self):
        if self.var_username.get() == "" or self.var_email.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.var_password1.get() != self.var_password2.get():
            messagebox.showerror("Error", "Passwords do not match", parent=self.root)
        else:
            try:
                conn = pymysql.connect(host="localhost", user="root", database="report2")
                my_cursor = conn.cursor()
                # Check if subjectID  already exists
                my_cursor.execute("SELECT * FROM user WHERE ref = %s", (self.var_ref.get(),))
                existing_record = my_cursor.fetchone()

                if existing_record:
                    messagebox.showerror("Error", "User reference already exists. Please enter a different reference.", parent=self.root)
                else:
                    my_cursor.execute("insert into user values(%s, %s, %s, %s, %s, %s, %s)", (
                        self.var_ref.get(),
                        self.var_username.get(),
                        self.var_email.get(),
                        self.var_role.get(),
                        self.var_password1.get(),
                        self.var_password2.get(),
                        self.var_image.get(),
                    ))
                    conn.commit()
                    self.reset()
                    conn.close()
                    messagebox.showinfo("Success", "User has been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
    def reset(self):
        try:
            # Fetch the last reference from the database
            last_reference = self.get_last_reference()

            if last_reference is not None:
                # Increment the last reference by 1
                next_reference = str(int(last_reference) + 1)
            else:
                # If there's no existing reference, set a default value
                next_reference = "1000"

            # Set the incremented reference to self.var_ref
            self.var_ref.set(next_reference)

        except Exception as e:
            print(f"Error fetching or incrementing reference: {e}")

        # Reset other variables
        self.var_username.set("")
        self.var_email.set("")
        self.var_role.set("Select")
        self.var_password1.set("")
        self.var_password2.set("")
        self.var_image.set("")
        
    def get_last_reference(self):
            try:
                conn = pymysql.connect(host="localhost", user="root", database="report2")
                cursor = conn.cursor()

                # Execute a query to get the maximum reference value from the database
                cursor.execute("SELECT MAX(ref) FROM user")

                # Fetch the result
                result = cursor.fetchone()

                # Close the database connection
                conn.close()

                # If there are no existing references, return None
                if result[0] is not None:
                    return str(result[0])
                else:
                    return None

            except Exception as e:
                print(f"Error: {e}")
                return None

    def Exit(self):
            self.root.destroy()

                    
if __name__=="__main__":
    root=Tk()
    obj=User(root)
    root.mainloop()