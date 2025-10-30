import re
pattern = r"Colour"
if re.match(pattern,"red is red. and it is my fvrt"):
  print("Matched")
else:
  print("Not matched")
  
  
if re.search(pattern,"red is red. and it is my fvrt Colour"):
  print("Matched")
else:
  print("Not matched")



print(re.findall(pattern,"red is red. and it is my fvrt Colour"))


text="My fvrt Colour is red"  
match=re.search(pattern, text)

if match:
    print (match.start())
    print (match.end())
    print(match.span())