import mysql.connector
from mysql.connector import Error
from util.PropertyUtil import getPropertyString

class DBConnection:
    connection = None

    @staticmethod
    def getConnection():
        if DBConnection.connection is None:
            try:
                print("️ Attempting to connect to DB...")
                DBConnection.connection = mysql.connector.connect(
                    host='localhost',
                    port=3306,
                    database='car_rental',
                    user='root',
                    password='Praveen@07'
                )
                if DBConnection.connection:
                    print("Connected to database successfully!")
                else:
                    print(" Connection object is None.")
            except mysql.connector.Error as e:
                print(f" Database connection failed: {e}")
                raise
        return DBConnection.connection



