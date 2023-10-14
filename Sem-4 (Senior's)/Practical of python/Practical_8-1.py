class Employee:
    
    def __init__(self , name, department, salary):
            self.name = name
            self.department = department
            self.salary = salary
        
    def dispalyDetails(self):
        print("name", self.name,"Department",self.department,"Salary",self.salary)
e1 = Employee("Vandan","CE",50000)
e2 = Employee("Jaydip","IT",45000)
e3 = Employee("Keval","IT",45000)

e1.dispalyDetails()
e2.dispalyDetails()
e3.dispalyDetails()



