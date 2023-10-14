class exp:
    def __init__(self,a):
        self.a = a
    def __pow__(self,o):
        return self.a **o.a
ob1 =exp(1)
ob2 = exp(2)

print(ob1 ** ob2)