#3.	Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
n = int(input("Enter number:"))

l1 = []
for i in range(1,n):
    if(n % i == 0):
        l1.append(i)

        print(f"Divisor of number {n} is {l1}")
#Hello World
