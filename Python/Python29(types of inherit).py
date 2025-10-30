#Multilevel Inheritance

class A:
    def display1():
        print("I am inside A cls")
        
        
class B(A):
    def display2():
        print("I am inside B cls")        
        
        
class C(B):
    #display1
    #display2
    def display3():
        print("I am inside C cls")
        
obj1=C
obj1.display1()
obj1.display2()
obj1.display3()


        
#Multitle Inheritance 
class A:
    def display():
        print("I am inside A cls")
        
        
class B:
    def display():
        print("I am inside B cls")        
        
        
class C(A,B):
    pass
    #display1
    #display2
    #def display():
       # print("I am inside C cls")
       
       
       
class C(B,A):
    pass
    #display1
    #display2
    #def display():
       # print("I am inside C cls")       
       
        
obj1=C
obj1.display()
       