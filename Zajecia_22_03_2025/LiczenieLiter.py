
słowo = input('Podaj słowo: ')  # Pamiętaj o poprawnym użyciu zmiennej
słownik = {}

for i in słowo:
    print(i)
    if i in słownik:
        słownik[i] += 1
    else:
        słownik[i] = 1

print(słownik)
