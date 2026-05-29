print(" Enter the integer number: ")
number = int(input())
list = []
for v in range(1, number + 1):
    list.append(v**2)
if list : print("List of numbers squares:", list)
