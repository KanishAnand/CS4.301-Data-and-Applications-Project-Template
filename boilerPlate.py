import subprocess as sp
import pymysql
import pymysql.cursors

while(1):
    tmp = sp.call('clear',shell=True)
    username = input("Username: ")
    password = input("Password: ")

    try:
        con = pymysql.connect(host='localhost',
                user=username,
                password=password,
                db='COMPANY',
                cursorclass=pymysql.cursors.DictCursor)
        with con:
            while(1):
                tmp = sp.call('clear',shell=True)
                print("1. Hire a new employee")
                print("2. Fire an employee")
                print("3. Promote an employee")
                print("4. Reward a department")
                print("5. Project Statistics")
                print("6. Department Statistics")
                print("7. Employee Statistics")
                print("8. Check messages")
                print("9. Logout")
                c = int(input("Enter choice> "))
                tmp = sp.call('clear',shell=True)

                if(c==9):
                    break

                switch(c){
                    case 1: 
                }

    except:
        tmp = sp.call('clear',shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
    
   


