import string

class Password():
    def __init__(self,password=""):
        self.password = password
        
        
    def checkStrength(self):
        password = self.password
        count = len(password)>=8
        num = False
        speca = False
        cap = False
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
        
    def __str__(self):
        return self.password
                