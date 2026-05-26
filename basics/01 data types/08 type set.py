setData = {2,3,1,4,5}
setData.add(22)
setData.discard(1)
print(setData)
print (type(setData))
for v in setData:
    print(v)
setFrozenset = frozenset(setData)
print(setFrozenset)
print(type(setFrozenset))
#setFrozenset.add(33) # This will raise an error because frozenset is immutable
for v in  setFrozenset:
    print(v)