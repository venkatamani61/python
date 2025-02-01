#take a function ,the input shoub be given by user,if the is + then perfom add +-=%

def  calculate():
    num1=input("enter the first number:")
    set1=int(num1)
    operation=input("-:")
    num2=input("enter second number:")
    set2=int(num2)
    if operation=="+":
        result=int(num1)+int(num2)
        print(f" the result of{num1}+{num2} is:{result}")
    if operation=="+-":
        result=int(num1)/int(num2)
        print(f" the result of{num1}/{num2} is:{result}")
    elif operation=="-":
        result=int(num1)-int(num2)
        print(f" the result of{num1}-{num2} is:{result}")
    elif operation=="*":
        result=int(num1)*int(num2)
        print(f" the result of{num1}*{num2} is:{result}")
    elif operation=="|":
        result=set1.union(set2)
        print(f" the result of{num1}|{num2} is:{result}")
      
calculate()        
     
