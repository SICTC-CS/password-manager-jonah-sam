from PasswordManager import Password

class Account:
    
    def __init__(self, username, password, accNam):
        self.username = username
        self.password = password
        self.accNam = accNam
        
    def register(self, username, password):
        self.username = username(input("Enter username: "))
        self.password = password(input("Enter password: "))
        
        if password == self.password():
            file1 = open("reg.txt","a")
            file1.write(username,password)
            
            
       
        
    def __str__(self):
        
        string=f"""
        {self.accNam}
        username: {self.username}
        password: {self.password}
        """
        return string
