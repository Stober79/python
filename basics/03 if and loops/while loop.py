number =5
while number>0:
    print(number)
    number -=1

number = 1
while number <6:
    print(number)
    number +=1

num = 0
while True:
    print ( "Enter a number (exit to quit): " )
    strData = input()
    if strData == "exit" : break
    num +=int(strData)
    print ( "The total is: " + str(num) )


number = 3
while number > 0:
    print(number)
    number -= 1
else:    print("The loop is over")
