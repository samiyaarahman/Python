class triangle:
    base=""
    height=""
    
    
    def set_value(self,base,height):
        self.base=base
        self.height=height
    
    
    def display(self):
        result=1/2* self.base * self.height
        
        print("Result is : ",result)
        
        
       

t1=triangle()
t1.set_value(4,5)
t1.display()



t2=triangle()
t2.set_value(10,30)
t2.display()




##or we can complete it like this--




class triangle:
    
    def __init__(self,base,height): #constructor
        self.base=base
        self.height=height
    
    
    def calculate_area(self):
        area=1/2* self.base * self.height
        
        print("Result is : ",area)
        
        
       

t1=triangle(4,5)
t1.calculate_area()



t2=triangle(30,40)
t2.calculate_area()