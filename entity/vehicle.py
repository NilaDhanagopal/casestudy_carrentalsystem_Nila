class Vehicle:
    def __init__(self, vehicleID=0, make="", model="", year=0, dailyRate=0.0, status="available", passengerCapacity=0, engineCapacity=0):
        self.__vehicleID = vehicleID
        self.__make = make
        self.__model = model
        self.__year = year
        self.__dailyRate = dailyRate
        self.__status = status
        self.__passengerCapacity = passengerCapacity
        self.__engineCapacity = engineCapacity

    # Getters
    def get_vehicleID(self):
        return self.__vehicleID

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_dailyRate(self):
        return self.__dailyRate

    def get_status(self):
        return self.__status

    def get_passengerCapacity(self):
        return self.__passengerCapacity

    def get_engineCapacity(self):
        return self.__engineCapacity

    # Setters
    def set_vehicleID(self, vehicleID):
        self.__vehicleID = vehicleID

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def set_dailyRate(self, dailyRate):
        self.__dailyRate = dailyRate

    def set_status(self, status):
        self.__status = status

    def set_passengerCapacity(self, passengerCapacity):
        self.__passengerCapacity = passengerCapacity

    def set_engineCapacity(self, engineCapacity):
        self.__engineCapacity = engineCapacity
