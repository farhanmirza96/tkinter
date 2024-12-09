from customtkinter import *
from PIL import Image
from tkinter import ttk, messagebox
import database as db


def treeview_data():
    employees = db.fetch_employees()
    for employee in employees:
        tree.insert('', END, values = employee)
    
def add_employee():
    if idEntry.get()=='' or nameEntry.get()=='' or phoneEntry.get()=='' or salaryEntry.get()=='':
        messagebox.showerror('Alert', 'All feild are required')
    elif db.id_exists(idEntry.get()):
        messagebox.showerror('Alert', 'Employee ID already exists')
    else:
        db.insert(idEntry.get(), nameEntry.get(), phoneEntry.get(), roleCombo.get(), genderCombo.get(), salaryEntry.get())
        def treeview_data():
            messagebox.showinfo('Success', 'Employee added successfully')

window = CTk()
window.geometry('950x580+100+100')   # Here 100 is the x position and 100 is the y position of the window to apear on the screen
window.resizable(0,0)

window.title('Employee Management System')

window.configure(fg_color = '#161c30')

image = CTkImage(Image.open('employee.jpg'), size=(950,158))
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
rightFrame.grid(row=1, column=1, pady= 5)

search_options = ['ID', 'Employee Name', 'Phone', 'Role', 'Gender', 'Salary']
searchCombo = CTkComboBox(rightFrame, width=140, font=('garamond',15), values=search_options, corner_radius=0, state='readonly')
searchCombo.set('Search By')
searchCombo.grid(row=0, column=0, sticky='W')

searchEntry = CTkEntry(rightFrame,width=140,height=28, corner_radius=0,border_width=2,bg_color='white',placeholder_text='Enter your Salary.',font=('garamond',15,))
searchEntry.grid(row=0, column=1, sticky='W')

searchButton = CTkButton(rightFrame, text='Search', width=100)
searchButton.grid(row=0, column=2)

showAllBtn = CTkButton(rightFrame, text='Show All', width=100)
showAllBtn.grid(row=0, column=3, pady=5)

tree = ttk.Treeview(rightFrame, height=13)
tree.grid(row=1, column=0, columnspan=4)

tree['columns'] = ('Id', 'Name', 'Phone', 'Role', 'Gender', 'Salary')
tree.heading('Id', text='Id')
tree.heading('Name', text='Name')
tree.heading('Phone', text='Phone')
tree.heading('Role', text='Role')
tree.heading('Gender', text='Gender')
tree.heading('Salary', text='Salary')

tree.config(show='headings')   # it will show only headings not the first column by default

tree.column('Id', anchor='center', width=50)   # dy default anchor is in center
tree.column('Name', width=150)
tree.column('Phone', width=100)
tree.column('Role', width=110)
tree.column('Gender', width=100)
tree.column('Salary', width=100)

style = ttk.Style()
style.configure("Treeview", font=('arial',18,'bold'))

scrollbar = ttk.Scrollbar(rightFrame, orient=VERTICAL)
scrollbar.grid(row=1, column=4, sticky='ns')

btnFrame = CTkFrame(window, fg_color = '#161c30')
btnFrame.grid(row=2, column=0, columnspan=2, pady=5)

newbtn = CTkButton(btnFrame, text='New Employee', width=160, font=('arial',18,'bold'), corner_radius=15)
newbtn.grid(row=0, column=0, pady=5)

addbtn = CTkButton(btnFrame, text='Add Employee', width=160, font=('arial',18,'bold'), corner_radius=15, command=add_employee)
addbtn.grid(row=0, column=1, padx=5, pady=5)

updatebtn = CTkButton(btnFrame, text='Update', width=160, font=('arial',18,'bold'), corner_radius=15)
updatebtn.grid(row=0, column=2, padx=5, pady=5)

deletebtn = CTkButton(btnFrame, text='Delete', width=160, font=('arial',18,'bold'), corner_radius=15)
deletebtn.grid(row=0, column=3, padx=5, pady=5)

deleteAllbtn = CTkButton(btnFrame, text='Delete', width=160, font=('arial',18,'bold'), corner_radius=15)
deleteAllbtn.grid(row=0, column=4, padx=5, pady=5)

window.mainloop()