no=input("how many numbers u want to generate")
sequence=raw_input("enter few numbers")
l=[]
for i in sequence:
    l.append(i)
print l
i=0
for i in l:
    if i <no:

        l[i]=l[i-1]+l[i-2]
     i+=1












