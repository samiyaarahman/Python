import re
pattern= r"a{1,4}$" # {} means range, we can use 1to 4 a in a pattern


text= "aaaaa"
if re.match(pattern,text):
    print("matched")

else:
    print ("Not matched")    





import re
pattern= r"[aeiou]" # {} means range, we can use 1to 4 a in a pattern


text= "ahjionygs"
if re.match(pattern,text):
    print("matched")

else:
    print ("Not matched")    


import re
pattern= r"[A-Z][a-z][0-9]" # [] means character class


text= "Aa0hbshshbd"
if re.match(pattern,text):
    print("matched")

else:
    print ("Not matched")   
    
    
     

import re
pattern= r"[A-Z]*[a-z]*[0-9]" 

text= "AHJJHjja00987hbshshbd"
if re.match(pattern,text):
    print("matched")

else:
    print ("Not matched")   

        