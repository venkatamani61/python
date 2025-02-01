#list methods:append(),extend(),insert(i,a),pop(),del [i],
#set methods:.add(),a.update(b),a.re

a={1}
print(type(a))
a.add(2)
print(a)
a.add(9)
print(a)
a.add(8)
a.add(10)
print(a)
a.add("hii")
print(a)
#a={3,7,9}
b={1,2,3,4,5}
b.update(a)
print(b)
a.remove(10)
print(a)
a.remove(2)
print(a)
a.discard(2)
print(a)

#copy
a={2,3,4,5,6}
b=a.copy()
print(b)
#clear
b={4,6,7,8,9}
b.clear()
print(b)


a={1,2,3,4,5,6,7,8,9,0}
b={2,4,6,8,10}
c={1,3,5,7,9}
m=b.issubset(a)
print(m)
n=c.issubset(a)
print(n)
p=b.issubset(b)
print(p)

#disjoint
j=b.isdisjoint(c)
print(j)



#set operations
a={2,4,6,8,10}
b={1,3,5,7,9}
c={1,2,3,4,5,6,7,8,9,10}

#union
m=a|b
print(m)
n=a.union(b)
print(n)

#intersection
k=a&b
print(k)
#difference
t=(a-b)
print(t)

#simantic difference
h=(a^c)
b=a.symmetric_difference(c)
print(h)
print(b)


