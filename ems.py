from customtkinter import *
from PIL import Image
from tkinter import ttk

window = CTk()
window.geometry('930x580')
window.resizable(0,0)

window.title('Employee Management System')

window.configure(fg_color = '#161c30')

image = CTkImage(Image.open('employee.jpg'), size=(930,158))
imageLabel = CTkLabel(window, image=image, text='')
imageLabel.grid(row=0, column=0, columnspan=2)

leftFrame = CTkFrame(window)
leftFrame.grid(row=1, column=0 )
leftFrame.configure(fg_color = '#161c30')

idLabel = CTkLabel(leftFrame, text='Employee ID', font=("garamond", 18, 'bold'), text_color='white')
idLabel.grid(row=0, column=0, padx=(0,20), pady=5, sticky='W')

idEntry = CTkEntry(leftFrame,width=140,height=28, corner_radius=0,border_width=2,bg_color='white',placeholder_text='Enter your ID',font=('garamond',18,))
idEntry.grid(row=0, column=1, sticky='W')

nameLabel = CTkLabel(leftFrame, text='Employee Name', font=("garamond", 18, 'bold'), text_color='white')
nameLabel.grid(row=1, column=0, padx=(0,20), pady=(5,5), sticky='W')

nameEntry = CTkEntry(leftFrame,width=140,height=28, corner_radius=0,border_width=2,bg_color='white',placeholder_text='Enter your name',font=('garamond',18,))
nameEntry.grid(row=1, column=1, sticky='W')

phoneLabel = CTkLabel(leftFrame, text='Employee phone', font=("garamond", 18, 'bold'), text_color='white')
phoneLabel.grid(row=2, column=0, padx=(0,20), pady=(5,5))

phoneEntry = CTkEntry(leftFrame,width=140,height=28, corner_radius=0,border_width=2,bg_color='white',placeholder_text='Enter your phone No.',font=('garamond',18,))
phoneEntry.grid(row=2, column=1, sticky='W')

rollLabel = CTkLabel(leftFrame, text='Employee Roll', font=("garamond", 18, 'bold'), text_color='white')
rollLabel.grid(row=3, column=0, padx=(0,20), pady=(5,5), sticky='W')

role_options = ['Select Role','Web Development', 'Accountant', 'Cloud Architect', 'Technical Writer']
roleCombo = CTkComboBox(leftFrame, width=140, font=('garamond',15), values=role_options, corner_radius=0, state='readonly')
roleCombo.set(role_options[0])
roleCombo.grid(row=3, column=1, padx=(0,20), pady=(5,5), sticky='W')

genderLabel = CTkLabel(leftFrame, text='Gender', font=("garamond", 18, 'bold'), corner_radius=0, text_color='white')
genderLabel.grid(row=4, column=0, padx=(0,20), pady=(5,5), sticky='w')

gender_options = ['Select Gender', 'Male', 'Female']
genderCombo = CTkComboBox(leftFrame, width=140, font=('garamond',15), values=gender_options, corner_radius=0, state='readonly')
genderCombo.set(gender_options[0])
genderCombo.grid(row=4, column=1, padx=(0,20), pady=(5,5), sticky='W')

salaryLabel = CTkLabel(leftFrame, text='Employee Salary', font=("garamond", 18, 'bold'), text_color='white')
salaryLabel.grid(row=5, column=0, padx=(0,20), pady=(5,5), sticky='W')

salaryEntry = CTkEntry(leftFrame,width=140,height=28, corner_radius=0,border_width=2,bg_color='white',placeholder_text='Enter your Salary.',font=('garamond',15,))
salaryEntry.grid(row=5, column=1, sticky='W')

rightFrame = CTkFrame(window)
rightFrame.grid(row=1, column=1)

search_options = ['ID', 'Employee Name', 'Phone', 'Role', 'Gender', 'Salary']
searchCombo = CTkComboBox(rightFrame, width=140, font=('garamond',15), values=search_options, corner_radius=0, state='readonly')
searchCombo.set('Search By')
searchCombo.grid(row=0, column=0, padx=(0,20), pady=(5,5), sticky='W')

searchEntry = CTkEntry(rightFrame,width=140,height=28, corner_radius=0,border_width=2,bg_color='white',placeholder_text='Enter your Salary.',font=('garamond',15,))
searchEntry.grid(row=0, column=1, sticky='W', padx=(0,20))

window.mainloop()