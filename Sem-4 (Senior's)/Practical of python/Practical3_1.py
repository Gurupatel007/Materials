print("20012011130_Patel Vandan")
num=int(input("Enter Number:"))
sum=0
temp=num
while(num>0):
    num1 = num % 10
    sum = sum + num1 ** 3
    num = int(num / 10)

if(sum==temp):
    print(f"{temp} is an armstrong number.")
else:
    print(f"{temp} is an armstrong not number.")
