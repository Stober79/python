print(" Enter the integer number: ")
number = int(input())
listOdd = []
listEven = []
for v in range(1, number + 1):
    if v % 2 == 0:
        listEven.append(v)
    else:
        listOdd.append(v)
print("List of odd numbers from 1 to", number, ":", listOdd)
print("List of even numbers from 1 to", number, ":", listEven)