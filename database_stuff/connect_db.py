import mysql.connector

def connect_db():
        db_name = "library_management"
        user = "root"
        password = "A6d0a6m1!"
        host = "localhost" # or 127.0.0.1

        try:
            conn = mysql.connector.connect(
                database = db_name,
                user = user,
                password = password,
                host = host
            )
            print("Connected Succesfully")
            return conn
        
        except mysql.connector.Error as e:
            print(f"Error: {e}")

