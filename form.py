import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title("Data Entry Form")

# Creating file menue
menu = tkinter.Menu(window)
window.config(menu = menu)
filemenu = tkinter.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)

# creating help menu
helpmenu = tkinter.Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About")

# Creating frame inside main window
frame = tkinter.Frame(window)
frame.pack()

user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=15)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["","Mr.", "Mrs"])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=100)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values="")
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# saving course
courses_frame = tkinter.LabelFrame(frame, text="Registration Courses")
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=0)

registered_label = tkinter.Label(courses_frame, text="Registration Status")
registered_check = tkinter.Checkbutton(courses_frame, text="Currently Rigestered")
registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(courses_frame, text="# Registered Courses")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
numcourses_label.grid(row=0, column=1, padx=20, pady=0)
numcourses_spinbox.grid(row=1, column=1, padx=20, pady=0)

numsumister_label = tkinter.Label(courses_frame, text="# Sumister")
numsumister_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
numsumister_label.grid(row=0, column=2)
numsumister_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

terms_frams = tkinter.LabelFrame(frame, text="Terms & Condition.")
terms_frams.grid(row=2, column=0, sticky="news", padx=20, pady=5)

terms_check = tkinter.Checkbutton(terms_frams, text="I accept the terms and condition")
terms_check.grid(row=0, column=0)

window.mainloop()