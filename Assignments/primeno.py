

def prime(n):
    fcount=0
    for i in range(1,n+1):
        if (n%i) ==0:
            fcount +=1

    if fcount==2:
        print n,"prime"
    else:
        print n,"not prime"


for k in range(1,100):

    prime(k)




    


















