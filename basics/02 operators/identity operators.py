strData = "test"

print(dir(strData))  

print( strData.upper() )

a = [1,2,3,4,5]
b = a
print(a is b)  # True

a.append(6)
print(b)  # [1, 2, 3, 4, 5, 6]
c=[1,2,3]
print(a is c)  # False
print(a is not c)  # True