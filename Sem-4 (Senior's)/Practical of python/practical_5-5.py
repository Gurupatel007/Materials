
d1={"War": [3,5],"Bourne": [18,5],"Gully boy": [15,5],"Uri":[12, 5]}
movie =input("enter a movie name :")
if movie in d1.keys():
     print ("{} movie is available".format(movie))
     tkt=int(input("enter a number of tickets you want to buy : "))
     if(d1[movie][1]>tkt):
        print("tickets are available")
        age=int(input("enter the age of youngest person in your group : "))
        if(age>d1[movie][0]):
            print("you are successfully buy tickets")
        else:
            print("youngest person is too small for watch movie")
     else:
         print ("only {} tickets are availabel".formate(d1[movie][1]))
else:
   print("the movie is not avilabel") 
d1[movie][1]-=tkt
print ("{} tickets are remaining".format(d1[movie][1]))