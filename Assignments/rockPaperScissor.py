player1=raw_input("enter the name of the player1")
player2=raw_input("enter the name of the player2")

y=True
while(y):
    option1 = raw_input("hey %s what do u want to play" % ("player1"))
    option2 = raw_input("hey %s what do u want to play" % ("player2"))


    if option1==option2:
        "its a tie"
    elif option1=="rock" and option2=="paper":
        print "player1 wins"
    elif option1=="rock" and option2=="scissors":
        print "player1 wins"
    elif option1=="scissors" and option2=="paper":
        print "player1 wins"
    else:
        print "player2 wins"
    b=raw_input("do u wish to play again? press y or n")
    if b=="n":
     break

