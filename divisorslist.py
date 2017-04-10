num=int(raw_input("enter a number"))
i=1
while i <= num:
    if(num % i) == 0:
        print "divisors of num are" ,i 
    i+=1
