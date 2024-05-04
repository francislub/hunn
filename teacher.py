from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import tkinter as tk
#import mysql.connector
import pymysql
import random
import tkinter.messagebox
from tkinter import messagebox
class Teacher_win:
    def __init__(self,root):
        self.root=root
        self.root.title("School Management System")
        self.root.geometry("1550x800+0+0")
        self.root.overrideredirect(True)
        #========================variables=======================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_teacher_name=StringVar()
        self.var_gender=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        
        self.serch_var=StringVar()
        self.txt_search=StringVar()
        
        #=====================title=======================================================
        lbl_title=Label(self.root,text="ADD TEACHER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1355,height=50)
        #===================2st Image===log======================================================
        #===================labelframe====================================================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Teacher Details",font=("times new roman",18,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=500)
        #====================labels and entrys=========================================
        lbl_teacher_ref = Label(labelframeleft, text="Teacher Ref", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_teacher_ref.grid(row=0, column=0, sticky=W)
        
        entry_ref = ttk.Entry(labelframeleft, textvariable=self.var_ref, width=29, font=("times new roman", 13, "bold"), state="readonly")
        entry_ref.grid(row=0, column=1)
        
        last_reference = self.get_last_reference()  # Function to get the last reference
        
        if last_reference is not None:
            next_reference = str(int(last_reference) + 1)
        else:
            next_reference = "1001"  # Initial reference
        
        self.var_ref.set(next_reference)

            
        ename=Label(labelframeleft,text="Teacher Name",font=("times new roman",12,"bold"),padx=2,pady=6)
        ename.grid(row=1,column=0,sticky=W)
        txtename=ttk.Entry(labelframeleft,textvariable=self.var_teacher_name,width=29,font=("times new roman",13,"bold"))
        txtename.grid(row=1,column=1)
        
        label_gender=Label(labelframeleft,text="Gender",font=("times new roman",12,"bold"),padx=2,pady=6)
        label_gender.grid(row=2,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,width=27,font=("times new roman",13,"bold"),state="readonly")
        combo_gender["value"]=("Select","Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=2,column=1)
        
        lblMobile=Label(labelframeleft,text="Mobile",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblMobile.grid(row=3,column=0,sticky=W)
        txtMobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,width=29,font=("times new roman",13,"bold"))
        txtMobile.grid(row=3,column=1)
        
        lblEmail=Label(labelframeleft,text="Email",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblEmail.grid(row=4,column=0,sticky=W)
        txtEmail=ttk.Entry(labelframeleft,textvariable=self.var_email,width=29,font=("times new roman",13,"bold"))
        txtEmail.grid(row=4,column=1)
        
        lblNationality=Label(labelframeleft,text="Nationality",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNationality.grid(row=5,column=0,sticky=W)
        combo_Nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,width=27,font=("times new roman",13,"bold"))
        combo_Nationality["value"]=("Ugandan","Kenyan","Tanzania","Others")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=5,column=1)
        
        lblAddress=Label(labelframeleft,text="Address",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblAddress.grid(row=6,column=0,sticky=W)
        txtAddress=ttk.Entry(labelframeleft,textvariable=self.var_address,width=29,font=("times new roman",13,"bold"))
        txtAddress.grid(row=6,column=1)
        #================btn===========================================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=420,width=760,height=550)
        
        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=0,padx=1)
        
        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnUpdate.grid(row=0,column=1,padx=1)
        
        btnDelete=Button(btn_frame,text="Delete",command=self.Delete,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnDelete.grid(row=0,column=2,padx=1)
        
        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnReset.grid(row=0,column=3,padx=1)
        
        btnExit=Button(btn_frame,text="Close",command=self.Exit,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnExit.grid(row=0,column=4,padx=1)
        
        #===============table===============
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("arial",12,"bold"))
        Table_Frame.place(x=435,y=50,width=915,height=490)
        
        lblSearchBy=Label(Table_Frame,text="Search By:",font=("times new roman",12,"bold"),bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)
        
        self.serch_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.serch_var,width=20,font=("times new roman",13,"bold"),state="readonly")
        combo_Search["value"]=("Ref","Name")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)
        
        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,width=20,font=("times new roman",13,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)
        
        btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnSearch.grid(row=0,column=3,padx=1)
        
        btnShowAll=Button(Table_Frame,text="Show All",command=self.show_all_data,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnShowAll.grid(row=0,column=4,padx=1)
        
        #================Show data table===========================================
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=890,height=400)
        
        Scrollbar_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        Scrollbar_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        
        self.Cust_Details_Table=ttk.Treeview(details_table,columns=("ref","name","gender","mobile","email","nationality","address"),xscrollcommand=Scrollbar_x.set,yscrollcommand=Scrollbar_y.set)
        Scrollbar_x.pack(side=BOTTOM,fill=X)
        Scrollbar_y.pack(side=RIGHT,fill=Y)
        

        Scrollbar_x.config(command=self.Cust_Details_Table.xview)
        Scrollbar_y.config(command=self.Cust_Details_Table.yview)
        
        self.Cust_Details_Table.heading("ref",text="Refer No", anchor=tk.CENTER)
        self.Cust_Details_Table.heading("name",text="Name", anchor=tk.CENTER)
        self.Cust_Details_Table.heading("gender",text="Gender", anchor=tk.CENTER)
        self.Cust_Details_Table.heading("mobile",text="Mobile", anchor=tk.CENTER)
        self.Cust_Details_Table.heading("email",text="Email", anchor=tk.CENTER)
        self.Cust_Details_Table.heading("nationality",text="Nationality", anchor=tk.CENTER)
        self.Cust_Details_Table.heading("address",text="Address", anchor=tk.CENTER)
        
        self.Cust_Details_Table["show"]="headings"
        s = ttk.Style(root)
        s.theme_use("clam")
        
        s.configure(".", font=('Helvetice',11))
        s.configure("Treeview.Heading",foreground='red',font=('Helvetica',11,"bold"))
        
        self.Cust_Details_Table.column("ref",width=100, anchor=tk.CENTER)
        self.Cust_Details_Table.column("name",width=400, anchor=tk.CENTER)
        self.Cust_Details_Table.column("gender",width=100, anchor=tk.CENTER)
        self.Cust_Details_Table.column("mobile",width=200, anchor=tk.CENTER)
        self.Cust_Details_Table.column("email",width=250, anchor=tk.CENTER)
        self.Cust_Details_Table.column("nationality",width=100, anchor=tk.CENTER)
        self.Cust_Details_Table.column("address",width=150,anchor=tk.CENTER)
        
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cusrsor)
        self.fetch_data()
        
        self.Cust_Details_Table.tag_configure("evenrow", background="#f0f0f0")
        self.Cust_Details_Table.tag_configure("oddrow", background="#ffffff")
        
    def add_data(self):
        if self.var_mobile.get() == "" or self.var_teacher_name.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = pymysql.connect(host="localhost", user="root", database="report2")
                my_cursor = conn.cursor()
                # Check if subjectID  already exists
                my_cursor.execute("SELECT * FROM teacher WHERE ref = %s", (self.var_ref.get(),))
                existing_record = my_cursor.fetchone()

                if existing_record:
                    messagebox.showerror("Error", "Teacher reference already exists. Please enter a different reference.", parent=self.root)
                
                else:
                    my_cursor.execute("insert into teacher values(%s, %s, %s, %s, %s, %s, %s)", (
                        self.var_ref.get(),
                        self.var_teacher_name.get(),
                        self.var_gender.get(),
                        self.var_mobile.get(),
                        self.var_email.get(),
                        self.var_nationality.get(),
                        self.var_address.get()
                    ))
                    conn.commit()
                    self.fetch_data()
                    self.reset()
                    conn.close()
                    messagebox.showinfo("Success", "Teacher has been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def fetch_data(self):
        conn = pymysql.connect(host="localhost", user="root", database="report2")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from teacher")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            # Clear existing data in the treeview
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())

            # Insert new rows into the treeview
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
            
            # Commit changes and close the connection
                conn.commit()
            conn.close()

        # Add tags to alternate rows
        for i, item in enumerate(self.Cust_Details_Table.get_children()):
            if i % 2 == 0:
                self.Cust_Details_Table.item(item, tags=("oddrow",))
            else:
                self.Cust_Details_Table.item(item, tags=("evenrow",))

    def get_cusrsor(self,event=""):
       cusrsor_row=self.Cust_Details_Table.focus()
       content=self.Cust_Details_Table.item(cusrsor_row)
       row=content["values"]
        
       self.var_ref.set(row[0]),
       self.var_teacher_name.set(row[1]),
       self.var_gender.set(row[2]),
       self.var_mobile.set(row[3]),
       self.var_email.set(row[4]),
       self.var_nationality.set(row[5]),
       self.var_address.set(row[6])
        
    def update(self):
       if self.var_mobile.get()=="":
           messagebox.showerror("Error","Please enter mobile number",parent=self.root)
       else:
           conn=pymysql.connect(host="localhost",user="root",database="report2")
           my_cursor=conn.cursor()
           my_cursor.execute("update  teacher set Name=%s,Gender=%s,Mobile=%s,Email=%s,Nationality=%s,Address=%s where Ref=%s",(
                   self.var_teacher_name.get(),
                   self.var_gender.get(),
                   self.var_mobile.get(),
                   self.var_email.get(),
                   self.var_nationality.get(),
                   self.var_address.get(),
                   self.var_ref.get()
           ))
           conn.commit()
           self.fetch_data()
           conn.close()
           self.reset()
           messagebox.showinfo("Update","Teacher details has been updated sucessfully",parent=self.root)
    def Delete(self):
       Delete=messagebox.askyesno("Report Management System","Do you want to delete this Teacher",parent=self.root)
       if Delete>0:
           conn=pymysql.connect(host="localhost",user="root",database="report2")
           my_cursor=conn.cursor()
           query="delete from teacher where Ref=%s"
           value=(self.var_ref.get(),)
           my_cursor.execute(query,value)
       else:
           if not Delete:
               return
       conn.commit()
       self.fetch_data()
       conn.close()
       self.reset()

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
        self.var_teacher_name.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        self.var_address.set("")
        
    def search(self):
       conn=pymysql.connect(host="localhost",user="root",database="report2")
       my_cursor=conn.cursor()
        
       my_cursor.execute("SELECT * FROM teacher WHERE " + str(self.serch_var.get()) + " LIKE %s", ('%' + str(self.txt_search.get()) + '%',))
        
       rows=my_cursor.fetchall()
       if len(rows)!=0:
           self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
           for i in rows:
               self.Cust_Details_Table.insert("",END,values=i)
           conn.commit()
       conn.close()
       # Add tags to alternate rows
       for i, item in enumerate(self.Cust_Details_Table.get_children()):
           if i % 2 == 0:
               self.Cust_Details_Table.item(item, tags=("oddrow",))
           else:
               self.Cust_Details_Table.item(item, tags=("evenrow",))
       
    def show_all_data(self):
        conn = pymysql.connect(host="localhost", user="root", database="report2")
        my_cursor = conn.cursor()

        my_cursor.execute("SELECT * FROM teacher")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            # Assuming self.Cust_Details_Table is your treeview widget
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())

            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)

            conn.commit()
            conn.close()
        for i, item in enumerate(self.Cust_Details_Table.get_children()):
            if i % 2 == 0:
                self.Cust_Details_Table.item(item, tags=("oddrow",))
            else:
                self.Cust_Details_Table.item(item, tags=("evenrow",))
                
    def get_last_reference(self):
            try:
                conn = pymysql.connect(host="localhost", user="root", database="report2")
                cursor = conn.cursor()

                # Execute a query to get the maximum reference value from the database
                cursor.execute("SELECT MAX(ref) FROM teacher")

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
           self.Exit= tkinter.messagebox.askyesno("Report Management System","confirm if you want to exit",parent=self.root)
           if self.Exit>0:
               self.root.destroy()

                    
if __name__=="__main__":
    root=Tk()
    obj=Teacher_win(root)
    root.mainloop()