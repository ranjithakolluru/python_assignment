import createaccount
import pymysql

db=pymysql.Connect(host='localhost', port=3306, user='root', passwd='AnjuSandy2628', db='banking_app')
cursor=db.cursor()

def bankingapp():
    option=input("enter ur choice 1. Create Account \n 2. Check Balance \n 3. Withdraw Cash \n 4. Deposit Cash \n 5. Display all account holders: \n 6.Delete Account \n")

    if option==1:
        q=createaccount.createacc()
        cursor.execute(q)
        db.commit()
        db.close()
    elif option==2:
        q="select * from banking_app.customer_details"
        r=cursor.execute(q)
        print r
        db.close()

bankingapp()
