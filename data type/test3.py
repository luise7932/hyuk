s1 = set([1,2,3])
print(s1)

l1 = list(s1)
print(l1)

s2 = set([3,4,5])
print(s1&s2)
print(s1|s2)
print(s1-s2)

s1.update([4,5,6])
s1.add(7)
print(s1)