import mysql.connector
from datetime import datetime

# Connect to MySQL and use the existing willson_financial database
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='ezaccess!',
    auth_plugin='mysql_native_password',
    database='willson_financial'
)
cursor = db.cursor()

# Get the current date and time
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"\nReport Generated on: {current_datetime}\n")

# Report 1: Number of Clients Added Per Month for the Past Six Months
query_clients_per_month = """
SELECT 
    DATE_FORMAT(DateAdded, '%Y-%m') AS Month, 
    COUNT(*) AS NumberOfClients 
FROM 
    Client 
WHERE 
    DateAdded >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH) 
GROUP BY 
    DATE_FORMAT(DateAdded, '%Y-%m')
"""

#Display the Number of Clients Added Per Month for the Past Six Months   
cursor.execute(query_clients_per_month)
tables = cursor.fetchall()
print("-- Number of Clients Added Per Month --")
for table in tables:
    print(f"Month: {table[0]}\nNumberofClients: {table[1]}\n")

# Report 2: Average Amount of Assets for the Entire Client List
query_avg_assets_per_client = """
SELECT 
    AVG(Balance) AS AverageAssets
FROM 
    Account
"""

#Display the Average Amount of Assets for the Entire Client List   
cursor.execute(query_avg_assets_per_client)
tables = cursor.fetchall()
print("-- Average Amount of Assets for the Entire Client List --")
for table in tables:
    print("AverageAssests: ${:.2f}\n".format(table[0]))


# Report 3: Clients with a High Number of Transactions (More Than 10 per Month)
query_high_transaction_clients = """
SELECT 
    C.ClientID, 
    CONCAT(C.FirstName, ' ', C.LastName) AS ClientName, 
    COUNT(TransactionID) AS NumberOfTransactions 
FROM 
    Client C 
JOIN 
    Account A ON C.ClientID = A.ClientID 
JOIN 
    Transaction T ON A.AccountID = T.AccountID 
WHERE 
    T.TransactionDate >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH) 
GROUP BY 
    C.ClientID, 
    CONCAT(C.FirstName, ' ', C.LastName) 
HAVING 
    COUNT(T.TransactionID) > 10
"""

#Display Clients with 10 or more Transactions   
cursor.execute(query_high_transaction_clients)
tables = cursor.fetchall()
print("-- Clients with a High Number of Transactions --")
for table in tables:
    print(f"ClientID: {table[0]}\nClientName: {table[1]}\nNumberofTransactions: {table[2]}\n")

# Wait for user input so that info can be read, then close database
input("\nPress Enter key to close Database...")
cursor.close()
db.close()