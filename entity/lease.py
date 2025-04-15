class Lease:
    def __init__(self, leaseID=0, vehicleID=0, customerID=0, startDate="", endDate="", leaseType="", status="active"):
        self.__leaseID = leaseID
        self.__vehicleID = vehicleID
        self.__customerID = customerID
        self.__startDate = startDate
        self.__endDate = endDate
        self.__leaseType = leaseType
        self.__status = status  # Using 'status' instead of 'active'

    # Getters
    def get_leaseID(self):
        return self.__leaseID

    def get_vehicleID(self):
        return self.__vehicleID

    def get_customerID(self):
        return self.__customerID

    def get_startDate(self):
        return self.__startDate

    def get_endDate(self):
        return self.__endDate

    def get_leaseType(self):
        return self.__leaseType

    def get_status(self):
        return self.__status  # Getter for status

    # Setters
    def set_leaseID(self, leaseID):
        self.__leaseID = leaseID

    def set_vehicleID(self, vehicleID):
        self.__vehicleID = vehicleID

    def set_customerID(self, customerID):
        self.__customerID = customerID

    def set_startDate(self, startDate):
        self.__startDate = startDate

    def set_endDate(self, endDate):
        self.__endDate = endDate

    def set_leaseType(self, leaseType):
        self.__leaseType = leaseType

    def set_status(self, status):
        self.__status = status  # Setter for status
