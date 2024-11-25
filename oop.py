names: str = []
s= 1
while s < 4:
    student_names: str = input(f"Enter the name of student {s}: ")
    
    names.append(student_names)
    s+=1

subjects: dict = {}
sub= 1

while sub < 4:
    subjects_names: str = input(f"Enter the name of subjects {sub}: ")
    subjects_marks: int = int(input(f"Enter the marks of {subjects_names}: "))
    # if subjects_marks != type(int):
    #     subjects_marks: int = input(f"Enter the marks of subjects {sub}: ")
    # else:
    subjects.update({subjects_names: subjects_marks})
    sub+=1

class Student:
    def __init__(self, names, subjects) -> None:
        self.names = names
        self.subjects = subjects

s1 = Student(names, subjects)
print(s1.names, s1.subjects)