from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ctk
from customtkinter import *
from tkinter import *
from tkinter import messagebox
import pymysql
from dashboard import IMS
from user import User

def userLoggedIn():
    app.destroy() 
    def Exit():
           Exit= messagebox.askyesno("Report Management System","confirm if you want to exit",parent=root)
           if Exit>0:
               root.destroy()
              
    
    root = ctk.CTk()
    root.geometry("1450x730+0+0")
    root.overrideredirect(True)
    #root.overrideredirect(True)
    root.title("ADMIN PANEL")

    ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
    ctk.set_appearance_mode("dark")

    title_label1 = ctk.CTkLabel(
        root,
        text="SCHOOL ADMIN LOGIN",
        font=CTkFont(
            size=40,
            weight="bold",
            family="Microsoft YaHei UI Light"))
    title_label1.place(x=360, y=300)
    
    def login():
        password = password_entry1.get()  # Get the entered password
        if password == "111":
            pass
            # open_admin_window()
            # Close the current login window
            #root.destroy()
        else:
            messagebox.showerror("Error", "Wrong Password")

    main_frame1 = ctk.CTkFrame(master=root, width=500, height=200)
    main_frame1.place(x=430, y=400)
    
    close_button = ctk.CTkButton(root, text="Close", command=Exit, fg_color="black",bg_color="black")
    close_button.grid(row=0, column=0)

    user_label1 = ctk.CTkLabel(main_frame1,
                              text="ADMIN",
                              font=ctk.CTkFont(
                                  size=20,
                                  weight="bold",
                                  family="Microsoft YaHei UI Light"))
    user_label1.grid(row=0, column=1, pady=20)

    password_label1 = ctk.CTkLabel(main_frame1,
                                  text="Password",
                                  font=ctk.CTkFont(
                                      size=15,
                                      weight="bold",
                                      family="Microsoft YaHei UI Light"))
    password_label1.grid(row=4, column=1)
    
    password_entry1 = ctk.CTkEntry(main_frame1, show="*", width=300)
    password_entry1.grid(row=5, column=1, padx=100, pady=(0, 10))

    login_button1 = ctk.CTkButton(main_frame1, text="LOGIN", command=login)
    login_button1.grid(row=6, column=1, pady=10)

    root.mainloop()
    
def open_dos_window():
    new_window=Toplevel()
    app=IMS(new_window)
    
def register():
    new_window=Toplevel()
    app=User(new_window)
    
def validate_login(username, password):
    conn = pymysql.connect(host="localhost", user="root", database="report2")
    my_cursor = conn.cursor()
    my_cursor.execute("SELECT * FROM user WHERE username = %s AND password1 = %s", (username, password))
    user = my_cursor.fetchone()

    if user:
        pass
        #messagebox.showinfo("Success", "Login successful")
        open_dos_window()
        # Add code to open a new window here
    elif username == "" and password == "":
        messagebox.showerror("Error", "Please Enter username or password")
    else:
        messagebox.showerror("Error", "Invalid username or password")

    conn.close()
def validate_DOS(username, password, selected_role):
    conn = pymysql.connect(host="localhost", user="root", database="report2")
    my_cursor = conn.cursor()
    my_cursor.execute("SELECT * FROM user WHERE username = %s AND password1 = %s", (username, password))
    user = my_cursor.fetchone()

    if user:
        # Check if the user's role matches the selected role
        if user[3] != selected_role:  # Assuming the role is stored in the third column
            messagebox.showerror("Error", "Please select your role")
        else:
            # messagebox.showinfo("Success", "Login successful")
            open_dos_window()
            # Add code to open a new window here
    elif username == "" and password == "":
        messagebox.showerror("Error", "Please Enter username or password")
    else:
        messagebox.showerror("Error", "Invalid username or password")

    conn.close()

def userLogin():
    selected_role = role_menu.get()
    if selected_role == "Select Role":
        messagebox.showinfo("Error", "Please select a role")
    else:
        select_label.destroy()
        role_menu.destroy()
        enter_button.destroy()
        
        user_label = ctk.CTkLabel(mainFrame,
                                text=f"SELECTED ROLE: {selected_role}",
                                font=ctk.CTkFont(size=20, weight="bold", family="Microsoft YaHei UI Light"))
        user_label.grid(row=0, column=1, pady=20)
        
        if selected_role == "Admin":
            admin_button = ctk.CTkButton(app, text="Admin", command=userLoggedIn, fg_color="black", bg_color="black")
            admin_button.grid(row=1, column=0)
        username_label = ctk.CTkLabel(mainFrame,
                                    text="Username",
                                    font=ctk.CTkFont(size=15, weight="bold", family="Microsoft YaHei UI Light"))
        username_label.grid(row=1, column=1)

        var_username = ctk.StringVar()
        username_entry = ctk.CTkEntry(mainFrame, textvariable=var_username, width=300)
        username_entry.grid(row=2, column=1, padx=100, pady=(0, 20))
        
        password_label = ctk.CTkLabel(mainFrame,
                                    text="Password",
                                    font=ctk.CTkFont(size=15, weight="bold", family="Microsoft YaHei UI Light"))
        password_label.grid(row=3, column=1)

        var_password = ctk.StringVar()
        password_entry = ctk.CTkEntry(mainFrame, textvariable=var_password, show="*", width=300)
        password_entry.grid(row=4, column=1, padx=100, pady=(0, 10))
        if selected_role == "":
            login_button = ctk.CTkButton(mainFrame, text="LOGIN", command=lambda: validate_DOS(var_username.get(), var_password.get(),selected_role))
            login_button.grid(row=5, column=1, pady=10)
        else:
            login_button = ctk.CTkButton(mainFrame, text="LOGIN", command=lambda: validate_login(var_username.get(), var_password.get()))
            login_button.grid(row=5, column=1, pady=10)
            
            login_button = ctk.CTkButton(mainFrame, text="REGISTER", command=register)
            login_button.grid(row=5, column=2, pady=10)
    
    close_button = ctk.CTkButton(app, text="Close", command=Exit, fg_color="black",bg_color="black")
    close_button.grid(row=0, column=0)


def Exit():
           Exit= messagebox.askyesno("Report Management System","confirm if you want to exit",parent=app)
           if Exit>0:
               app.destroy()

app = ctk.CTk()
#app.geometry("1400x900")
app.geometry("1450x730+0+0")
from PIL import Image, ImageTk
app.overrideredirect(True)
app.title("STUDENT MANAGEMENT SYSTEM")

ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
ctk.set_appearance_mode("dark")

# Create the logo frame
logo_frame = ctk.CTkFrame(master=app)
logo_frame.place(x=600, y=4)

# Load the logo image
logo_image = Image.open("images/logo.png")  # Replace "path_to_your_logo_image.png" with the actual path to your logo image
logo_image = logo_image.resize((100, 100))  # Resize the image to fit the frame
logo_photo = ImageTk.PhotoImage(logo_image)

# Create a label to display the logo image
logo_label = ctk.CTkLabel(logo_frame, image=logo_photo)
logo_label.pack()

title_label = ctk.CTkLabel(
    app,
    text="SCHOOL MANAGEMENT SYSTEM FOR HUMM",
    font=CTkFont(
        size=40,
        weight="bold",
        family="Microsoft YaHei UI Light"))
title_label.place(x=80, y=150)

mainFrame = ctk.CTkFrame(master=app, width=500, height=200)
mainFrame.place(x=400, y=300)

select_label = ctk.CTkLabel(mainFrame,
                        text="Select Role",
                        font=CTkFont(
                            size=20,
                            weight="bold",
                            family="Microsoft YaHei UI Light"))
select_label.grid(row=0, column=2, pady=20)

roles_list = ["Select Role", "Secretary/Teacher"]

role_menu = ctk.CTkComboBox(mainFrame, values=roles_list, width=400)
role_menu.grab_current()
role_menu.grid(row=1, column=2, padx=100, pady=10)

enter_button = ctk.CTkButton(mainFrame, text="ENTER",command=userLogin)
enter_button.grid(row=2, column=2, pady=40)

app.mainloop()
#=============================================================


