listData = [1,2,3,4,5,6,7,8,9,10]
for num in listData:
    if num%2 == 0:
        continue
    elif num>8:
        break
    else:
        print(num**2)