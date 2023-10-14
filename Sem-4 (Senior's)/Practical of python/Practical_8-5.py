class Lion: 
 def __init__(self,legs,ears,name): 
  self.legs=legs 
  self._ears=ears 
  self.__name=name 
 def roar(self): 
  print("Loud Roar") 
class Cub(Lion): 
 def __init__(self, legs, ears, name): 
  super().__init__(legs, ears, name) 
 def play(self): 
  print("Love Playing") 
c=Cub(3, 2, 'x') 
c.play() 
c.roar() 

print(c.legs) 
print(c._ears) 
print("Vandan Patel")