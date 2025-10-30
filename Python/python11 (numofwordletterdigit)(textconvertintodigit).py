#list as input from user

n= input("Entet a text :")

#assume text was (10 20 30)

list= n.split()  #now it will be (10, 20,30)
sum=0
for num in list:
    sum= sum+ int (num)

print ("sum is :", sum)



#Number of words letters digits in a sentence

numofword=0
numofletter=0
numofdigit=0

text= input ("Enter a text :")

for x in text:
    x=x.lower()
    if x>= 'a' and x<= 'z' :
        numofletter=numofletter+1
        
    elif x>= '0' and x<= '9' :
        numofdigit=numofdigit +1
      
    elif x== ' ' :
        numofword=numofword+1
 
print ("\nNumber of letters :",numofletter)
print ("Number of words :",numofword+1)
print ("Number of digits :",numofdigit)


