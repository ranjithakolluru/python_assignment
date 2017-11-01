l=[1,4,3,5,2,6]
#l=[1,2,3,4,5,6]

counter=0
while(counter < len(l)-1):

    counter=0
    for i in range(0,len(l)-1):

        if l[i]>l[i+1]:
            temp=l[i]
            l[i]=l[i+1]
            l[i+1]=temp
        else:
            print l[i]
            counter+=1

print l





