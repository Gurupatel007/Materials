class Student:
    count=0
    def __init__(self,a) -> None:
        self.name=a
        print('instance variable=',self.name)
        Student.count+=1
    
ob1=Student("Guru")
ob2=Student("Aman")
print("No of students =",Student.count)