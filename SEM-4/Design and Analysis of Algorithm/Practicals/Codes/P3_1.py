print("hello")
class shape:
    def vol(self,a):
        self.a=a
        return(self.a ** 3)
s1=shape()
Vol=s1.vol(4)
print(Vol)