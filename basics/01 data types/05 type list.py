list = ["Ola", "Abua", 23, 99 , "Rafał"]
print(type(list))
print(list)
print(len(list))
print(list[4])
print(list[len(list)-1])
print(list[-1]) # ujemne indeksy liczą od końca listy, więc -1 to ostatni element, -2 to przedostatni itd.
print(list[0:3]) # slicing - wyświetla elementy od indeksu 0 do 2 (3 nie jest wliczane)
print(list[2:4]) # slicing - wyświetla elementy od indeksu 2 do 3 (4 nie jest wliczane)
print(list[::2]) # slicing - wyświetla elementy od początku listy co drugi element
list[0] = "Kasia" # zmiana wartości elementu o indeksie 0
print(list)
del list[1] # usunięcie elementu o indeksie 1
print(list)
list.append("Nowy element") # dodanie nowego elementu na końcu listy
print(list)
print(99 in list) # sprawdzenie, czy 99 jest w liście
print("Ola" in list) # sprawdzenie, czy "Ola" jest
print("Rafał" in list) # sprawdzenie, czy "Rafał" jest
if "Rafał" in list:
    print("Rafał jest w liście")

for v in list:
    print(v)
data = [["Daniel", 23], ["Kasia", 30], ["Rafał", 25]]
print(len(data))
print(data[1][0])    # wyświetla element o indeksie 1, czyli ["Kasia", 30], a następnie element o indeksie 0, czyli "Kasia"
data1 = [1, 2, 3]
data2 = [4, 5, 6]   
numbers = data1 + data2 # łączenie dwóch list
print(numbers)   
numbersX2 = numbers * 2 # powielanie listy
print(numbersX2) 