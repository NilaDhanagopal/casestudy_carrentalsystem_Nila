import mysql.connector
from mysql.connector import Error
from util.PropertyUtil import getPropertyString

class DBConnection:
    connection = None

    @staticmethod
    def getConnection():
        if DBConnection.connection is None:
            props = getPropertyString()
            print(" Loaded DB properties:", props)
            try:
                print("️ Attempting to connect to DB...")
                DBConnection.connection = mysql.connector.connect(
                    host=props.get('host'),
                    port=props.get('port'),
                    database=props.get('database'),
                    user=props.get('user'),
                    password=props.get('password')
                )
                if DBConnection.connection:
                    print("Connected to database successfully!")
                else:
                    print(" Connection object is None.")
            except Error as e:
                print(f" Database connection failed: {e}")
        return DBConnection.connection
