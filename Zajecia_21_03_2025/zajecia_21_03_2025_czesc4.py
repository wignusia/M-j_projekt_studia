year=int(input('Podaj rok '))
if (year%4 == 0 and  year%100 != 0)or  (year % 400 == 0):
     print('Rok jest przestępny')
else:    
    print('Rok jest zwykły')
