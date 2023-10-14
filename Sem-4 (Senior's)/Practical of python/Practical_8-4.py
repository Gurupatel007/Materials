class Hospital: 
 def __init__(self,pat_no,pat_name,dis_name): 
  self.pat_no=pat_no 
  self.pat_name=pat_name 
  self.dis_name=dis_name 
p1=Hospital(130,"Vandan Patel","Corana") 

print(getattr(p1,'pat_name')) 


 
setattr(p1,'pat_no',125) 
 
print(hasattr(p1,'pat_name')) 
print(Hospital.__dict__) 
print(Hospital.__doc__) 
print(Hospital.__name__) 
print(Hospital.__module__) 
print(Hospital.__bases__) 
print("Patel Vandan") 