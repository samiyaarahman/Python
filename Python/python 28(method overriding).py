class phone:
    def __init__(self):
        print ("I am in phone class")
        
        
class samsung(phone):      #method overriding
    def __init__(self):
        super().__init__()  
    
        print ("I am in samsung class")      
        
        
s=samsung()       