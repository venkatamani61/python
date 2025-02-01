'''
#lambda function
a= lambda x,y : x*y
b=lambda x,y:x/y
c=lambda x,y:x-y
d=lambda x,y:x+y
e=lambda x,y:x%y
print(a(2,5))
print(b(10,5))
print(c(10,5))
print(d(10,5))
print(e(10,5))'''

'''
a= lambda x,y : x*y
b=lambda x,y:x/y if y!=0 else 'can not devide'
print(b(4,0))

a= lambda x,y,z : x*z
b=lambda x,z,y:x/z if y!=0 else 'can not devide'
print(b(4,0))'''

'''#list
a=[1,2,3,4,5]
b=list(map(lambda x:x**2,a))
print(b)

#string
a=["hiii","hello","jagga"]
b=list(map(lambda x:len(x),a))
print(b)'''

'''#powers
a=[2,4,3,5,6]
b=list(map((lambda x:x**2),a))
print(b)

#module
a=[2,4,6,8,10]
c=[1,2,3,4,5]
b=list(map(lambda x,y:x%y,a,c))
print(b)'''


