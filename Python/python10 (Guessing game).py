#Guessing number game

from random import randint
for x in range(1,6):
     guessNumber =int(input("Guess a number from 1-5 : "))
     randomNumber =randint(1,5)
     
     if guessNumber==randomNumber:
         print ("\nYou have won")
         
     else:
         print ("\nYou have lost")
     print ("The random number was : ", randomNumber)  
     

     
     
 #Guessing number game
 
import random
for x in range(1,6):
     guessNumber =int(input("Guess a number from 1-100 : "))
     randomNumber= random.random() *100
     
     if guessNumber==randomNumber:
         print ("\nYou have won")
         
     else:
         print ("\nYou have lost")
     print ("The random number was : ", randomNumber)