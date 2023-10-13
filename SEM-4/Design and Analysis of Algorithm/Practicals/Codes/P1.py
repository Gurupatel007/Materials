# -*- coding: utf-8 -*-
# Question1
global count_loop
global count_equ

def func_loop(n):
    count_loop=0
    sum=0
    count_loop+=1
    for i in range(1,n+1):
        sum=sum+i
        count_loop+=1
    print("Sum:",sum)
    print("Count:",count_loop)
        
def func_equ(n):
    count_equ=0
    sum=0
    count_equ+=1
    sum=(n*(n+1))//2
    count_equ+=1
    print("Sum:",sum)
    print("Count:",count_equ)

def func_rec(n):
    global Count_recu
    if(n==1):
        Count_recu+=1
        return 1
    else:
        Count_recu+=1
        return (n)+(func_rec(n-1))
        
        
    
n=int(input("Enter the Number"))
func_loop(n)
func_equ(n)
Count_recu=0
add=func_rec(n)
print("Sum:",add)
print("count",Count_recu)