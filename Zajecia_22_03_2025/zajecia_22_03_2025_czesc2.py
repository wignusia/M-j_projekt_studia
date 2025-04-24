słowo='rabarbar'
sumR=0
sumA=0
sumB=0
liczbaliter=int(len(słowo))
print(liczbaliter)
for i in słowo:
    if i=='r':
        sumR+=1
    elif i=='a':
        sumA+=1
    else:
        sumB+=1
print ('Suma R:',sumR)
print ('Suma A:',sumA)
print ('Suma B:',sumB)