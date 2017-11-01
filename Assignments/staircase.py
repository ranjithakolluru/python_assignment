no=input("enter a no")
var=no
for i in range(no+1):
    print var*" "+"#"*i+"#"*(i+1)
    var-=1
