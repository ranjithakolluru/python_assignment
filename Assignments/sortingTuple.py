t=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
#for i in t:

 #   print i[0]
counter=0
while(counter<len(t)-1):
    counter=0
    #print len(t)
    for i in range(0,len(t)-1):
        #counter =0
        if t[i][1]>t[i+1][1]:
            temp=t[i]
            t[i]=t[i+1]
            t[i + 1]=temp
        else:
            print t[i]
            counter+=1
print t
