def num(n1,n2):
    try:
        res=n1/n2
    except ZeroDivisionError:
        print("Error:Cannot divide by zero.")
    except TypeError:
        print("Invalid input type")
    else:
        print(res)
        print("division success")
    finally:
        print("Execution haas been completed")
num(10,2)
num(23,4)
num(0,3)
num("syh",9)
