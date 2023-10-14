l1 = [10,54,21,34,61,87,94]
l2 = [65,24,21,87,32,54,67,18,97]
l3 = []
for i in l2:
    if(i in l1 and i not in l3):
        l3.append(i)
print(l3)