create database car_rental;
use car_rental;
CREATE TABLE Vehicle (
    vehicleID INT PRIMARY KEY AUTO_INCREMENT,
    make VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year INT NOT NULL,
    dailyRate DECIMAL(10,2) NOT NULL,
    status ENUM('available', 'notAvailable') NOT NULL,
    passengerCapacity INT NOT NULL,
    engineCapacity DECIMAL(5,2) NOT NULL
);

CREATE TABLE Customer (
    customerID INT PRIMARY KEY AUTO_INCREMENT,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phoneNumber VARCHAR(15) UNIQUE NOT NULL
);

CREATE TABLE Lease (
    leaseID INT PRIMARY KEY AUTO_INCREMENT,
    vehicleID INT NOT NULL,
    customerID INT NOT NULL,
    startDate DATE NOT NULL,
    endDate DATE NOT NULL,
    type ENUM('DailyLease', 'MonthlyLease') NOT NULL,
    FOREIGN KEY (vehicleID) REFERENCES Vehicle(vehicleID) ON DELETE CASCADE,
    FOREIGN KEY (customerID) REFERENCES Customer(customerID) ON DELETE CASCADE
);

CREATE TABLE Payment (
    paymentID INT PRIMARY KEY AUTO_INCREMENT,
    leaseID INT NOT NULL,
    paymentDate DATE NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (leaseID) REFERENCES Lease(leaseID) ON DELETE CASCADE
);
-- Insert into Customer Table
INSERT INTO Customer (firstName, lastName, email, phoneNumber) VALUES
('Nila', 'Sharma', 'nila.sharma@example.com', '9876543210'),
('Nisha', 'Iyer', 'nisha.iyer@example.com', '9876543211'),
('Praveen', 'Rao', 'praveen.rao@example.com', '9876543212'),
('Uma', 'Krishnan', 'uma.krishnan@example.com', '9876543213'),
('Dhana', 'Raj', 'dhana.raj@example.com', '9876543214');

-- Insert into Vehicle Table
INSERT INTO Vehicle (make, model, year, dailyRate, status, passengerCapacity, engineCapacity) VALUES
('Maruti Suzuki', 'Swift', 2022, 1500.00, 'available', 5, 1.2),
('Hyundai', 'Creta', 2023, 2500.00, 'available', 5, 1.5),
('Honda', 'City', 2021, 2000.00, 'notAvailable', 5, 1.5),
('Tata', 'Nexon', 2023, 1800.00, 'available', 5, 1.2),
('Mahindra', 'Scorpio', 2022, 3000.00, 'notAvailable', 7, 2.2);

-- Insert into Lease Table
INSERT INTO Lease (vehicleID, customerID, startDate, endDate, type) VALUES
(1, 1, '2025-04-01', '2025-04-10', 'DailyLease'),
(2, 2, '2025-04-05', '2025-04-20', 'MonthlyLease'),
(3, 3, '2025-04-02', '2025-04-07', 'DailyLease'),
(4, 4, '2025-04-06', '2025-04-30', 'MonthlyLease'),
(5, 5, '2025-04-08', '2025-04-15', 'DailyLease');

-- Insert into Payment Table
INSERT INTO Payment (leaseID, paymentDate, amount) VALUES
(1, '2025-04-01', 15000.00),
(2, '2025-04-05', 50000.00),
(3, '2025-04-02', 10000.00),
(4, '2025-04-06', 54000.00),
(5, '2025-04-08', 12000.00);
