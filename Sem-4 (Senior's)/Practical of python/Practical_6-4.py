
test_list = [(2, 3), (4, 7), (8, 11), (3, 6)]


print ("The original list is : " + str(test_list))


res1 = min(test_list)[0], max(test_list)[0]
res2 = min(test_list)[1], max(test_list)[1]


print ("The min and max of index 1 : " + str(res1))
print ("The min and max of index 2 : " + str(res2))
