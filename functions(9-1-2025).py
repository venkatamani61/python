


'''#require
def  function(name):
    print("hii "+name)
name=" chinnu "
function(name)

#keyword argument
def  funtion(name1,name2):
    print("hiii " +name1+name2)
funtion(name2="jagga",name1="deesh")


def funtion(name1,name2):
    print("hiii",name1,name2)
funtion(name2="jagadeesh",name1=9)'''


#default argument
def funtion(name1,name2=6):
    print("hiii",name1,name2)
funtion("mani")    

#variable length argument
def  funtion(*arg):
    print("jagga",arg)
funtion(10)
funtion(10,20,30,40)
funtion(10,'hello',20,30,40)


#def hello(x):
    #double=x*2
    #print(double)
#hello(2) 

def jagga(x,y):
    print('welcome to',x,y)
jagga(9,67)    
