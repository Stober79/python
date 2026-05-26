print("Podaj liczbę: ")
number = float(input())
if number > 0:
    print(number, "jest dodatnia")
elif number < 0:
    print(number, "jest ujemna")
else:
    print(number, "jest równa zero")