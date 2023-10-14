class Reptile: 
 def crawl(): 
  pass 
 def string(): 
  pass 
class python(Reptile): 
 def crawl(): 
   pass 
 def string(): 
  pass 
class snake(Reptile): 
 def crawl(): 
  pass 
 def string(): 
  pass 
print(issubclass(python, Reptile)) 
print(isinstance(snake(), Reptile))