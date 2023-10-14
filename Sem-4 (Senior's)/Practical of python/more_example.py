class Employee:
    Emp_compony_name = 'IBM'    
    Emp_age = 20
    defult_age=50

    def defultMethod(self):
        print("This is a defult method")
e=Employee()
print(getattr(e,'emp_age',30))
print(getattr(e,'emp_age_other',35))
print(getattr(e,'emp_age_other',e.defult_age))