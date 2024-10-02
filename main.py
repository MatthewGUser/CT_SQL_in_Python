import time
import mysql.connector
from db_connection import connect_to_db
from member_operations import add_member, update_member_age, get_members_in_age_range
from session_operations import add_workout_session, get_workout_sessions_for_member

def create_tables(connection):
    cursor = connection.cursor()
    try:
        # Create Members table
        cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS Members (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            age INT NOT NULL
        )
        ''')
        print("Members table created successfully.")

        # Create WorkoutSessions table
        cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS WorkoutSessions (
            session_id INT AUTO_INCREMENT PRIMARY KEY,
            member_id INT,
            date DATE NOT NULL,
            duration_minutes INT NOT NULL,
            calories_burned INT NOT NULL,
            FOREIGN KEY (member_id) REFERENCES Members(id) ON DELETE CASCADE
        )
        ''')
        print("WorkoutSessions table created successfully.")

        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

def drop_tables(connection):
    cursor = connection.cursor()
    try:
        # Drop the foreign key constraint from the WorkoutSessions table
        cursor.execute("ALTER TABLE WorkoutSessions DROP FOREIGN KEY workoutsessions_ibfk_1")
        print("Foreign key constraint dropped successfully.")

        # Drop the WorkoutSessions table
        cursor.execute("DROP TABLE IF EXISTS WorkoutSessions")
        print("WorkoutSessions table dropped successfully.")

        # Drop the Members table
        cursor.execute("DROP TABLE IF EXISTS Members")
        print("Members table dropped successfully.")

        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

def main():
    # Connect to the database
    connection = connect_to_db()
    
    if connection:
        # Create the tables at the start
        create_tables(connection)

        # Example operations to fill and manipulate data
        add_member(1, 'John Doe', 30)
        add_member(2, 'Jane Smith', 25)
        add_member(3, 'Alice Johnson', 35)
        
        update_member_age(1, 31)  # Update John's age
        get_members_in_age_range(25, 35)  # Retrieve members in age range

        # Add workout sessions for members
        add_workout_session(1, '2024-10-01', 45, 300)  # John Doe's session
        add_workout_session(2, '2024-10-01', 30, 200)  # Jane Smith's session

        # Demonstrate retrieving workout sessions for a member
        get_workout_sessions_for_member(1)

        # Wait for 1 minute (60 seconds)
        print("Waiting for 1 minute before dropping tables...")
        time.sleep(60)

        # Drop the tables after the wait
        drop_tables(connection)
        print("Database cleared.")

        # Close the connection
        connection.close()
    else:
        print("Failed to connect to the database.")

if __name__ == "__main__":
    main()
