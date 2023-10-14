# print("20012011130_Patel Vandan")
# st= "Hello,Good morning"
# sep=st.split(",")
# print(sep)
# x=[10,[3,141,20,[30,'technology',2.114],123],'computer']

#First internal Exam questions no 4
class cal():
    def __init__(self,a,b):
        self.a= a
        self.b=b
    def add(self):
        return self.a+self.b

a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))

obj = cal(a,b)

print("Answer is :",obj.add())