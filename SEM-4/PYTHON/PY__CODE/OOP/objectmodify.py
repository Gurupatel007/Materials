class Employee:
    def __init__(self,a,b) -> None:
        self.name=a
        self.age=b
ob1=Employee("Aman",25)
ob1.age=40 #object property modified
print(ob1.age)
# deleting a object property
del ob1.age
print(ob1.age)
# deleting an object
del ob1
print(p1)