class Student:
    def __init__(self,a,b,c) -> None:
        self.id=a
        self.name=b
        self.age=c
ob1=Student(63,"Aman",20)

print(getattr(ob1,'name'))
setattr(ob1,'age',19)
print(getattr(ob1,'age'))
print(hasattr(ob1,'id'))
delattr(ob1,'age')
print(getattr(ob1,'age'))
