r=6
unit=300
n=8
sum=0
s=0
t=r*unit
print(t)
arr=[200,400,1200,150,100,300,450,300]
if len(arr)==0:
    print("-1")
for i in range(n):
    sum=sum+arr[i]
if sum<t:
    print("0")
for i in range(n):
    s=s+arr[i]
    if s>=t:
       print(i+1)
       break

'''def find_houses(r,units,arr):
    if len(arr)==0:
        return -1
    food=r*units
    f=0
    for i,fd in enumerate(arr):
        f=f+fd
        if f>=food:
            return i+1
    return 0
r=int(input("rats:"))
units=int(input("units:"))
arr=[2,6,3,9,6]
print(find_houses(r,units,arr))

    
'''
