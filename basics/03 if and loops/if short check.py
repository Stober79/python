flag = True

if flag == True:
    print("Flag is true")

if flag is True:
    print("Flag is true")

# The above code is correct, but it can be simplified to:
if flag:
    print("Flag is true")

flag = False

if flag != True:
    print("Flag is not true")

if flag == False:
    print("Flag is not true")

if flag is not True:
    print("Flag is not true")

# The above code is correct, but it can be simplified to:
if not flag:
    print("Flag is not true")