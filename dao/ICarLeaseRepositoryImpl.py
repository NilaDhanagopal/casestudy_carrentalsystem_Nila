from dao.ICarLeaseRepository import ICarLeaseRepository
from entity.vehicle import Vehicle
from entity.customer import Customer
from entity.lease import Lease
from util.DBConnection import DBConnection  # ✅ Correct import
from datetime import date
import mysql.connector

class CarLeaseRepositoryImpl(ICarLeaseRepository):

    def __init__(self):
        self.connection = DBConnection.getConnection()  # ✅ Correct usage

    # 🚗 Car Management Methods
    def addCar(self, car: Vehicle) -> None:
        cursor = self.connection.cursor()
        query = "INSERT INTO vehicle (vehicle_id, make, model, year, rental_rate, available) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (car.vehicle_id, car.make, car.model, car.year, car.rental_rate, car.available)
        cursor.execute(query, data)
        self.connection.commit()
        print("✅ Car added successfully.")

    def removeCar(self, carID: int) -> None:
        cursor = self.connection.cursor()
        query = "DELETE FROM vehicle WHERE vehicle_id = %s"
        cursor.execute(query, (carID,))
        self.connection.commit()
        print("✅ Car removed successfully.")

    def listAvailableCars(self) -> list:
        cursor = self.connection.cursor()
        query = "SELECT * FROM vehicle WHERE available = TRUE"
        cursor.execute(query)
        return cursor.fetchall()

    def listRentedCars(self) -> list:
        cursor = self.connection.cursor()
        query = "SELECT * FROM vehicle WHERE available = FALSE"
        cursor.execute(query)
        return cursor.fetchall()

    def findCarById(self, carID: int) -> Vehicle:
        cursor = self.connection.cursor()
        query = "SELECT * FROM vehicle WHERE vehicle_id = %s"
        cursor.execute(query, (carID,))
        row = cursor.fetchone()
        if row:
            return Vehicle(*row)
        return None

    # 👤 Customer Management Methods
    def addCustomer(self, customer: Customer) -> None:
        cursor = self.connection.cursor()
        query = "INSERT INTO customer (customer_id, name, email, phone) VALUES (%s, %s, %s, %s)"
        data = (customer.customer_id, customer.name, customer.email, customer.phone)
        cursor.execute(query, data)
        self.connection.commit()
        print("✅ Customer added successfully.")

    def removeCustomer(self, customerID: int) -> None:
        cursor = self.connection.cursor()
        query = "DELETE FROM customer WHERE customer_id = %s"
        cursor.execute(query, (customerID,))
        self.connection.commit()
        print("✅ Customer removed successfully.")

    def listCustomers(self) -> list:
        cursor = self.connection.cursor()
        query = "SELECT * FROM customer"
        cursor.execute(query)
        return cursor.fetchall()

    def findCustomerById(self, customerID: int) -> Customer:
        cursor = self.connection.cursor()
        query = "SELECT * FROM customer WHERE customer_id = %s"
        cursor.execute(query, (customerID,))
        row = cursor.fetchone()
        if row:
            return Customer(*row)
        return None

    # 📜 Lease Management Methods
    def createLease(self, customerID: int, carID: int, startDate: date, endDate: date) -> Lease:
        cursor = self.connection.cursor()
        query = "INSERT INTO lease (customer_id, car_id, start_date, end_date, active) VALUES (%s, %s, %s, %s, TRUE)"
        cursor.execute(query, (customerID, carID, startDate, endDate))
        self.connection.commit()
        lease_id = cursor.lastrowid
        print("✅ Lease created successfully.")
        return Lease(lease_id, customerID, carID, startDate, endDate, True)

    def returnCar(self, leaseID: int) -> Lease:
        cursor = self.connection.cursor()
        query = "UPDATE lease SET active = FALSE WHERE lease_id = %s"
        cursor.execute(query, (leaseID,))
        self.connection.commit()
        print("✅ Lease returned successfully.")
        return self.findLeaseById(leaseID)

    def listActiveLeases(self) -> list:
        cursor = self.connection.cursor()
        query = "SELECT * FROM lease WHERE active = TRUE"
        cursor.execute(query)
        return cursor.fetchall()

    def listLeaseHistory(self) -> list:
        cursor = self.connection.cursor()
        query = "SELECT * FROM lease WHERE active = FALSE"
        cursor.execute(query)
        return cursor.fetchall()

    def findLeaseById(self, leaseID: int) -> Lease:
        cursor = self.connection.cursor()
        query = "SELECT * FROM lease WHERE lease_id = %s"
        cursor.execute(query, (leaseID,))
        row = cursor.fetchone()
        if row:
            return Lease(*row)
        return None

    # 💰 Payment Handling
    def recordPayment(self, lease: Lease, amount: float) -> None:
        cursor = self.connection.cursor()
        query = "INSERT INTO payment (lease_id, amount, payment_date) VALUES (%s, %s, CURDATE())"
        cursor.execute(query, (lease.lease_id, amount))
        self.connection.commit()
        print("✅ Payment recorded successfully.")
