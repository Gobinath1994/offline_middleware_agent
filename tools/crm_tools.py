# Import the function to establish a connection to the MySQL database
from db.db_utils import get_connection

# Define the function to retrieve overdue invoices, optionally filtered by customer name
def get_overdue_invoices(customer_name: str = None):
    """
    Fetches overdue invoices from the CRM database.
    
    Args:
        customer_name (str, optional): The name of the customer to filter overdue invoices.
                                       If None, returns all overdue invoices.
    
    Returns:
        str: A formatted string listing the overdue invoices, or a message if none found.
    """

    # Connect to the database
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)  # Return results as dictionaries (not tuples)

    # Build and execute the SQL query based on whether a customer name is provided
    if customer_name:
        # Filter invoices by customer name and status = 'overdue'
        query = "SELECT id, amount, due_date FROM invoices WHERE status = 'overdue' AND customer_name = %s"
        cursor.execute(query, (customer_name,))
    else:
        # Fetch all overdue invoices
        query = "SELECT id, amount, due_date FROM invoices WHERE status = 'overdue'"
        cursor.execute(query)

    # Fetch all matching rows from the result
    rows = cursor.fetchall()

    # Clean up database resources
    cursor.close()
    conn.close()

    # If no invoices are found, return a friendly message
    if not rows:
        return f"No overdue invoices found for {customer_name or 'any customer'}."

    # Format each invoice into a human-readable string
    formatted = "\n".join([
        f"📄 Invoice #{row['id']}: ₹{row['amount']} due on {row['due_date']}"
        for row in rows
    ])

    # Return the final formatted output
    return f"Overdue invoices for {customer_name or 'all customers'}:\n\n{formatted}"