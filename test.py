subjects: dict = {}
sub= 1

while sub < 4:
    for i in range(subjects):
        key: str = input(f"Enter the name of subjects {sub}: ")
        value: int = input(f"Enter the marks of subjects {sub}: ")
    # if subjects_marks != type(int):
    #     subjects_marks: int = input(f"Enter the marks of subjects {sub}: ")
    # else:
    subjects.update({key: value})
    sub+=1

class Student:
    def __init__(self, names, subjects) -> None:
        self.names = names
        self.subjects = subjects

s1 = Student(subjects)
print(s1.names, s1.subjects)