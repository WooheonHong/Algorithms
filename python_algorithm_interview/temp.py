import copy

a = "사랑해"
b = a
c = a[:]
d = copy.deepcopy(a)

print(id(a), id(b), id(c), id(d))