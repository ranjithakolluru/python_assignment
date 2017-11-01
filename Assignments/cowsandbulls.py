from random import randint
inputuser=raw_input("enter your guess")

userlist=[]
for i in inputuser:

    userlist.append(i)


print userlist

randnum=str(randint(1000,9999))
print "random",randnum
randlist=[]
for j in randnum:
    randlist.append(j)
print randlist
cows=0
bulls=0
for i in userlist:
    if userlist[i]==randlist[j]:
        cows+=1
    else:
        bulls+=1
print cows,bulls

