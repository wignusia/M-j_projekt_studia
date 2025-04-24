import numpy as np
tab =np.arange(20)
print(tab)
tab[tab%2==1]=-1
print(tab)


tab1=np.array([0,1,2,3,4,5,6,7,8,9])
tab2=np.array([3,1,13,1557,92,0,6,80,43,9])

tab3=np.where(tab1 == tab2)

print(tab3)