import mysql.connector

def connect_db():
    """Connect to the MySQL database and return the connection and cursor."""
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  # replace with your MySQL username
        password="An@210803",  # replace with your MySQL password
        database="car_counting"  # replace with your database name
    )
    cursor = conn.cursor()
    return conn, cursor

    conn.commit()
    conn.close()

def insert_count(count):
    """Insert a new count into the car_counts table."""
    conn, cursor = connect_db()
    cursor.execute('INSERT INTO car_counts (count) VALUES (%s)', (count,))
    conn.commit()
    conn.close()
