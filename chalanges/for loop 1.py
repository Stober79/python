listData = [-3, -2, -1, 0, 1, 2, 3]
setData = {-1}
for el in listData:
    if el%2 != 0:
        setData.add(el)

for v in setData:
    print(v)