
### ZADANIE DWA FUNKCJA 
samogłoski=['a','e','i','o','y','u']
liczbaSamogłosek=0
liczbaSpolg=0

def policzSamSpó():
     liczbaSamogłosek=0
     liczbaSpolg=0
     zdanie=str(input('Prosze podaj mi dowolne zadnie : '))
     for i in zdanie:
          if i in samogłoski: #   if i in samogłoski:
               liczbaSamogłosek += 1
          
          else:
             liczbaSpolg +=1 
            
     print('liczba samogłosek to ',str(liczbaSamogłosek))
     print('liczba spółgłosek to ',str(liczbaSpolg))

policzSamSpó()

#print('liczba samogłosek to ',str(liczbaSamogłosek))
#print('liczba spółgłosek to ',str(liczbaSpółg))
