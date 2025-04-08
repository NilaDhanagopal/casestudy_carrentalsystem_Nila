# main/MainModule.py

from dao.ICarLeaseRepositoryImpl import CarLeaseRepositoryImpl
from entity.customer import Customer
from entity.vehicle import Vehicle
from datetime import datetime
import sys

def show_menu():
    print("\n===== Car Lease System Menu =====")
    print("1. Add Customer")
    print("2. Add Car")
    print("3. List Available Cars")
    print("4. Create Lease")
    print("5. Return Car")
    print("6. Record Payment")
    print("7. List Customers")
    print("8. List Rented Cars")
    print("9. Exit")

def main():
    repo = CarLeaseRepositoryImpl()

    while True:
        show_menu()
        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            print("\n--- Add New Customer ---")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            email = input("Email: ")
            phone = input("Phone Number: ")
            customer = Customer(first_name=first_name, last_name=last_name, email=email, phone_number=phone)
            repo.addCustomer(customer)

        elif choice == '2':
            print("\n--- Add New Car ---")
            make = input("Make: ")
            model = input("Model: ")
            year = int(input("Year: "))
            daily_rate = float(input("Daily Rate: "))
            status = input("Status (available/notAvailable): ")
            passenger_capacity = int(input("Passenger Capacity: "))
            engine_capacity = int(input("Engine Capacity (cc): "))
            vehicle = Vehicle(make=make, model=model, year=year, daily_rate=daily_rate,
                              status=status, passenger_capacity=passenger_capacity,
                              engine_capacity=engine_capacity)
            repo.addCar(vehicle)

        elif choice == '3':
            print("\n--- Available Cars ---")
            available_cars = repo.listAvailableCars()
            for car in available_cars:
                print(car)

        elif choice == '4':
            print("\n--- Create Lease ---")
            try:
                customer_id = int(input("Customer ID: "))
                car_id = int(input("Car ID: "))
                start_date = input("Start Date (YYYY-MM-DD): ")
                end_date = input("End Date (YYYY-MM-DD): ")
                lease = repo.createLease(customer_id, car_id, start_date, end_date)
                print("Lease Created:", lease)
            except Exception as e:
                print(" Error:", e)

        elif choice == '5':
            print("\n--- Return Car ---")
            lease_id = int(input("Lease ID: "))
            try:
                returned = repo.returnCar(lease_id)
                print("Car Returned. Lease Info:", returned)
            except Exception as e:
                print("Error:", e)

        elif choice == '6':
            print("\n--- Record Payment ---")
            lease_id = int(input("Lease ID: "))
            amount = float(input("Payment Amount: "))
            try:
                repo.recordPayment(lease_id, amount)
                print("Payment Recorded.")
            except Exception as e:
                print("Error:", e)

        elif choice == '7':
            print("\n--- List of Customers ---")
            customers = repo.listCustomers()
            for customer in customers:
                print(customer)

        elif choice == '8':
            print("\n--- Rented Cars ---")
            rented = repo.listRentedCars()
            for car in rented:
                print(car)

        elif choice == '9':
            print(" Exiting application. Goodbye!")
            sys.exit(0)

        else:
            print("Invalid choice. Please select a number from 1 to 9.")

if __name__ == '__main__':
    main()
