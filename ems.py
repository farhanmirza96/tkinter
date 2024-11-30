from customtkinter import *
from PIL import Image
from tkinter import ttk

window = CTk()
window.geometry('930x580')
window.resizable(0,0)

window.title('Employee Management System')

image = CTkImage(Image.open('employee.jpg'), size=(930,158))
imageLabel = CTkLabel(window, image=image, text='')
imageLabel.grid(row=0, column=0, columnspan=2)

leftFrame = CTkFrame(window)
leftFrame.grid(row=1, column=0 )

idLabel = CTkLabel(leftFrame, text='Employee ID', font=("garamond", 18, 'bold'))
idLabel.grid(row=0, column=0, padx=(0,20), pady=5, sticky='W')

idEntry = CTkEntry(leftFrame,width=140,height=28, corner_radius=15,border_width=2,bg_color='white',placeholder_text='Enter your ID',font=('garamond',18,))
idEntry.grid(row=0, column=1, sticky='W')

nameLabel = CTkLabel(leftFrame, text='Employee Name', font=("garamond", 18, 'bold'))
nameLabel.grid(row=1, column=0, padx=(0,20), pady=(5,5), sticky='W')

nameEntry = CTkEntry(leftFrame,width=140,height=28, corner_radius=15,border_width=2,bg_color='white',placeholder_text='Enter your name',font=('garamond',18,))
nameEntry.grid(row=1, column=1, sticky='W')

phoneLabel = CTkLabel(leftFrame, text='Employee phone', font=("garamond", 18, 'bold'))
phoneLabel.grid(row=2, column=0, padx=(0,20), pady=(5,5))

phoneEntry = CTkEntry(leftFrame,width=140,height=28, corner_radius=15,border_width=2,bg_color='white',placeholder_text='Enter your phone No.',font=('garamond',18,))
phoneEntry.grid(row=2, column=1, sticky='W')

rollLabel = CTkLabel(leftFrame, text='Employee Roll', font=("garamond", 18, 'bold'))
rollLabel.grid(row=3, column=0, padx=(0,20), pady=(5,5), sticky='W')

role_options = ['Select Role','Web Development', 'Accountant', 'Cloud Architect', 'Technical Writer']
roleCombo = CTkComboBox(leftFrame, width=140, font=('garamond',15), values=role_options, corner_radius=15)
roleCombo.grid(row=3, column=1, padx=(0,20), pady=(5,5), sticky='W')

genderLabel = CTkLabel(leftFrame, text='Gender', font=("garamond", 18, 'bold'), corner_radius=15)
genderLabel.grid(row=4, column=0, padx=(0,20), pady=(5,5), sticky='w')

gender_options = ['Select Gender', 'Male', 'Female']
genderCombo = CTkComboBox(leftFrame, width=140, font=('garamond',15), values=gender_options, corner_radius=15)
genderCombo.grid(row=4, column=1, padx=(0,20), pady=(5,5), sticky='W')

salaryLabel = CTkLabel(leftFrame, text='Employee Salary', font=("garamond", 18, 'bold'))
salaryLabel.grid(row=5, column=0, padx=(0,20), pady=(5,5), sticky='W')

salaryEntry = CTkEntry(leftFrame,width=140,height=28, corner_radius=15,border_width=2,bg_color='white',placeholder_text='Enter your Salary.',font=('garamond',18,))
salaryEntry.grid(row=5, column=1, sticky='W')

rightFrame = CTkFrame(window)
rightFrame.grid(row=1, column=1)


window.mainloop()