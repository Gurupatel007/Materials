f1 = open("h1.txt","r")

x = f1.read()
l1 = x.split()

l = len(max(l1,key=len))
for i in l1:
    if(len(i)==l):
        print(i)