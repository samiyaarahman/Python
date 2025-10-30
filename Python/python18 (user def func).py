a=4
b=5
sum=a+b
print(sum)

#we can use userdefinedfunction


def add(x,y):
    sum=x+y
    print(sum)


def mul(m,n,o):
    result=m*n*o
    print(result)
    
    
    
def message():
    print("No parameter")    
    
    
add(10,20)
add(89,67)


mul(2,3,4)
message()


#Returning value from function

def large(a,b):
    if a>b:
        return a
    else:
        return b
  
  
print(large(60,40))

max=large  #we can change the name of function 
print(max(60,40))




