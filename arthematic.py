def user_input():
    a=input("enter a number for a:")
    b=input("enter a number for b:")
    option=input("enter your option")
    if option==1:
        val1=addition(a,b)
        display(val1)
    elif option==2:
        val1= subtraction(a,b)
        display(val1)
    elif option==3:
        val1= multiplication(a,b)
        display(val1)
    elif option==4:
        val1= division(a,b)
        display(val1)

def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    return a/b

def display(val1):
    print "Result of operation:",val1

user_input()


    
   