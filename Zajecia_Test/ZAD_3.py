import random
i=0
kolory=['czerowny','zielony', 'niebieski', 'różowy', 'fioletowy'] 
imiona=['Ania', 'Ola', 'Ela', 'Ula', 'Emma','Alex']

goscie=int(input('podaj liczbe gości od 1 do 5 '))
ListaGości= {}
#print(type(ListaGości))

for i in range(0,goscie+1):
     j=random.randint(0,goscie+1)
     print(j)
     ListaGości.update({kolory[j]:imiona[j]})

     ##print(nowy_slownik) 
print(ListaGości)

##nowy_slownik = {klucz:wartosc for (kolor,imiona) in slownik.items()} 
##print(nowy_slownik) 

##nowy_slownik = {klucz:wartosc for (klucz,wartosc) in slownik.items()} 
##print(nowy_slownik) 