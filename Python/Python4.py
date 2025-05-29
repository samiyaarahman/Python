#Relational Operator

a= input("Enter 1st Number :")
b= input("Enter 2nd Number :")

print (a>b)
print(a<b)
print(a<=b)
print(a!=b)
print("anu"=="anu")



#conditional control statement

mark = int(input("Enter the mark: "))  # Convert to integer
if mark >= 33:
    print("Pass")
else:
    print("Fail")


# if, elif, else

a= int (input("Enter 1st number: "))
b= int (input("Enter 2nd number: "))
c= int (input("Enter 3rd number: "))

if a>b and a>c:
    print ("a is larger")

elif b>a and b>c:
    print ("b is larger")

else:
    print(" c is larger")


#Ternary operator
print (a if a>b  else b)



