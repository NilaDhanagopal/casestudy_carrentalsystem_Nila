import mysql.connector
from mysql.connector import Error
from util.PropertyUtil import getPropertyString

class DBConnection:
    connection = None

    @staticmethod
    def getConnection():
        if DBConnection.connection is None:
            try:
                print("🛜 Attempting to connect to DB...")

                # Fetch properties from properties file
                props = getPropertyString('db.properties')

                DBConnection.connection = mysql.connector.connect(
                    host=props.get('db.host'),
                    port=int(props.get('db.port')),
                    database=props.get('db.database'),
                    user=props.get('db.user'),
                    password=props.get('db.password')  # <--- key line to supply password properly
                )

                if DBConnection.connection.is_connected():
                    print("✅ Connected to database successfully!")
                else:
                    print("❌ Connection object is None.")

            except mysql.connector.Error as e:
                print(f"❌ Database connection failed: {e}")
                raise

        return DBConnection.connection
