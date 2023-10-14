from turtle import update

#1
# d1  = {"a":1,"b":2,"c":3,"d":4}
# print(d1["a"])
# print(d1["b"])
# print(d1["c"])
# print(d1["d"])

# #2
# d2  = {"a":1,"b":2,"c":3,"d":4}
# sum = 0
# for i in d2:
#     sum = sum + d2[i]
# print("Sum=",sum)

# 3
d1  = {"a":1,"b":2,"c":3,"d":4}
d1.update({'e':5})
print(d1)
d1.update([('e',6)])
print(d1)