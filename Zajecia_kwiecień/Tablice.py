import numpy as np
tablica=np.array([1,2,358,9566,444,56,3,99,65,5])
NieparzytsTabkica=np.where(tablica%2 == 0)

print(NieparzytsTabkica)

for elemnt in np.nditer(tablica):
     print(elemnt)
     if elemnt%2 != 0:
          elemnt = -1
     else:
          elemnt = elemnt
print(tablica)


tab =np.arange(20)
tab[tab%2==1]=-1
print(tab)
#NieparzytsTabkica=np.where(tablica%2 == 0)