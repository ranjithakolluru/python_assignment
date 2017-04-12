"""You are given a string.  Split the string on a " " (space) delimiter and join using a - hyphen.
Sample Input
this is a string   
Sample Output
this-is-a-string"""

s=raw_input("enter any string")
v=s.split(' ')
print "-".join(v)
