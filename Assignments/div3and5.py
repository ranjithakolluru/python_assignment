# range=(1,100)
# 1.if a no is divisible by 3 print
#                          5 print it
# 3 and 5- print
# if not divisible by 3 and 5,,print not
#
for n in range(1,100):


    if n % 3 == 0:
        if n % 5 == 0:
            print n , " is divisble by 3 and 5"
        else:
            print n,"its divisble by 3"
    elif n%5==0:
        print n, "divisible by 5"
    else:
        print  n,"not divisible by 3 and 5"







