class Customer:
    def __init__(self, customerID=0, firstName="", lastName="", email="", phoneNumber="", username="", password=""):
        self.__customerID = customerID
        self.__firstName = firstName
        self.__lastName = lastName
        self.__email = email
        self.__phoneNumber = phoneNumber
        self.__username = username
        self.__password = password

    # Getters
    def get_customerID(self):
        return self.__customerID

    def get_firstName(self):
        return self.__firstName

    def get_lastName(self):
        return self.__lastName

    def get_email(self):
        return self.__email

    def get_phoneNumber(self):
        return self.__phoneNumber

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    # Setters
    def set_customerID(self, customerID):
        self.__customerID = customerID

    def set_firstName(self, firstName):
        self.__firstName = firstName

    def set_lastName(self, lastName):
        self.__lastName = lastName

    def set_email(self, email):
        self.__email = email

    def set_phoneNumber(self, phoneNumber):
        self.__phoneNumber = phoneNumber

    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password

    def __str__(self):
        return f"CustomerID: {self.__customerID}, Name: {self.__firstName} {self.__lastName}, Email: {self.__email}, Phone: {self.__phoneNumber}"
