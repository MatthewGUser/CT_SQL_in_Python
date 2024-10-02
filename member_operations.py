import mysql.connector
from db_connection import connect_to_db

def add_member(id, name, age):
    """
    Adds a new member to the Members table.

    Parameters:
        id (int): Member's unique ID.
        name (str): Member's name.
        age (int): Member's age.

    Returns:
        None
    """
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        try:
            # Check if member already exists
            cursor.execute("SELECT COUNT(*) FROM Members WHERE id = %s", (id,))
            count = cursor.fetchone()[0]
            if count > 0:
                print(f"Member with ID {id} already exists.")
                return

            # SQL query to insert a new member
            query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)"
            cursor.execute(query, (id, name, age))
            connection.commit()
            print(f"Member '{name}' added successfully.")
        except mysql.connector.Error as e:
            print(f"Error while adding member: {e}")  # Print specific database error
        finally:
            cursor.close()
            connection.close()

def update_member_age(member_id, new_age):
    """
    Updates the age of a member in the Members table.

    Parameters:
        member_id (int): Member's unique ID.
        new_age (int): New age for the member.

    Returns:
        None
    """
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        try:
            # Check if member exists
            cursor.execute("SELECT * FROM Members WHERE id = %s", (member_id,))
            member = cursor.fetchone()
            if member:
                # SQL query to update age
                query = "UPDATE Members SET age = %s WHERE id = %s"
                cursor.execute(query, (new_age, member_id))
                connection.commit()
                print(f"Member with ID {member_id}'s age updated to {new_age}.")
            else:
                print(f"Member with ID {member_id} does not exist.")
        except mysql.connector.Error as e:
            print(f"Error while updating member age: {e}")  # Print specific database error
        finally:
            cursor.close()
            connection.close()

def get_members_in_age_range(start_age, end_age):
    """
    Retrieves members whose ages fall between the specified range.

    Parameters:
        start_age (int): Starting age for the range.
        end_age (int): Ending age for the range.

    Returns:
        None
    """
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        try:
            # SQL query to select members within the age range
            query = "SELECT * FROM Members WHERE age BETWEEN %s AND %s"
            cursor.execute(query, (start_age, end_age))
            members = cursor.fetchall()
            if members:
                for member in members:
                    print(f"ID: {member[0]}, Name: {member[1]}, Age: {member[2]}")
            else:
                print("No members found in this age range.")
        except mysql.connector.Error as e:
            print(f"Error while retrieving members: {e}")  # Print specific database error
        finally:
            cursor.close()
            connection.close()
