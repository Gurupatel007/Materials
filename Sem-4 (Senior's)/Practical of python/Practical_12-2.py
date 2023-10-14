from threading import * 
import time
class Myth1(Thread):
   def run(self):
      for i in range(5):
          time.sleep(0.5)
print("First Thread")
class Myth2(Thread):
     def run(self): 
        for i in range(5):
            time.sleep(0.5)
print("Other thread")
t1 = Myth1()
t2= Myth2()
t1.start() 
t2.start()
