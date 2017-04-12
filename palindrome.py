"""Take a string input from the user and check if its Palindrome or not."""
y=True
f=False
while(y):
    a=raw_input("enter any string")
    rev=a[::-1]
    if rev==a:
        print "the number you entered is a palindrome number"
    else:
        print"not a palindrome number"
    b=raw_input("do u want to enter the string again?? press y or f")
    if(b=='f'):
        break       

        
    
  
