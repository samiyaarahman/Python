#map function

def square(x):
    return x * x
    
    
num=[1,2,3,4,5]


result= list(map (square,num))
print( result)
   
   
   
#list comprehensions
#syntax -[expression for item in list]   

num=[1,2,3,4,5]   
result=[x*x for x in num]
print(result)
   
    
#filter function

num=[1,2,4,5,6,8,7]

result = list(filter(lambda x : x % 2==0 ,num))
print(result)



#we can use list comprehensions

num=[1,2,3,4,5]   
result=[x for x in num if x % 2 ==0]
print(result)