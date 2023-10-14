class Student:
    count =0
    def __init__(self):
        Student.count += 1
    def get_values(self,enrollment_no,name,branch):
        self.enrollment_no = enrollment_no
        self.name = name
        self.branch = branch
    def print_value(self):
        print("Enrollment_no",self.enrollment_no,"Name",self.name,"Branch",self.branch)

    @staticmethod
    def display1():
            print("Total instance created = ",Student.count)

S1 = Student()
S1.get_values(130,"Vandan Patel","CE")
S1.print_value()
s2 = Student()
s3 = Student()
s4 = Student()
Student.display1()




