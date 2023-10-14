print("20012011130_Patel Vandan")
st = input("Enter statement:")
upper,lower,digit,special=0,0,0,0
for i in st:
    if(i>='A' and i<='Z'):
        upper+=1
    elif(i>='a' and i<='z'):
        lower+=1
    elif(i>='0' and i<='9'):
        digit+=1
    else:
        special+=1
print("Uperercase count=",upper)
print("Lowercase count=",lower)
print("diditcase count=",digit)
print("specialcase count=",special)
