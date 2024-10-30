

class User:

    def __init__(self , username , pwd , nome , email , number_phone):
        self.__username = username
        self.__pwd = pwd
        self.__nome = nome
        self.__email = email
        self.__number_phone = number_phone

    
    @property
    def username(self):
        return self.__username
    
    @property
    def pwd(self):
        return self.__pwd
    
    @property 
    def nome(self):
       return self.__nome
    
    @property
    def email(self):
       return self.__email
    
    @property
    def number_phone(self):
       return  self.__number_phone



    @username.setter
    def username(self , username):
        if username == "":
            print("DEBUG : username is empty")
        else:
            self.__username = username
    
    @pwd.setter
    def pwd(self , pwd):
        if pwd == "" or len(pwd) < 8:
            print("DEBUG : passowrd is empty or too short")
        else:
            self.__pwd = pwd

    @nome.setter
    def nome(self , nome):
        if nome == "":
            print("DEBUG : name is empty")
        else:
            self.__nome = nome

    @email.setter
    def email(self , email):
        if email == "":
            print("DEBUG : email is empty")
        else:
            self.__email = email

    @number_phone.setter
    def number_phone(self, number_phone):
        if number_phone == "" or len(number_phone)<10 or len(number_phone) > 10:
            print("DEBUG : number phone is invalid")

            