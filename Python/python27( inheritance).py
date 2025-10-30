#parent class, Base cls, super cls
class phone:
    def message():
        print("You can send mesaage")
        
    def call():
        print ("You can call")   
        
#sub class, chilo cls, derived cls       
class samsung(phone):      #inheritance 
    
        
    def photo():
        print ("You can take photo")
        
        
p1=phone
p1.call()
p1.message()      
                 
                 
s1=samsung
s1.photo()
s1.call()             
    
    
    
                 