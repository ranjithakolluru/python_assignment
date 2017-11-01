def inputlist():
    a_list=list(input("enter few numbers"))
    print a_list
    return a_list

def code():
    a_list=inputlist()
    l=list((a_list[0],a_list[-1]))
    #print l
    return l


anju=code()
print anju