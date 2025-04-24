
list =[]
y =-100000
x = float(input('podaj liczbe: '))

while x >=y:
    print(x)
    list= list+[x]
    y=x +0
    #print('to jest nowy Y :', y)
    x = float(input('podaj liczbe: '))
print(list)

