#!/usr/bin/python3
"""Lists cities with their IDs, names, and corresponding state names"""

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

    # Execute a SQL query to select cities with their IDs, names, and corresponding state names
    query = """SELECT cities.id, cities.name, states.name 
               FROM cities 
               INNER JOIN states ON states.id = cities.state_id"""
    cursor.execute(query)

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()

