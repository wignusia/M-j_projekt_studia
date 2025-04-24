plik=open('pliczek1.txt','a')
zawarosc=str(input('podaj zartosci pliku'))
if plik.writable():
    plik.write (str(input('podaj zartosci pliku')))
else:
    print("Plik nie jest zapisowy.")

#plik.close()
#plik.
#print(plik)
plik.close()
#plik.write('jabłko jest dobre 3333')
#plik.close()
#print(plik.read())