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



'''#void dunction

def jagga(a):
    if a<0:
        return "try with other"
    if a%2==0:
        return "even"
    else:
        return "odd"
b=jagga(-2)
print(b)
#fruitful

def jagga(a):
    if a<0:
        return "try with other"
    if a%2==0:
        return "even"
    else:
        return "odd"
b=jagga(2)
print(b)'''



#recursive function

def fact1(n):
    fact=1
    if n==1:
        return 1
    else:
        for i in range(1,n+1):
            fact=fact*i
        return fact
        
print(fact1(4))    



#fruitful function

'''def sum1(radius):
    #a=3.14*raduis*radius
    #return a
       #or
    pi=3.14
    return pi*radius*radius
b=sum1(3)
print(b)'''

'''#area of rect
def  sum1(a,b):

   return a*b
b=sum1(2,5)
print(b)'''

'''#area of triangle
def sum1(a,b):
   return 0.5*a*b
b=sum1(1,2)
print(b)
'''

'''#condional loop
def jagga(a):
    if a<0:
        return "try with other"
    if a%2==0:
        return "even"
    else:
        return "odd"
b=jagga(2)
print(b)'''







