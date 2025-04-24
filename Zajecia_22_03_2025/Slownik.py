słownik={1:1,
         2:2.5,
         3:3.9,
         4:4,
         5:4.3,
         6:4.5}

#for key, values in  słownik.keys().value():
for key, values in  słownik.items():
#for value in  słownik.values():
   # if #values==int(values):#
    if isinstance(values, int):
        słownik[key]=values**2
    else:
         słownik[key] = values
print(słownik)

 #   if value==int(value):
  #      value=value**2
 #   else:
 #       value=value
#print(słownik)

#for value in  słownik.values():
  #  if value%2 ==0:
  ##  else:
   #     value=value
#print(słownik) 

