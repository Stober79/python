listData = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
for el in listData:
    if el == 0:
        print(f"{el} is zero")
    elif el%2 == 0:
        print(f"{el} is even")
    elif el%2 != 0:
        print(f"{el} is odd")
    