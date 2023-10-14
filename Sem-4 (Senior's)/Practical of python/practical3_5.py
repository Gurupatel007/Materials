print("20012011130_Patel Vandan")
num=int(input("Enter Number:"))
sum=0
temp=num
while(num>0):
   num1=num%10
   sum=sum+num1
   num=int(num/10)

print(f"Sum of the given number {temp} is {sum}")
