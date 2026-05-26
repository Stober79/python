list = [0, 1, 2, 3, 4, 5, 6]
print(len(list))
del list[1]
print(len(list))
if 3 in list:
    print("3 jest w liście")
for v in list:
    print('Element listy plus 2 to:', v + 2)
for w in list:
    print(w*2)
