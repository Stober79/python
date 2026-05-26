firstName = "John"
lastName = "Doe"
fullName = firstName + " " + lastName
print(fullName)  # Output: John Doe
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combinedList = list1 + list2
print(combinedList)  # Output: [1, 2, 3, 4, 5, 6]
if len(combinedList) >5:
    print("The list is long")
else:
    print("The list is short")

greeting = "Hello, " + fullName + "!"

if "Hello" in greeting:
    print("The greeting contains Hello.")
    print(greeting) 