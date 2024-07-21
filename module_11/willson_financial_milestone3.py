import mysql.connector
import pandas as pd

# Connect to MySQL and use the existing willson_financial database
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='yourpassword!',
    database='willson_financial'
)
cursor = db.cursor()

# Helper function to display and save results
def display_and_save_results(query, description, csv_filename, columns):
    cursor.execute(query)
    results = cursor.fetchall()
    df = pd.DataFrame(results, columns=columns)
    print(f"\n{description}")
    print(df)
    df.to_csv(csv_filename, index=False)

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
display_and_save_results(query_clients_per_month, "Number of Clients Added Per Month", "clients_per_month.csv", ['Month', 'NumberOfClients'])

# Report 2: Average Amount of Assets for the Entire Client List
query_avg_assets_per_client = """
SELECT 
    AVG(Balance) AS AverageAssets 
FROM 
    Account
"""
display_and_save_results(query_avg_assets_per_client, "Average Amount of Assets for the Entire Client List", "avg_assets_per_client.csv", ['AverageAssets'])

# Report 3: Clients with a High Number of Transactions (More Than 10 per Month)
query_high_transaction_clients = """
SELECT 
    C.ClientID, 
    CONCAT(C.FirstName, ' ', C.LastName) AS ClientName, 
    COUNT(T.TransactionID) AS NumberOfTransactions 
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
display_and_save_results(query_high_transaction_clients, "Clients with a High Number of Transactions", "high_transaction_clients.csv", ['ClientID', 'ClientName', 'NumberOfTransactions'])

# Close the cursor and connection
cursor.close()
db.close()

print("Reports generated and saved as CSV files.")
