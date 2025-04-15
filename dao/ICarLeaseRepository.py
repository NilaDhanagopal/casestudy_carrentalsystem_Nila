# dao/ICarLeaseRepository.py

from abc import ABC, abstractmethod
from entity.vehicle import Vehicle
from entity.customer import Customer
from entity.lease import Lease
from datetime import date

class ICarLeaseRepository(ABC):

    # car Management
    @abstractmethod
    def addCar(self, car: Vehicle) -> None:
        pass

    @abstractmethod
    def removeCar(self, carID: int) -> None:
        pass

    @abstractmethod
    def listAvailableCars(self) -> list:
        pass

    @abstractmethod
    def listRentedCars(self) -> list:
        pass

    @abstractmethod
    def findCarById(self, carID: int) -> Vehicle:
        pass

    # Customer Management
    @abstractmethod
    def addCustomer(self, customer: Customer) -> None:
        pass

    @abstractmethod
    def removeCustomer(self, customerID: int) -> None:
        pass

    @abstractmethod
    def listCustomers(self) -> list:
        pass

    @abstractmethod
    def findCustomerById(self, customerID: int) -> Customer:
        pass

    #  Lease Management
    @abstractmethod
    def createLease(self, customerID: int, carID: int, startDate: date, endDate: date) -> Lease:
        pass

    @abstractmethod
    def returnCar(self, leaseID: int) -> Lease:
        pass

    @abstractmethod
    def listActiveLeases(self) -> list:
        pass

    @abstractmethod
    def listLeaseHistory(self) -> list:
        pass

    #  Payment Handling
    @abstractmethod
    def recordPayment(self, lease: Lease, amount: float) -> None:
        pass
