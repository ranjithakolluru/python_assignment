list1=[3,7,9,6,5]
list2=[3,6,7,9]

common=[]

for i in list1:
    if i in list2:
        common.append(i)
print common
