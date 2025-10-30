#swapping
a= int(input("Enter 1st number -"))
b= int(input("\nEnter 2nd number -"))

temp=a      #temp=value of a
a=b         #a=value of b
b=temp      #b=value of a

print("\na is ",a)
print("\nb is ",b)


#in python we can easily do this
a= int(input("Enter 1st number -"))
b= int(input("\nEnter 2nd number -"))


(a,b) = (b,a)   #swapping

print("\na is ",a)
print("\nb is ",b)