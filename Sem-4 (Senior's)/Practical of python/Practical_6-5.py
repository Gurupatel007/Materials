l1 = [12,54,89,15,54,78,45,31,15,94,31,13]
l2 = [21,65,34,98,76,34,94,31,13,74,35,64]
l3 =[]
def listAdd(l1,l2,l3):
    for i in range(len(l1)):
        l=l1[i]+l2[i]
        l3.append(i)
listAdd(l1,l2,l3)
print("List 1:",l1)
print("List 2:",l2)
print("List 1+2 :",l3)