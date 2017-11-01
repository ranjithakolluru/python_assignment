a=[2,3,5,7,11,13,15,17,19,23,27,29]
factor=0

def prime(n):
    factor=0
    for i in range(1,n+1):
        if n%i==0:

            factor+=1
    if factor==2:
        print i,"is prime"
    else:
        print i,"is not prime"
for k in range(1,100):
    prime(k)