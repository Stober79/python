#immutabel: int, float, bool, str, tuple, frozenset
a=1
addr1= id(a)
a +=1
addr2= id(a)
print(addr1)
print(addr2) 

#mutabel: list, set, dict
my_list = [1, 2, 3]
addr1 = id(my_list)
my_list.append(4)
addr2 = id(my_list)
print(addr1)
print(addr2)