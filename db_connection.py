import mysql.connector

def connect_to_db():
    """Establish a connection to the database and return the connection object."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Update this with your actual username
            password='',  # Update this with your actual password if needed
            database='gym_database'  # Ensure this database exists
        )
        return connection
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None
