print("20012011130_Patel Vandan")
num =int(input("Enter Number:"))
sum=0
for i in range(1,num):
    if(num % i == 0):
        sum = sum +i

if(num == sum):
    print(f"{num} is a special number")
else:
    print(f"{num} is a special not number")

