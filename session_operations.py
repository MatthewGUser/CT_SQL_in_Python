import mysql.connector
from db_connection import connect_to_db

def add_workout_session(member_id, date, duration_minutes, calories_burned):
    """
    Adds a new workout session for a specific member.

    Parameters:
        member_id (int): The ID of the member.
        date (str): The date of the workout session.
        duration_minutes (int): Duration of the workout session in minutes.
        calories_burned (int): Calories burned during the session.

    Returns:
        None
    """
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        try:
            # SQL query to insert a new workout session
            query = "INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (member_id, date, duration_minutes, calories_burned))
            connection.commit()
            print("Workout session added successfully.")
        except mysql.connector.Error as e:
            print(f"Error: {e}")  # Print specific database error
        finally:
            cursor.close()
            connection.close()

def get_workout_sessions_for_member(member_id):
    """
    Retrieves all workout sessions for a specific member.

    Parameters:
        member_id (int): The ID of the member.

    Returns:
        list: A list of workout sessions for the member.
    """
    connection = connect_to_db()
    sessions = []
    if connection:
        cursor = connection.cursor()
        try:
            query = "SELECT * FROM WorkoutSessions WHERE member_id = %s"
            cursor.execute(query, (member_id,))
            sessions = cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"Error while retrieving sessions: {e}")  # Print specific database error
        finally:
            cursor.close()
            connection.close()
    return sessions


def delete_workout_session(session_id):
    """
    Deletes a workout session based on its session ID.

    Parameters:
        session_id (int): The ID of the workout session to delete.

    Returns:
        None
    """
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        try:
            # SQL query to delete a workout session by session_id
            query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
            cursor.execute(query, (session_id,))
            connection.commit()
            if cursor.rowcount > 0:
                print("Workout session deleted successfully.")
            else:
                print(f"No session found with ID {session_id}.")
        except mysql.connector.Error as e:
            print(f"Error while deleting workout session: {e}")  # Print specific database error
        finally:
            cursor.close()
            connection.close()
