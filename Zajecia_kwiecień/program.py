# Funkcja do liczenia sumy cyfr
def suma_cyfr(liczba):
    suma = 0
    while liczba > 0:
        suma += liczba % 10  # Dodaj ostatnią cyfrę liczby
        liczba //= 10         # Usuń ostatnią cyfrę z liczby
    return suma

# Przykładowe użycie
liczba = int(input("Podaj liczbę: "))
wynik = suma_cyfr(liczba)
print(f"Suma cyfr liczby {liczba} to: {wynik}")
