'''a={'apple','banana','orange'}
b={1,2,3}
c=dict(zip(a,b))
print(c)
d=c.get(1)
print(d)
a={1:"one",2:"two"}
a[1]="ONE"
a[2]="TWO's"
print(a)
b=a.keys()
print(b)
c=a.values()
print(c)

#adding key and values
a[3]="Three"
print(a)
a[4]="four"
print(a)
#pop
a.pop(1)
print(a)

#a.pop(1)
#print(a)
#in operator
print(2 in a)
print('two' in a)

#from keys
a={1,2,3,4,5,6,7}
b='team'
c=dict.fromkeys(a,b)
print(c)

a={1,2,3,4,5,6,7}
b={'team','mem'}
c=dict.fromkeys(a,b)
print(c)
c[1]='members'
print(c)
#setdefault
c.setdefault(5,'hi')
print(c)

c.setdefault(8,'hello')
print(c)

#items(access particular dictionary)
print(c.items())
#clear
c.clear()
print(c)

#dict comprehension           
a={x:x**2 for x in range(21) if x%2==0}
print(a)

#merge two dict
a={1:'a',2:'b',3:'c'}
b={4:'e',5:'f',6:'m'}
a.update(b)
print(a)

m=["jagga","mani","koti"]
j={name:len(name) for name in m}
print(j)'''

 

names=['jagga','jay','mani']
a={names:len(names) for names in names}     
print(a)


def hello(x):
    double=x*2
    print(double)
hello(2)    













