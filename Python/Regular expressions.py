import re
pattern= r"colour"
text1= "My fvrt colour is red. Blue colour is fvrt as well"
text2= re.sub(pattern,"color",text1,count=1)#count parameter helps to replace that number of pattern
print(text2)
