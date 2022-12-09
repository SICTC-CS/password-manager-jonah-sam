# from PasswordManager import Password
from Account import Account
from User import User
import string

# functions and variables
ui = "0"
tries = 0
masterAccountList = []

# Check password requirement
def checkStrength(password):
    count = len(password)>=8
    num = False
    speca = False
    cap = False
    #if car in password has a uppercase,digits and punctuation and has 8 letter or number return True else return False
    for char in password:
        if char in string.ascii_uppercase:
            cap = True
        elif char in string.digits:
            num = True
        elif char in string.punctuation:
            speca = True
    if num and speca and cap and count:
        return True
    else:
        return False


#login use def check strength if meet requirement         
def login():
    tries = False
    k = 0
    #While tries equal False and less the 3 loop
    while tries == False and k < 3:
        user = input("Username: " )
        passw = input("Password: ")
#read reg.txt file
        file1 = open("reg.txt","r")
        file1 = file1.readlines()
#for line in file rstrip and split it with , 
        for line in file1:
            username,password,first,last = line.rstrip().split(",")
            #if password and username match password and username in txt file trie to true
            if user == username and passw == password:
                print("login good")
                tries = True
        if tries == True:
            fileToWriteTo = open(f"{User.lastName}_{User.firstName}.txt","w")
            fileToWriteTo.close
            k += 3
            return True
        if tries == False:
            print("Incorrect")
            k += 1
    if tries == False and k == 3:
        return False


#register
def register():
    check = False
    #While check is false loop
    while check == False:
        aNewFirst = input("First Name: ")
        aNewLast = input("Last Name: ")
        aNewUsername = input("Username: ")
        aNewPass = input("Password: ")
#Check pass strength
        passCheck = checkStrength(aNewPass)
#if passcheck is true
#append user input from register to ref.txt file
        if passCheck == True:
            file1 = open("reg.txt","a")
            file1.write(f"{aNewUsername},{aNewPass},{aNewFirst},{aNewLast}\n")
            file1.close()
            aNewUser = User(aNewFirst,aNewLast,aNewUsername,aNewPass)
            check = True
            #elif false ask user to try again
        elif passCheck == False:
            print("Invalid Password Requirements")
            print('''
    password requirement
  1. atleast 8 characters  
  2. contains numbers
  3. contains special chars
  4. contains capitals
  ''')


def addAccount():
    newAccount = Account(input("What do you want to call this account? "),
                         input("Username: "),
                         input("Password: "),
                         input("Category: "))
    masterAccountList.append(newAccount)







# running code
while ui != "3":
    print('''
           ::PASSWORD MANAGER::
-------------Login or SignUp-------------
1. Login
2. SignUp
3. Exit 
-----------------------------------------
          ''')
    ui = input("What would you like to do? ")
    if ui == "1":
        userInput = login()
        while userInput == True:
            print(f'''
--------------Password Manager--------------
1. Add Account
2. Account List
3. Edit/Delete Account
4. Exit
--------------------------------------------
''')
            choice = input("What would you like to do? ")
            if choice == "1":
                addAccount()
            elif choice == "2":
                for i in masterAccountList:
                    print(i)
            elif choice == "3":
                editAccount()
            elif choice == "4":
                userInput = False
        if userInput == False:
            ui = "3"
    elif ui == "2":
        register()
        ui = "0"
    



