with open("h1.txt","r") as f1:
    with open("demo.txt","r") as f2:
        x=f1.readlines()
        y=f2.readlines()
        m=min(len(x),len(y))
for i in range(m):
 z=x[i].strip()+" "+y[i].strip()
 print(z)



f1 = open ("h1.txt","r")
f2 = open ("demo.txt","r")
for i,j in zip(f1,f2):
     print(i+j)
f1.close
f2.close