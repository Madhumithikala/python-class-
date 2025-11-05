eids={101,102,103}
uids=eids.copy()

print(eids)

print(uids)

eids.add(104)
print(eids)

eids.update({105,106,107})
print(eids)

eids={101, 102, 103, 104, 105, 106, 107}
eids.discard(105)
#remove specified element from set
#if element not  present it will return any error
print(eids)
