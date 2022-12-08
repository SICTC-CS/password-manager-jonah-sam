from PasswordManager import Password
from Account import Account

# functions and variables
ui = "0"
acc1 = Account(input("Enter a Username: "),input("Enter a Password:"),"App")


def login():
    user = input("Username: " )
    passw = input("Password: ")
    
    file1 = open("reg.txt","r")
    file1 = (file1.readlines())
    
    for line in file1:
        username,password = line.rstrip().split(",")
    if user == username and passw == password:
        print("login good")
    else:
        print("NO")

def register():
    aNewUser = input("Username: ")
    aNewPass = input("Password: ")
    
    file1 = open("reg.txt","a")
    file1.write(f"{aNewUser},{aNewPass}\n")
    file1.close()








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
        login()
    elif ui == "2":
        register()
    

