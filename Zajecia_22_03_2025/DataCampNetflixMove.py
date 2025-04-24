x=input('Ile masz wzrostu ?: ')
wzrost= float(x)

if wzrost> 170 :
    print('Przykromi jesteś za wysoki na Dzokeja')
elif  wzrost <140:
     print('Przykromi jesteś za niski na Dzokeja')
else:
     print('Brawo możesz być  Dzokeja')


i=1
for i in range(50):
    print(i)
    if i%2 ==0:
        print('liczba jest parzysta')
    else :
        print('iczba jest nie parzysta')


while i< 51:
    print(i)
    i=i +1
    