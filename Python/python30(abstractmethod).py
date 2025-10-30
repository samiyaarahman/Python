#Abstract method
from abc import ABC, abstractmethod
class shape(ABC):
    def __init__(self, dim1,dim2):   #constructor
        self.dim1=dim1
        self.dim2=dim2
        
        
    @abstractmethod    
    def area(self):
        print("I am a method of shape class")    
        
        
        
        
class Triangle(shape):
    def area(self):
        area= 0.5 * self.dim1 * self.dim2
        print ("The area of the Triangle is - ",area)
    
    
    
class Rectangle(shape):
    def area(self):
        area= self.dim1 * self.dim2
        print ("The area of the Rectangle is - ",area)
       

 
            
r1=Rectangle(5,4)
r1.area()  



t1=Triangle(6,7)
t1.area()       
           
        
        
        
        