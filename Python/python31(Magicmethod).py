class Bike:
    def __init__(self,name,color):
        self.name=name
        self.color=color
        
    def __str__(self):
        return(f"name = {self.name}, color= {self.color}")
    
    
    def __eq__(self,other):
        return (self.name==other.name and self.color== other.color)
    
    #def display(self):
        #print(f"name = {self.name}, color= {self.color}")
            
        
        
bike1=Bike("Yamaha R15", "Red")
bike2=Bike("Yamaha R15","Red")

print(str( bike1))       
        
print(bike1==bike2) #if we not declared the magic functon "eq" then this statement not working or it compare only the object name