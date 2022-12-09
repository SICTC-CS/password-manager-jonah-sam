class Account:
    
    def __init__(self,accNam, username, password, category):
        self.username = username
        self.password = password
        self.accNam = accNam
        self.category = category

    def __str__(self):
        
        string=f"""
        {self.accNam}
        username: {self.username}
        password: {self.password}
        category: {self.category}
        """
        return string
