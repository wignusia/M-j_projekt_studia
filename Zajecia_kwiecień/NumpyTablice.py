import numpy as np
#shape ilośc kolumn 
#(wymiar wierszy, kolumna)

tablica_ilosc=np.array([1,2,358,9566,444,56,3,99,65,5])
print(tablica_ilosc)
zmian_wymiaru=tablica_ilosc.reshape(5,-1)

print(zmian_wymiaru)

#Maskowanie danych
tablica = np.arange(1,20,2).reshape(2,5)
print(tablica)
masak = tablica>10
zamskowanie =np.ma.masked_where(masak,tablica)
print(zamskowanie)

#Pliki
np.savetxt('plikuś3.cvs',tablica(),delimiter='0')