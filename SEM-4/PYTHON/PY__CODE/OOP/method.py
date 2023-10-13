class Employee:
    def __init__(self,a,b) -> None:
        self.id=a
        self.name=b
    def Display(self):
        print("Id=%s and Name=%s"%(self.id,self.name))

ob1=Employee(74,"Guru")
ob1.Display()
