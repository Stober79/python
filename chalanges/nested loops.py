nested_list = [
    [1,2,3], 
    ['a', 'b', 'c'],
    [True, False, None]
]

for inner_list in nested_list:
    for item in inner_list:
        print(item)