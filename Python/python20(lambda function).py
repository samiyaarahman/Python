def calculate(a,b):
    return a*a + 2*a*b +b*b
    
    
print(calculate(2,3))


#we can use lambda function (no function name)
#syntax -(lambda parameter: expression) (value)

print("Answer is -",(lambda a,b : a*a + 2*a*b + b*b) (2,3) )
    