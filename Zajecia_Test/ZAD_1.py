#import nampy as np
import random
tablica=[]
i =1
LiczbaWiekszOd05= 0
print(tablica)

for i in range(0,20):
    tablica.append(random.random())

print(tablica)

for x in  tablica:
     if x > 0.5:
          LiczbaWiekszOd05 +=1
 
print('Liczby większe niż 0.5 jest: ',str(LiczbaWiekszOd05))

