from tkinter import *
from tkinter import ttk
import pymysql

class Student():
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1378x780+0+0")
        
        # ******   Variables
        self.roll_no_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()

        title = Label(self.root,text="Student Management System", bd=9, relief=GROOVE, font=("times new roman", 50, "bold"), bg="yellow", fg="red")
        title.pack(side=TOP, fill=X)

        # ****************  Management Frame ************
        manage_frame = Frame(self.root, bd=4, relief=RIDGE, bg="light blue")
        manage_frame.place(x=20, y=100, width=450, height=585)

        m_title = Label(manage_frame, text="Manage student", bg="yellow", fg="black", font=("times new roman", 40, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)
        #  ******* Roll
        lbl_roll = Label(manage_frame, text="Roll No", textvariable=self.roll_no_var, bg="light blue", fg="black", font=("times new roman", 20, "bold"))
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

        combo_search = ttk.Combobox(detail_frame, font=("times new roman", 13, "bold"), width=10, state="readonly")
        combo_search['values'] = ("Roll No", "Name", "Contact")
        combo_search.grid(row=0, column=1, pady=10, padx=20)
        
        txt_search = Entry(detail_frame, font=("times new roman", 15, "bold"), width=20, bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20)
        
        search_btn = Button(detail_frame, text="Search", width=10, pady=5).grid(row=0, column=3, padx=10, pady=10)
        showall_btn = Button(detail_frame, text="Show All", width=10, pady=5).grid(row=0, column=4, padx=10, pady=10)
        
         # ****************  Table Frame ************
        table_frame = Frame(detail_frame, bd=4, relief=RIDGE, bg="crimson")
        table_frame.place(x=10, y=70, width=780, height=500)
        
        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)

        self.Student_table = ttk.Treeview(table_frame, columns=("Roll No", "Name", "Email", "Gender", "Contact No", "D.O.B", "Address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        
        self.Student_table.heading("Roll No", text="Roll No.")
        self.Student_table.heading("Name", text="Name.")
        self.Student_table.heading("Email", text="Email.")
        self.Student_table.heading("Gender", text="Gender")
        self.Student_table.heading("Contact No", text="Contact")
        self.Student_table.heading("D.O.B", text="DOB")
        self.Student_table.heading("Address", text="Address")
        
        self.Student_table["show"] = 'heading'
        self.Student_table.column('Roll No',width = 100)
        self.Student_table.column("Name", width = 100)
        self.Student_table.column("Email", width = 100)
        self.Student_table.column("Gender", width = 100)
        self.Student_table.column("Contact No", width = 100)
        self.Student_table.column("D.O.B", width = 100)
        self.Student_table.column("Address", width = 150)

        self.Student_table.pack(fill=BOTH, expand=1)
                                           
class Student():
    pass
    root = Tk()
    obj = Student(root)
    root.mainloop()