# Import the mysql.connector module to connect to a MySQL database
import mysql.connector

# Define a function to establish a connection to the MySQL CRM database
def get_connection():
    """
    Establish and return a connection to the local MySQL database.

    Returns:
        MySQLConnection: A live connection object to the 'crm_db' database
                         using the credentials provided.
    """
    return mysql.connector.connect(
        host="localhost",           # The address of the MySQL server; 'localhost' means the local machine
        user="root",                # The MySQL username with access to the 'crm_db' database
        password="Gopinath",        # The password for the MySQL user
        database="crm_db"           # The name of the database to connect to (assumed to contain CRM data)
    )