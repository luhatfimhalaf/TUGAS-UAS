import os
import transaction

def loginLanding():
    while True:
        username = input("Username: ")
        password = input("Password: ")
        statusAuth = authCheck(username,password)
        if statusAuth == True:
            transaction.transactionLanding()
            break
        else:
            print("Wrong Password or username")

def authCheck(_username,_password):
    username1 = "Buyer"
    password1 = "iwannafrozenfood"
    if username1 == _username and password1 == _password:
        print("Logged in")
        os.system("cls")
        return True
    elif username1 != _username and password1 == _password:
        print("Your username is wrong !")
        os.system("cls")
        return False
    elif username1 == _username and password1 != _password:
        print("Your password is wrong !")
        os.system("cls")
        return False
    elif username1 != _username and password1 != _password:
        print("Your password and username are wrong !")
        os.system("cls")
        return False