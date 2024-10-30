
class Credential:

    def __init__(self , pwd , username , email , product):
        
        self.__pwd = pwd 
        self.__username = username
        self.__email = email
        self.__product = product

    
    @property
    def pwd(self):
        return self.__pwd
    
    @property
    def unsername(self):
        self.__username

    @property
    def email(self):
        self.__email

    @property
    def product(self):
        self.__product


    @pwd.setter
    def pwd(self, pwd):
        if pwd == "":
            print("DEBUG : Invalid password")
        else:
            self.__pwd = pwd

    @unsername.setter
    def username(self, username):
        if username == "":
            print("DEBUG : username can be added leater")
        else:
            self.__username = username
    
    @email.setter
    def email(self, email):
        if email == "":
            print("DEBUG : Invalid email")
        else:
            self.__email = email
    
    @product.setter
    def product(self , product):
        if product == "":
            print("DEBUG : Invalid product")