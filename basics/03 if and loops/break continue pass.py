data = [0,1,2,3,4,5]

for num in data:
    if num == 3:
        break
    print(num)

for num in data:
    if num == 3 or num == 5:
        continue
    print(num)

for num in data:
    if num == 3:
        pass
    print(num)  

