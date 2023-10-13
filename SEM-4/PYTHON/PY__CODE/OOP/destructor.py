class Employee:
    def __init__(self) -> None:
        print("Object initialized")
    def __del__(self):
        print("Object Deleted")
ob1=Employee()
del ob1
