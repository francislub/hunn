from tkinter import *
import tkinter as tk
import tkinter.messagebox
from PIL import Image,ImageTk
import pymysql
from time import strftime
from teacher import Teacher_win
from student import Student

class IMS:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1450x730+0+0")
        self.root.overrideredirect(True)
        # Other initialization code...
        self.classes = []  # List to store available classes
        self.current_class_index = 0

        # Fetch available classes from the database
        self.fetch_classes()
        self.selected_class = None
        self.current_class = 1
        self.root .title("Report Management System | Developed by LarksTeckHub")
        
        
        #====================title================
        self.icon_title = PhotoImage(file="images/logo.png")
        desired_width = 100
        desired_height = 50
        self.icon_title = self.icon_title.subsample(int(self.icon_title.width() / desired_width), int(self.icon_title.height() / desired_height)) 
        title= Label(self.root, text="DIRECTOR OF STUDIES DASHBOARD",image=self.icon_title,compound=LEFT, font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        
        #============btn_logout=====
        btn_history = Button(self.root,text="History",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=10,height=50,width=150)
        #========clock================
        # Function to display time on the label
        def time():
            string = f"Welcome to Report Management System\t\t Date: {strftime('%d-%m-%Y')}\t\t Time: {strftime('%H:%M:%S')}"  # Format the time string
            self.lbl_clock.config(text=string)  # Update the label with the current time
            self.lbl_clock.after(1000, time)  # Call the time function after 1000ms (1 second)

        # Create a label for the clock
        self.lbl_clock = Label(self.root, text="", font=("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        # Call the time function to start displaying the time
        time()
        
        #===========Left Menu==============
        LeftMenu = Frame(self.root,bd=2,relief=RIDGE, bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=600)
        
                # Assuming functions to retrieve user information from the database
        def get_user_name():
            # Replace this function with your code to fetch the user's name from the database
            return "Francis"  # Example user name

        def get_user_role():
            # Replace this function with your code to fetch the user's role from the database
            return "DOS"  # Example user role

        # Placeholder for user's photo (Assumed as a box)
        user_photo_placeholder = Label(LeftMenu, text="User Photo", bg="lightgray", height=10)
        user_photo_placeholder.pack(side="top", fill="x")

        # Retrieve user information from the database
        user_name = get_user_name()
        user_role = get_user_role()

        # Label to display the user's name
        label_user_name = Label(LeftMenu, text=f"User: {user_name}",bg="#4d636d", padx=5,font=("times new roman",16,"bold"))
        label_user_name.pack(side="top", fill="x")

        # Label to display the user's role
        label_user_role = Label(LeftMenu, text=f"Role: {user_role}",bg="#4d636d", padx=5,font=("times new roman",16,"bold"))
        label_user_role.pack(side="top", fill="x")
        
        
        ########################Buttons#############################################
        self.icon_side = PhotoImage(file="images/side.png")
        new_width, new_height = 25, 25  # Set the new dimensions
        self.icon_side = self.icon_side.subsample(self.icon_side.width()// new_width, self.icon_side.height() // new_height)
       ################## Class####################################################
        
        btn_teacher = Button(LeftMenu,text="Teachers",command=self.show_loading_message,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",16,"bold"),bg="white",bd=3,cursor="hand2")
        btn_teacher.pack(side=TOP,fill=X)
        
        btn_student = Button(LeftMenu,text="Students",command=self.show_loading_student,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",16,"bold"),bg="white",bd=3,cursor="hand2")
        btn_student.pack(side=TOP,fill=X)
        
        btn_logout = Button(LeftMenu,text="Logout",command=self.logout,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",16,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        #========footer================
        
        lbl_footer = Label(self.root,text="Report Management System | Developed by LarksTeckHub \nFor any Technical Issue Contact: 0741789121",font=("times new roman",12),bg="#4d636d",fg="white").pack(side=BOTTOM, fill=X)
   
        #===============content==================
        ###############################################################
        # Display total students
        self.lbl_student = Label(self.root, text="", bd=5, relief=RIDGE, bg="#33bbf9", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_student.place(x=250, y=120, height=100, width=200)
        
        # Connect to the MySQL database
        self.mydb = pymysql.connect(host="localhost", user="root", database="report2")

        # Create a cursor object to execute SQL queries
        self.mycursor = self.mydb.cursor()

        # Initialize the slide index
        self.slide_index = 0

        # Schedule the slide show
        self.update_slideshowStudent()
        
        #===========Left Menu==============
        photoMenu = Frame(self.root,bd=2,relief=RIDGE, bg="white")
        photoMenu.place(x=250,y=225,width=1100,height=450)
        
        # Load the logo image
        logo_image = Image.open("images/dos.png")  # Replace "path_to_your_logo_image.png" with the actual path to your logo image
        logo_image = logo_image.resize((1100, 450))  # Resize the image to fit the frame
        self.logo_photo = ImageTk.PhotoImage(logo_image)
        
        # Create a label to display the logo image
        self.logo_label = Label(photoMenu, image=self.logo_photo)
        self.logo_label.pack()

    def update_slideshowStudent(self):
        # Execute queries to get relevant information
        queries = [
            "SELECT COUNT(*) FROM student",
            "SELECT COUNT(*) FROM student WHERE gender = 'Female'",
            "SELECT COUNT(*) FROM student WHERE gender = 'Male'",
            "SELECT class, COUNT(*) FROM student GROUP BY class"
        ]

        self.mycursor.execute(queries[self.slide_index])

        if self.slide_index == 0:
            result = self.mycursor.fetchone()
            total_students = result[0]
            self.lbl_student.config(text=f"Total Pupil's\n{total_students}")

        elif self.slide_index == 1:
            result = self.mycursor.fetchone()
            total_girls = result[0]
            self.lbl_student.config(text=f"Total Girls\n{total_girls}")

        elif self.slide_index == 2:
            result = self.mycursor.fetchone()
            total_boys = result[0]
            self.lbl_student.config(text=f"Total Boys\n{total_boys}")

        elif self.slide_index == 3:
            results = self.mycursor.fetchall()
            class_info = "\n".join([f"{row[0]}: {row[1]}" for row in results])
            self.lbl_student.config(text=f"Total Pupil's in Each Class\n{class_info}")

        # Increment the slide index
        self.slide_index = (self.slide_index + 1) % 4

        # Schedule the next update after 3000 milliseconds (3 seconds)
        self.root.after(3000, self.update_slideshowStudent)
        ##################################################### START ######################
               # Connect to the MySQL database
        mydb = pymysql.connect(host="localhost",user="root",database="report2")

        # Create a cursor object to execute SQL queries
        mycursor = mydb.cursor()

        # Execute an SQL query to get the total number of stuff
        mycursor.execute("SELECT COUNT(*) FROM teacher")

        # Fetch the result of the query
        result = mycursor.fetchone()

        # Get the total number of stuff from the result
        total_stuff = result[0]
        ###################################################################===================
    
        # Display the total number of stuff
        self.lbl_stuff = Label(self.root, text=f"Total Staff\n{total_stuff}", bd=5, relief=RIDGE, bg="#ff5722", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_stuff.place(x=450, y=120, height=100, width=235)
       
        ##################################################################===================================
        # Connect to the MySQL database
        mydb = pymysql.connect(host="localhost",user="root",database="report2")

        # Create a cursor object to execute SQL queries
        mycursor = mydb.cursor()

        # Execute an SQL query to get the total number of stuff
        mycursor.execute("SELECT COUNT(*) FROM subject")

        # Fetch the result of the query
        result = mycursor.fetchone()

        # Get the total number of stuff from the result
        total_subject = result[0]

        # Display the total number of stuff
        self.lbl_subject = Label(self.root, text=f"Total Subjects\n{total_subject}", bd=5, relief=RIDGE, bg="#009688", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_subject.place(x=650, y=120, height=100, width=235)
        #################################################################
       # Connect to the MySQL database
        mydb = pymysql.connect(host="localhost",user="root",database="report2")

        # Create a cursor object to execute SQL queries
        mycursor = mydb.cursor()

        # Execute an SQL query to get the total number of stuff
        mycursor.execute("SELECT COUNT(*) FROM term")

        # Fetch the result of the query
        result = mycursor.fetchone()

        # Get the total number of term from the result
        total_term = result[0]

        # Display the total number of term
        self.lbl_term = Label(self.root, text=f"Total Term\n{total_term}", bd=5, relief=RIDGE, bg="#607d8b", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_term.place(x=880, y=120, height=100, width=235)
       #########################################################
       # Connect to the MySQL database
        mydb = pymysql.connect(host="localhost",user="root",database="report2")

        # Create a cursor object to execute SQL queries
        mycursor = mydb.cursor()

        # Execute an SQL query to get the total number of user
        mycursor.execute("SELECT COUNT(*) FROM user")

        # Fetch the result of the query
        result = mycursor.fetchone()

        # Get the total number of user from the result
        total_term = result[0]

        # Display the total number of user
        self.lbl_sales = Label(self.root, text=f"Total Users\n{total_term}", bd=5, relief=RIDGE, bg="#ffc107", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_sales.place(x=1100, y=120, height=100, width=255)
        #######################################################################################################################
 
    def fetch_classes(self):
        # Fetch available classes from the database
        conn = pymysql.connect(host="localhost", user="root", database="report2")
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT class FROM subject")  
        self.classes = [cls[0] for cls in cursor.fetchall()]

        #########################################  
    def show_loading_message(self):
        self.loading_label = Label(self.root, text="Loading...", font=("times new roman", 20, "bold"))
        self.loading_label.pack()
        self.root.after(1000, self.cust_details)  # After 30 seconds, show another window
        
    def cust_details(self):
        self.loading_label.destroy()
        self.new_window=Toplevel(self.root)
        self.app=Teacher_win(self.new_window)
    
    #########################################  
        
    #########################################  
    def show_loading_student(self):
        self.loading_label = Label(self.root, text="Loading...", font=("times new roman", 20, "bold"))
        self.loading_label.pack()
        self.root.after(1000, self.student_details)  # After 30 seconds, show another window
    def student_details(self):
        self.loading_label.destroy()
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    #########################################   
        
    def logout(self):
        logout = tkinter.messagebox.askyesno("Report Management System", "Confirm if you want to log out", parent=self.root)
        if logout:
            # Perform logout actions here (e.g., closing the window, resetting variables, etc.)
            self.root.destroy()
    
if __name__=="__main__":
    root=Tk()
    ob = IMS(root)
    #ims_instance = IMS(root)
    root.mainloop()
