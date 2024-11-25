from tkinter import *
from tkinter import ttk

class Student():
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1378x780+0+0")

        title = Label(self.root,text="Student Management System", bd=9, relief=GROOVE, font=("times new roman", 50, "bold"), bg="yellow", fg="red")
        title.pack(side=TOP, fill=X)

        # ****************  Management Frame ************
        manage_frame = Frame(self.root, bd=4, relief=RIDGE, bg="light blue")
        manage_frame.place(x=20, y=100, width=450, height=585)

        m_title = Label(manage_frame, text="Manage student", bg="yellow", fg="black", font=("times new roman", 40, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)
        #  ******* Roll
        lbl_roll = Label(manage_frame, text="Roll No", bg="light blue", fg="black", font=("times new roman", 20, "bold"))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky=W)

        txt_roll = Entry(manage_frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_roll.grid(row=1, column=1, pady=10, padx=20, sticky=W)

        #  ******* Name
        lbl_name = Label(manage_frame, text="Name", bg="light blue", fg="black", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky=W)

        txt_name = Entry(manage_frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky=W)

        #  ******* Email
        lbl_email = Label(manage_frame, text="Email", bg="light blue", fg="black", font=("times new roman", 20, "bold"))
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky=W)

        txt_email = Entry(manage_frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky=W)

        #  ******  Gender
        lbl_gender = Label(manage_frame, text="Gender", bg="light blue", fg="black", font=("times new roman", 20, "bold"), bd=5)
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky=W)

        combo_gender = ttk.Combobox(manage_frame, font=("times new roman", 13, "bold"), state="readonly")
        combo_gender['values'] = ("Male", "Female")
        combo_gender.grid(row=4, column=1, pady=10, padx=20, sticky=W)

        #  ******* Contact
        lbl_contact = Label(manage_frame, text="Contact No", bg="light blue", fg="black", font=("times new roman", 20, "bold"))
        lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky=W)

        txt_contact = Entry(manage_frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_contact.grid(row=5, column=1, pady=10, padx=20, sticky=W)

        #  ******* DOB
        lbl_dob = Label(manage_frame, text="D.O.B", bg="light blue", fg="black", font=("times new roman", 20, "bold"))
        lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky=W)

        txt_dob = Entry(manage_frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_dob.grid(row=6, column=1, pady=10, padx=20, sticky=W)

        #  ******* Address
        lbl_address = Label(manage_frame, text="Address", bg="light blue", fg="black", font=("times new roman", 20, "bold"), bd=5)
        lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky=W)

        self.txt_address = Text(manage_frame, width=30, height=3, font=("times new roman", 10, "bold"))
        self.txt_address.grid(row=7, column=1, pady=10, padx=20, sticky=W)

        #  *********  Button frame
        btn_frame = Frame(manage_frame, bd=3, relief=RIDGE, bg="black")
        btn_frame.place(x=15, y=525, width=400)

        #  *********  Add Button
        add_btn = Button(btn_frame, text="Add", width=10).grid(row=0, column=0, padx=10, pady=10)
        update_btn = Button(btn_frame, text="Update", width=10).grid(row=0, column=1, padx=10, pady=10)
        delete_btn = Button(btn_frame, text="Delete", width=10).grid(row=0, column=2, padx=10, pady=10)
        clear_btn = Button(btn_frame, text="Clear", width=10).grid(row=0, column=3, padx=10, pady=10)

        # ****************  Detail Frame ************
        detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg="light blue")
        detail_frame.place(x=480, y=100, width=895, height=585)

        lbl_search = Label(detail_frame, text="Searched By", bg="light blue", fg="black", font=("times new roman", 20, "bold"), bd=5)
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky=W)


class Student():
    pass
    root = Tk()
    obj = Student(root)
    root.mainloop()