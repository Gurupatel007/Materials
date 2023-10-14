class Person: 
 def __init__(self,name,age): 
  self.name=name 
  self.age=age 
class SpotPerson(Person): 
 def __init__(self,name,age,sports_name): 
  
  super().__init__(name,age) 
  self.sports_name=sports_name 
 
 def print(self): 
  print(self.name,self.age,self.sports_name) 
x=SpotPerson("Vandan Patel",50,"Cricket") 
print("Using Class Name") 
x.print()