#direct method
'''for i in range(1,8):
       print(i*"*")
       i=i-1'''

#print forward
'''n=int(input("enter value:"))
for i in range(1,n+1):
    for j in range(i):
       print("*",end="")
    print()
'''
'''#reversing pattern
n=int(input("enter value:"))
for i in range(n,0,-1):
    for j in range(i):
       print("*",end="")

    print()'''

#piramid
'''n=int(input("enter value:"))
for i in range(n):
    for j in range(n-i-1):
        print('  ',end="")
    for j in range(2*i+1):
        print('*',end="")
    print( )'''


'''n=int(input("enter value:"))
for i in range(n):
    for j in range(n-i-1):
        print('  ',end="")
    for j in range(2*i+1):
        a=chr(65+i)
        a=chr(97+i)
        print('',end=" ")
    print( )'''

'''
n=int(input("enter value:"))
for i in range(n):
    for j in range(n-i-1):
        print('  ',end="")
    for j in range(2*i+1):
        print(j,end="")
    print( )'''


            

    
    
