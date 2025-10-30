#Exception Handling
#type error

try:
    list = [20,10,0]
    result= list [0] / list [2]
    print(result)
    print ("Done")
    
except ZeroDivisionError:
    
    print("Deviding by zero is not possible")
    
except IndexError:
    print ("Index error")
    
    
    
finally:
    print("Successful")
    
 #valueerror (float instead of integer)   

try:
    a= int(input("\nEnter a number -"))
    b= int(input("\nEnter another number -"))
    
    result=a/b
    print(result)
    
       
except (ValueError, ZeroDivisionError):
    print ("\nYou Enter invalid number")
    
    
finally:
    print ("\nThanks!!")
    
    
#raise function  

def voter(age):
    if age<18:
        raise ValueError ("Invalid Voter")
    return ("You are allowed for vote")
try:
    print(voter(19))
    
     
except ValueError as e:
    print(e)
    


