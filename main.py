from dao.ICarLeaseRepositoryImpl import CarLeaseRepositoryImpl
from entity.customer import Customer
from entity.vehicle import Vehicle
from datetime import datetime
import sys
from exceptions.CustomerNotFoundException import CustomerNotFoundException
from exceptions.CarNotFoundException import CarNotFoundException
from exceptions.LeaseNotFoundException import LeaseNotFoundException
from exceptions.invalid_customer_detail_exception import DuplicateCustomerException
from exceptions.invalid_customer_detail_exception import InvalidEmailException
from exceptions.invalid_customer_detail_exception import InvalidPhoneNumberException
import mysql.connector
from util.DBConnection import DBConnection
from util.validators import validate_email, validate_phone
import re  # For regular expression operations


def get_connection():
    return DBConnection.getConnection()
def login():
    print("\n=== Login ===")
    username = input("Username: ")
    password = input("Password: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Admin WHERE username=%s AND password=%s", (username, password))
    admin = cursor.fetchone()

    if admin:
        print(" Admin Login Successful.")
        admin_menu()
        return

    cursor.execute("SELECT * FROM Customer WHERE username=%s AND password=%s", (username, password))
    customer = cursor.fetchone()

    if customer:
        print(f" Customer Login Successful. Welcome, {customer[1]}!")
        customer_menu(customer[0])  # customerID
    else:
        print(" Invalid credentials. Try again.")

    conn.close()


def admin_menu():
    repo = CarLeaseRepositoryImpl()

    while True:
        print("\n===== Admin Menu =====")
        print("1. Add Car")
        print("2. Remove Car")
        print("3. List Available Cars")
        print("4. List Rented Cars")
        print("5. Find Car by ID")
        print("6. Add Customer")
        print("7. Remove Customer")
        print("8. List Customers")
        print("9. Find Customer by ID")
        print("10. List Active Leases")
        print("11. List Lease History")
        print("12. Record Payment")
        print("13. Logout")

        choice = input("Enter choice: ")

        if choice == '1':
            make = input("Make: ")
            model = input("Model: ")
            year = int(input("Year: "))
            dailyRate = float(input("Rate: "))
            status = input("Status (available/notAvailable): ")
            passengerCapacity = int(input("Capacity: "))
            engineCapacity = float(input("Engine Capacity: "))
            car = Vehicle(make, model, year, dailyRate, status, passengerCapacity, engineCapacity)
            repo.addCar(car)

        elif choice == '2':
            vehicleID = int(input("Car ID: "))
            repo.removeCar(vehicleID)

        elif choice == '3':
            for car in repo.listAvailableCars():
                print(car)

        elif choice == '4':
            for car in repo.listRentedCars():
                print(car)

        elif choice == '5':
            vehicleID = int(input("Car ID: "))
            try:
                car = repo.findCarById(vehicleID)
                print(car)
            except CarNotFoundException as e:
                print(f" {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")


        elif choice == '6':
            fname = input("First Name: ")
            lname = input("Last Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            username = input("Username: ")
            password = input("Password: ")
            try:

                # Validate email and phone before creating the customer
                print("Validating email and phone...")  # Debugging statement
                validate_email(email)
                validate_phone(phone)
                # If validation passes, proceed to add customer
                print("Validation passed, creating customer...")  # Debugging statement
                cust = Customer(fname, lname, email, phone, username, password)
                repo.addCustomer(cust)
                print("Customer added successfully.")
            except InvalidEmailException as e:
                print(f" {e}")
            except InvalidPhoneNumberException as e:
                print(f" {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")


        elif choice == '7':
            customerID = int(input("Customer ID: "))
            repo.removeCustomer(customerID)

        elif choice == '8':
            for cust in repo.listCustomers():
                print(cust)

        elif choice == '9':
            customerID = int(input("Customer ID: "))
            try:
                customer = repo.findCustomerById(customerID)
                print(customer)
            except CustomerNotFoundException as e:
                print(f" {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")

        elif choice == '10':
            for lease in repo.listActiveLeases():
                print(lease)

        elif choice == '11':
            for lease in repo.listLeaseHistory():
                print(lease)

        elif choice == '12':
            leaseID = int(input("Lease ID: "))
            try:
                lease = repo.findLeaseById(leaseID)
                amount = float(input("Amount: "))
                repo.recordPayment(lease, amount)
                print("Payment recorded.")
            except LeaseNotFoundException as e:
                print(f" {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")

        elif choice == '13':
            print(" Logged out.")
            break


def customer_menu(customerID):
    repo = CarLeaseRepositoryImpl()

    while True:
        print("\n===== Customer Menu =====")
        print("1. List Available Cars")
        print("2. Create Lease")
        print("3. Return Car")
        print("4. View My Lease History")
        print("5. Logout")

        choice = input("Enter choice: ")

        if choice == '1':
            for car in repo.listAvailableCars():
                print(car)

        elif choice == '2':
            vehicleID = int(input("Car ID: "))
            start = input("Start Date (YYYY-MM-DD): ")
            end = input("End Date (YYYY-MM-DD): ")
            lease = repo.createLease(customerID, vehicleID, start, end)
            print("Lease Created:", lease)

        elif choice == '3':
            leaseID = int(input("Lease ID: "))
            try:
                lease = repo.returnCar(leaseID)
                print("Car Returned:", lease)
            except LeaseNotFoundException as e:
                print(f" {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")

        elif choice == '4':
            try:
                leases = repo.listLeaseHistory(customerID)
                for l in leases:
                    print(l)
            except LeaseNotFoundException as e:
                print(f" {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")

        elif choice == '5':
            print(" Logged out.")
            break


if __name__ == '__main__':
    login()
