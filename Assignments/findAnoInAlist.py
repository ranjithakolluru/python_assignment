def userinput():

    inpu=input("enter few numbers")
    s=str(inpu)
    print s
    l=[]
    for i in s:
        l.append(i)
    print l
    return l

def look():
    n=userinput()
    no=input("enter any no")

    for j in range(len(n)):

        if no == n[j]:
            print "truthy"
        else:
            print "falsy"

look()

