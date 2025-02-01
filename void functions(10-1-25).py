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


