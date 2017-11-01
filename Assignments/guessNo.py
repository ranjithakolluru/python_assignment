from random import randint
def random():
    no=randint(1,9)
    return no

def userinput():
    user=input("gues the number")
    return user
def compare(no,user):
    no=random()
    user=userinput()
    flag=False
    if user==no:
        print "exactly right"
        flag='n'
        return flag
    elif user<no:
        print "too low"
        flag='y'
        return flag
    elif user>no:
        print "too high"
        flag='y'
        return flag

def main():
    guesses=0
    flag='y'
    rand=random()
    while(flag):

