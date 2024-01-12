#!/usr/bin/python3
"""Lists city names in a specific state from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Establish a connection to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute a SQL query to select city names in a specific state
    query = """SELECT cities.name 
               FROM cities 
               INNER JOIN states ON states.id = cities.state_id
               WHERE states.name = %s"""
    state_name = sys.argv[4]
    cursor.execute(query, (state_name,))

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Extract city names into a list
    city_names = [row[0] for row in rows]

    # Print city names separated by commas
    print(", ".join(city_names))

    # Close the cursor and database connection
    cursor.close()
    db.close()

