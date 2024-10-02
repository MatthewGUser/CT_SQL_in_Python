# CT_SQL_in_Python
Module 5, Lesson 3

# In `db_connection.py` please fill in credentials as needed.

## Code to run in assignment terminal:
``
pip install mysql-connector-python
python
import mysql.connector
exit()
``
* Restart IDE *

# Log into MySQL then:

## Show existing databases:
``
SHOW DATABASES;
``
## Create a new database:
``
CREATE DATABASE gym_database;
``
## Select the new database:
``
USE gym_database;
``
## Verify the current database:
``
SELECT DATABASE();
``

## Once main.py is run, open up the CLI and execute the following:
``
USE gym_database;
SELECT * FROM Members;
SELECT * FROM WorkoutSessions;
SELECT COUNT(*) AS total_members FROM Members;
SELECT COUNT(*) AS total_workout_sessions FROM WorkoutSessions;

``

# Tables will be removed after operation (main.py) is run after 1 minute.
# This is done so that a blank start can be used for when you execute and won't keep my populated table.