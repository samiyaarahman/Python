#while loop
i=1
while i<=20:
    print (i)
    i = i+1






#sum using while loop
i = 1
total = 0  # Initialize a variable to keep the sum

while i <= 5:
    total = total + i
    i = i + 1

print("Sum =", total)







#list

subject= ["Java", "Python", "C", "C++", "HTML", "CSS"]
print (subject)                           #Print every element
print (subject[0])                        #Print element of index 0
print (subject[2:])                       #Print elements from index 2 to end
print (subject[-1])                       #Print element from reverse, element 4 





#Break
i=1
while i<=100:
    if i==20:
        break
    print (i)
    i=i+1


#Continue

i=1
while i<=100:
    if i==25:
        continue           #after watching Continue it go to the loop again
    print (i)
    i=i+1



#in or not in operator

Subject= ["A", "B", "C", "D", "E"]
print ("C" in Subject)