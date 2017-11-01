str1=raw_input("enter a long string")
spl=str1.split()
print spl
p=[]
for i in range(len(spl)):
    p.append(spl.pop())
    "".join(p)
print p