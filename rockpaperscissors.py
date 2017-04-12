"""Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, 
print out a message of congratulations to the winner, and ask if the players want to start a new game)"""


p1=raw_input("enter the name of player1")
p2=raw_input("enter the name of player2")
y=True
f=False
while(y):
    userwish1=raw_input("player1-what do u wish to play,rock-paper-scissor")
    userwish2=raw_input("player2-what do u wish to play,rock,paper-scissor")
    if userwish1 == userwish2:
        print "Its a tie,try again"
    elif userwish1=='rock' and userwish2=='paper':
        print "player2 wins"
    elif userwish1=='paper' and userwish2=='rock':
        print "player2 wins"
    elif userwish1=='rock' and userwish2=='scissors':
        print "player1 wins"
    elif userwish1=='scissors' and userwish2=='rock':    
        print "player2 wins"
    elif userwish1=='paper' and userwish2=='scissors':
        print "player2 wins"
    elif userwish1=='scissors' and userwish2=='paper':
        print "player1 wins"
    else:
        print "invalid option , please enter the valid one"
    a=raw_input("do u want to play another game?? press y or f")
    if(a=='f'):
        break
   
   
    