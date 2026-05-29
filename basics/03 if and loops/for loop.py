for v in  [1,2,3,4]:
    print(v*2)

for v in ("Ania", "Ola", "Kasia"):
    print(v.upper())

for v in {3,4,5, "Ola"}:
    print(v)

for v in "Hello":
    print(v)
else: print("No more letters")

dict = {"a":1, "b":2, "c":3}
for key in dict: # by default it iterates through keys
    print(key)

for key in dict.keys():# by default it iterates through keys
    print(key)

for key, value in dict.items(): # to get both key and value
    print(key, value)

for value in dict.values(): # to get only values
    print(value)