number = 5
adrrNum = id(number)
print(adrrNum)
number += 2
addrNum2 = id(number)
print(addrNum2)
fruit = ["apple", "banana", "cherry"]
addrList = id(fruit)
print(addrList)
fruit.append("orange")
addrList2 = id(fruit)
print(addrList2)
