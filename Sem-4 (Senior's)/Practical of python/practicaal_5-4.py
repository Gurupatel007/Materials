
d1={"male": ["Tom", "Charlie", "Harry", "Frank"],"female":["Sarah", "Huda", 
"Samantha", "Emily", "Elizabeth"] }
for i in d1.values():
      for j in i:
        if('a' in j):
           print(j)