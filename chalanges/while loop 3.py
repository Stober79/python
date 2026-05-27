print("Enter number of elements to add:")
num = int(input())
sum = 0
if num > 0:
    i = num
    while i > 0 :
        print("Enter number:")
        n = float(input())
        sum += n
        i -= 1
    average = sum / num
    print("Average of numbers is:", average)
else: print("Number you entered is not greater than 0")
