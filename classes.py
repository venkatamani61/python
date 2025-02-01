
'''
class qis:
    name="Nani"
    print("hello,everyone!")
    print("this is ,",name)
    #pass
qis() '''


'''def fun(n):
    
    if n%2==0:
        print("even")
    else:
        print("odd")
m=int(input("enter number:"))
fun(m)'''


'''class qis:
    name="Nani"
    print("hello,everyone!")
    print("this is ,",name)
    #pass
    def fun(n):
    
      if n%2==0:
        print("even")
      else:
        print("odd")
#m=int(input("enter number:"))
#fun(m)
qis()
print(qis.fun(5))'''






'''class qis:
    name="Nani"
    print("hello,everyone!")
    print("this is ,",name)
    #pass
    def fun(name):
    
     print("this is ,",name)

qis()
qis.fun("mani")'''

#calculator
'''class calculator:
    def mul(m,n):
        print(m,"*",n,"=",m*n)
    def add(m,n):
        print(m,"+",n,"=",m+n)   
    def division(m,n):
        print(m,"/",n,"=",m/n)
    def modulo(m,n):
        print(m,"%",n,"=",m%n)

calculator()
calculator.mul(10,2)
calculator.add(10,2)
calculator.division(10,2)
calculator.modulo(10,2)'''




#self parameter:instance of current position
'''class qis:
    name="Nani"
    
    print("this is ,",name)
    #pass
    def fun(self):
     print("this is ,",self.name)
b=qis()
b.fun()'''

#__init__ is default constructor
'''class cal:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def sub(self):
        return self.a-self.b
a=int(input("enter:"))
b=int(input("enter:"))
obj=cal(a,b)
choice=1
while choice!=0:
    print("0.Exit")
    print("1.Add")
    print("2.mul")
    print("3.div")
    print("4.sub")
    choice=int(input("enter choice:"))
    if choice==1:
        print(obj.add())
    elif choice==2:
        print(obj.mul())
    elif choice==3:
        print(obj.div())
        
    elif choice==4:
        print(obj.sub())
    elif choice==0:
        print("Exiting!!!")
    else:
        print("exit")'''
        
#obj=cal(a,b)
#print(obj.add())
#print(obj.mul())
#print(obj.div())
#print(obj.sub())





#types of constructors
#1.parameterized
#2.non parameterized
#3.default        



#task        
class bankaccount:
    def __init__(self,account_holder,balance=0):
        self.account_holder=account_holder
        self.balance=balance
    def dp(self,amount):
        self.balance=self.balance+amount
        return f"${amount} deposited. Current balance {self.balance}"
    def wd(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            return f"${amount} withdrawn.Current balance {self.balance}"
        else:
            return f"insufficient balance.Available balance {self.balance}"
    def cb(self):
        return f"Account holder:{self.account_holder},balance:{self.balance}"

AH=input("name:")
amount=int(input("enter amount:"))
ba=bankaccount("mani",100)
print(ba.dp(200))
print(ba.wd(50))
print(ba.cb())
choice=1        
while choice!=0:
    print("1.deposit")
    print("2.withdrawl")
    print("3.check balance")
    choice=int(input("enter :"))
    if choice==1:
         print(ba.dp(amount))
    elif choice==2:
         print(ba.wd(amount))
    elif choice==3:
         print(ba.cb())
    else:
         print("Exit!!!")    