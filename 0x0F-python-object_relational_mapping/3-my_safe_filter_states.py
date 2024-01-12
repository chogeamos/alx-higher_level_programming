#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa based on provided name"""

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

    # Assign the value of sys.argv[4] to the variable match
    match = sys.argv[4]

    # Execute a SQL query to select states based on the provided name
    query = "SELECT * FROM states WHERE name LIKE %s"
    cursor.execute(query, (match,))

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()

