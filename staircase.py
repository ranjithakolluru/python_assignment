""""A single integer, n , denoting the size of the staircase.
Print a staircase of size n using # symbols and spaces.
Input: 6 
Output:
          #
        ##
      ###
    ####
  #####
######"""


s='madam'
l=[ ]
nl=[ ]
for i in range(len(s)):
    
    l.append(s[i])
    
    
print l
print range(len(l))
    
    #nl.append(l.pop())
    #print nl
p=[ ] 
for j in range(len(l)):
    p.append(l.pop())
print l
print p    
if l==p:
    print"its a palindrome"
else:
    print "not a palindrome"
