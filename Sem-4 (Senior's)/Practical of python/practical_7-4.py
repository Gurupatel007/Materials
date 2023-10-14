import csv 


with open('pr7_3.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Name", "Branch"])
    writer.writerow([1, "Vandan Patel", "CE"])
    writer.writerow([2, "Jaydip", "CE-IT"])
    writer.writerow([3,"Nill Patel","CE"])
    writer.writerow([4,"Keval Vasoyia","CE-IT"])
    writer.writerow([5,"Vansh Patel","diploma"])

with open('Players.csv','w',newline= '') as file1:
    fieldnames = ['Players_name','Players_rating']
    writer = csv.DictWriter(file1, fieldnames=fieldnames)

    writer.writeheader() 
    writer.writerow({'Players_name': 'Dhoni','Players_rating': 10})
    writer.writerow({'Players_name': 'Virat Kholi','Players_rating': 8})
    writer.writerow({'Players_name': 'Rohit Sharma','Players_rating': 9})
    writer.writerow({'Player_name': 'Hardik Pandya','Players_rating': 7})





