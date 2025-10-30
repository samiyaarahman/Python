#X arg
def student(*details):
    print(details)
    
   
   
student("Anisul",22240078,3.56)   #using normal function call


#to add multiple numbers
def add(*numbers):
    sum=0
    for num in numbers:
        sum= sum + num
    return sum
        
        
print(add(10,20,30,50))    #using return value of function



#XX arg

def student(**details):    #for xx arg use 2*
    print (details)
    
    
student(id = 101, name= "Samiya" , cgpa=3.90)

