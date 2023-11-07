s = set()
print(type(s))
s_from_list = set([1,2,3,4])

""""line no 3 and 4 are same using set as multiple in line 3 or
    make a seperate set then print it as line in 5"""
#s_from_list = {1,2,3,4}

print(s_from_list)
print(type(s_from_list))
print(max(s_from_list))
s_from_list.add(5)
print(s_from_list)
print(max(s_from_list))


p = {1}
q = {1,2,3}
print(p|q)
r = p.intersection(q)
print(r)
p1 = p.union({5})
p2 = p.intersection({1,2,3})
print(p1)
print(p2)
print(p.isdisjoint(p1))
print(p.isdisjoint(q))

p2 = p.remove(1)
print(p2)