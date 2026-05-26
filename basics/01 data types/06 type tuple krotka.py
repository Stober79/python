data = ("Ala", "Ola", "Kasia") # krotka - tuple
names = data + ("Rafał",) # dodanie elementu do krotki - trzeba dodać przecinek, żeby Python wiedział, że to jest krotka    
print(names)
print(len(names)) # wyświetla długość krotki
print(type(names)) # wyświetla typ danych - tuple
empty_tuple = () # pusta krotka
print(empty_tuple)
print(names[0]) # wyświetla pierwszy element krotki
print(names[-1]) # wyświetla ostatni element krotki
print(names[1:3]) # slicing - wyświetla elementy od indeksu
cars = (("Toyota", "Corolla"), ("Honda", "Civic"), ("Ford", "Focus")) # krotka zagnieżdżona - tuple w tuple
print(cars[0][0]) # wyświetla "Toyota"
if "Toyota" in cars[0]: # sprawdzenie, czy "Toyota" jest w pierwszej krotce
    print("Toyota jest w krotce")


del cars # usunięcie krotki - nie można usunąć pojedynczego elementu, ale można usunąć całą krotkę  
 #print(cars) # błąd, ponieważ krotka została usunięta