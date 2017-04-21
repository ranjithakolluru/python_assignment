"""Guessing Game: Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, 
then tell them whether they guessed too low, too high, or exactly right. 
(_Hint: remember to use the user input lessons from the very first exercise
Extras:
Keep the game going until the user types exit
Keep track of how many guesses the user has taken, and when the game ends, print this out."""

from random import randint
print "Guessing game"
randomnum=randint(1,9)
print "randomnum is:",randomnum

def comp():
    counter=1
    while(True):
        userno=raw_input("enter your guess or exit:")
        if userno=="exit":
            break 
        if(int(userno)<randomnum):
            print "too low"
        elif int(userno)>randomnum and int(userno)<10:
            print "too high"
        elif int(userno)==randomnum:
            print "exactly right"
            break
        elif int(userno)>9:
            print "Invalid option..enter within the range " 
            
        counter+=1   
    print "total guesses are:",counter  


comp()
 

