num1={1,2,3,4,5}
num2= set([6,7,8,9])

print ("Before -",num2)
num2.add(3)
num2.remove(7)
print ("After -",num2)

print (num1 | num2)   #union operation
print (num1 & num2)   #intersection operation
print (num1-num2)   # minus operation