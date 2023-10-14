
n = int(input("Enter the number:"))
for i in range (1,n+1):
    temp =0
    for j in range(2,i-1):
        if(i%j==0):
            temp = 1
            break
    if(temp==0):
        print(i,end= " ")