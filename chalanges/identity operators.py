text = "Hello"
print(dir(text))  # List of all attributes and methods of the string object
print(text.upper())  # Convert the string to uppercase
x= 256
u =256
print(x is u)  # True, small integers are cached by Python
listOne = [1, 2, 3]
listTwo = listOne
print(listOne is listTwo)  # True, both variables point to the same list object
listOne.append(4)
print(listTwo)  # [1, 2, 3, 4], list
if listOne is listTwo:
    print("listOne and listTwo are the same object")
else:
    print("listOne and listTwo are different objects")

listThree = [1, 2, 3, 4]
if listOne is listThree:
    print("listOne and listThree are the same object")  
else:
    print("listOne and listThree are different objects")  # True, listOne and listThree are different objects