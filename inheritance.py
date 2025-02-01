#single inheritance
'''class animal:
    def speak(self):
        return "animal cannot speaks"
class cat(animal):
    def drink(self):
        return "cat drinks milk"
Cat=cat()
Ani=animal()
print(Cat.drink())
#print(Cat.speak())
#print(Ani.speak())
#print(Ani.drink())'''

#multiple inheritance
'''class family:
    def good(self):
        return "dad is head of the family"
class dad(family):
    def hus(self):
        return "mom is dads solemate"    
class mom(family):
    def wife(self):
        return "mom is dads solemate"
class child(dad,mom):
    def son(self):
        return "superman"
    def daughter(self):
        return "super women"
obj1=mom()
print(obj1.wife())
print(obj1.dad())'''

#multiple inheritance(1->,2->,1,2->3)(two parent class having one child class)
'''class animal:
    def legs(self):
        return "legs"
    def cute(self):
        return "cute"
class pet:
    def speak(self):
        return "animal cannot speaks"
    
class cat(animal,pet):
    def drink(self):
        return "cat drinks milk"
    def meow(self):
        return "meow"
Cat=cat()

print(Cat.drink())
print(Cat.speak())
print(Cat.cute())
print(Cat.meow())'''



#multilevel inheritance(1->2,2->3)(each class has one parent and one child)

'''class animal:
    def legs(self):
        return "legs"
    def cute(self):
        return "cute"
class pet(animal):
    def speak(self):
        return "animal cannot speaks"
    
class cat(pet):
    def drink(self):
        return "cat drinks milk"
    def meow(self):
        return "meow"
Cat=cat()

print(Cat.drink())
print(Cat.speak())
print(Cat.cute())
print(Cat.meow())'''

#heirarichal inheritance(more than one child of a parent class)
'''class animal:#parent1
    def legs(self):
        return "legs"
    def cute(self):
        return "cute"
class dog(animal):#child1
    def speak(self):
        return "animal cannot speaks"
    
class cat(animal):#child2
    def drink(self):
        return "cat drinks milk"
    def meow(self):
        return "meow"
Cat=cat()
Dog=dog()

print(Cat.drink())

print(Cat.cute())
print(Cat.meow())

print(Dog.speak())
print(Dog.cute())'''


'''#method overriding: a method is using in more than one class
class Animal:
    def speak(self):
        return "animal speaks"
class Dog(Animal):
    def speak(self):
        
        return "dog barks"
class cat(Animal):
    def speak(self):
        
        return "cat meows"  
dog=Dog()
Cat=cat()
print(dog.speak())
print(Cat.speak())



#super keyword
class Animal:
    def speak(self):
        return "animal speaks"
class Dog(Animal):
    def speak(self):
        parent_speak=super().speak()
        return f"{parent_speak} and dog barks"
dog=Dog()
print(dog.speak())'''


#method overloading
class mathoperation:
    def mani(self,a,b=20,c=0):
        return a+b+c
math=mathoperation()
print(math.mani(10))
print(math.mani(10,20))
print(math.mani(10,20,30))


class mathoperation:
    def mani(self,*a):
        return sum(a)
math=mathoperation()
print(math.mani(10))
print(math.mani(10,20))


'''def  funtion(*arg):
    print("jagga",arg)
funtion(10)
funtion(10,20,30,40)
funtion(10,'hello',20,30,40)'''


a=[(x,y) for x in [0,1,2] for y in [3,4,5] if x!=y]
print(a)

a=['  today','mani','jagga']
print([x.strip() for x in a])

x=[5,4,3,2]
#x.remove(2)
#x.pop(2)
x.insert(1,0)
print(x)


import sys
print(len(sys.argv))

a='python'+3
print(a)













    
