from customtkinter import *
from PIL import Image
from tkinter import messagebox

def login():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Required Feild!', 'Please enter username and password')
    elif usernameEntry.get() == 'farhan' and passwordEntry.get() == '1234':
        messagebox.showinfo('','Login successful.')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Required Feild!', 'Incorrect username and password')

root = CTk()
root.geometry('930x478')
root.resizable(0,0)

root.title('Login Page')

image = CTkImage(Image.open('login.jpg'), size=(930,478))
imageLabel = CTkLabel(root, image=image, text='')
imageLabel.place(x=0,y=0)

headingLabel = CTkLabel(root, text='Employ Management System', bg_color='#bac9f0', font=('Garamond',20,'bold'), text_color='dark blue').place(x=20,y=100)

usernameEntry = CTkEntry(root, placeholder_text='Enter your user name', width=180)
usernameEntry.place(x=50,y=150)
passwordEntry = CTkEntry(root, placeholder_text='Enter your password', width=180, show='*')
passwordEntry.place(x=50,y=200)

loginBtn = CTkButton(root, text='Login', cursor='hand2', command=login).place(x=70,y=250)

root.mainloop()