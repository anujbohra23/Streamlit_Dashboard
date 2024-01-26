import mysql.connector
import streamlit as st

# Connection details
host = "localhost"
port = "3307"
user = "root"
passwd = "anuj232003"
database = "myDb"


print(
    f"Connecting to MySQL server at {host}:{port} as user {user} for database {database}"
)

conn = None

# Attempt to establish a connection
try:
    conn = mysql.connector.connect(
        host=host, port=port, user=user, passwd=passwd, database=database
    )
    print("Connection successful!")

    # Create a cursor after a successful connection
    c = conn.cursor()
except mysql.connector.Error as err:
    print(f"Error: {err}")


# Function to view all data
def view_all_data():
    if conn is not None:
        c.execute("SELECT * FROM insurance ORDER BY id ASC")
        data = c.fetchall()
        return data
    else:
        return None
