import re
pattern= r"^colo.r$" # ^ means start with colo and (.) means any character will be there and $ means ends with r

text= "colour"
if re.match(pattern,text):
    print("matched")
    
    
import re
pattern= r"ice(-)?cream" #(-)? means it match if there is 0 or 1 (-) in pattern

text= "icecream"
if re.match(pattern,text):
    print("matched")
    
        
        
        
import re
pattern= r"a*" # * means 0 or more

text= "colour"
if re.match(pattern,text):
    print("matched")
    
        
import re
pattern= r"a+" # * means 1 or more

text= "colour"
if re.match(pattern,text):
    print("matched")
    
else: 
    print ("Not matched") 
    
    
         
import re
pattern= r"ab*" # * means 0 or more

text= "ababcolour"
if re.match(pattern,text):
    print("matched")
    
       
    
        