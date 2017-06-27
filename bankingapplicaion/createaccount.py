

def createacc():

 
    accno=raw_input("enter ur acount number")
    if accno.isalpha():
        print "accountno contains only digits..retry!!"
        
    #print accno
    firstname=raw_input(" enter ur name:")
    while firstname=="":
        print "u forgot to enter ur firstname:"
        firstname=raw_input("enter ur firstname:")
    
    lastname=raw_input("enter ur lastname:")
    while lastname=="":
        print "u forgot to enter ur lastname:"
        lastname=raw_input("enter ur lastname:")
         
    address=raw_input("enter ur address:")
    while address=="":
        print "please enter ur address:"
        address=raw_input("enter ur address:")

    
    query = "insert into banking_app.customer_details (account_no, first_name,last_name,address) " \
            "values ({0}, '{1}','{2}','{3}')".format(accno,firstname, lastname,address)
    return query

    
        
        
        
      
        