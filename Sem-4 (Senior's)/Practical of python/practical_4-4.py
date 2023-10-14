l2 = [45,12,78,32,54,99]
l3 = l2
l3.sort()
print("List of l3:",l3)
my_list= [12,321,98,-78,67,94]
new_list = []
while my_list:
    min = my_list[0]
    for x in my_list:
        if x < min:
            min = x
    new_list.append(min)
    my_list.remove(min)
print(new_list)


