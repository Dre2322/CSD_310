import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='yourpassword!',
    auth_plugin='mysql_native_password'
)

cursor = db.cursor()

# Create the Database and select it
cursor.execute("CREATE DATABASE IF NOT EXISTS willson_financial")
cursor.execute("USE willson_financial;")

# Disable foreign key checks
cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")

# Drop tables in the correct order
tables_to_drop = [
    "EmployeeClient",
    "ComplianceManager",
    "Transaction",
    "Account",
    "Employee",
    "Client"
]

for table in tables_to_drop:
    cursor.execute(f"DROP TABLE IF EXISTS {table}")

# Re-enable foreign key checks
cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")

# Create the new fresh Database Tables
cursor.execute("""
CREATE TABLE Employee (
    EmployeeID int NOT NULL AUTO_INCREMENT, 
    FirstName varchar(50) NOT NULL, 
    LastName varchar(50) NOT NULL, 
    Position varchar(50) NOT NULL, 
    HireDate date NOT NULL, 
    PRIMARY KEY(EmployeeID)
);
""")

cursor.execute("""
CREATE TABLE ComplianceManager (
    ComplianceManagerID int NOT NULL, 
    ComplianceDetails varchar(2000) NOT NULL, 
    PRIMARY KEY(ComplianceManagerID), 
    FOREIGN KEY(ComplianceManagerID) REFERENCES Employee(EmployeeID)
);
""")

cursor.execute("""
CREATE TABLE Client (
    ClientID int NOT NULL AUTO_INCREMENT, 
    FirstName varchar(50) NOT NULL, 
    LastName varchar(50) NOT NULL, 
    Address varchar(80) NOT NULL, 
    PhoneNumber varchar(20) NOT NULL, 
    Email varchar(50) NOT NULL, 
    DateAdded date NOT NULL, 
    TotalAccounts int NOT NULL, 
    PRIMARY KEY(ClientID)
);
""")

cursor.execute("""
CREATE TABLE EmployeeClient (
    EmployeeID int NOT NULL, 
    ClientID int NOT NULL, 
    Role varchar (50) NOT NULL, 
    FOREIGN KEY(EmployeeID) REFERENCES Employee(EmployeeID), 
    FOREIGN KEY(ClientID) REFERENCES Client(ClientID),
    PRIMARY KEY (EmployeeID, ClientID)
);
""")

cursor.execute("""
CREATE TABLE Account (
    AccountID int NOT NULL AUTO_INCREMENT, 
    ClientID int NOT NULL, 
    Balance dec(15, 2) NOT NULL, 
    AccountType varchar(50) NOT NULL, 
    OpenDate date NOT NULL, 
    PRIMARY KEY (AccountID), 
    FOREIGN KEY(ClientID) REFERENCES Client(ClientID)
);
""")

cursor.execute("""
CREATE TABLE Transaction (
    TransactionID int NOT NULL AUTO_INCREMENT, 
    AccountID int NOT NULL, 
    TransactionDate date NOT NULL, 
    Amount dec(15, 2) NOT NULL, 
    TransactionType varchar(50) NOT NULL, 
    PRIMARY KEY(TransactionID), 
    CONSTRAINT fk_Account FOREIGN KEY(AccountID) REFERENCES Account(AccountID)
);
""")

# Input the Employee Data
cursor.execute("""
INSERT INTO Employee (FirstName, LastName, Position, HireDate) VALUES
('Jake', 'Willson', 'Financial Advisor', '2023-11-12'),
('Ned', 'Willson', 'Financial Advisor', '2023-11-12'),
('Phoenix', 'Two Star', 'Secretary', '2023-11-12'),
('June', 'Santos', 'Compliance Manager', '2023-11-12');
""")

# Input the Compliance Manager Data
cursor.execute("""
INSERT INTO ComplianceManager (ComplianceManagerID, ComplianceDetails) 
VALUES((SELECT EmployeeID FROM Employee WHERE Position = 'Compliance Manager'), 
'Ensures SEC Compliance');
""")

# Input the Client Data
cursor.execute("""
INSERT INTO Client (FirstName, LastName, Address, PhoneNumber, Email, DateAdded, TotalAccounts) VALUES
('William', 'Harris', '123 Rose St', '827-172-2836', 'W.Harris@yahoo.com', '2024-01-13', 1),
('Peter', 'Smith', '456 Lily Ln', '871-384-2910', 'P.Smith@gmail.com', '2024-02-15', 1),
('Timothy', 'Brown', '789 Carnation Ct', '762-918-7648', 'T.Brown@msn.com', '2024-03-10', 1),
('Gina', 'Fisher', '101 Daisy Blvd', '871-889-8473', 'G.Fisher@aol.com', '2024-04-12', 1),
('Roberta', 'Cooper', '112 Tulip Ln', '829-324-3298', 'R.Cooper@yahoo.com', '2024-05-08', 1),
('Samuel', 'Cross', '134 Orchid St', '871-281-9872', 'S.Cross@yahoo.com', '2024-06-07', 1),
('Alice', 'Johnson', '123 Elm St', '632-555-1234', 'alice@aol.com', '2024-06-14', 2),
('Bob', 'Smith', '456 Oak St', '295-555-5678', 'bob@gmail.com', '2024-01-01', 1),
('Bob', 'Grayson', '8374 Keening Way', '513-654-9697', 'bob.grayson@gmail.com', '2024-01-14', 1),
('Steve', 'Smith', '7454 Smith Ave', '632-975-9302', 'steve.smith@gmail.com', '2024-01-20', 1),
('Heather', 'Grant', '9502 Turtle Dr', '295-942-2452', 'hgrant2076@aol.com', '2024-02-03', 1),
('Gina', 'Swarez', '859 Deter Lane', '513-928-5923', 'ginaswarez11@yahoo.com', '2024-02-13', 2),
('Charlie', 'Brown', '789 Pine St', '513-555-9012', 'charlie@sbcglobal.net', '2024-03-01', 1),
('Hank', 'Ross', '309 Spring Pine St', '632-204-9255', 'hank.ross@gmail.com', '2024-03-26', 1),
('Diana', 'Prince', '101 Maple St', '632-555-3456', 'diana@yahoo.com', '2024-04-01', 1),
('Edward', 'Nigma', '202 Birch St', '513-555-7890', 'edward@aol.com', '2024-05-01', 1),
('Fiona', 'Shrek', '303 Cedar St', '295-555-2345', 'fiona@aol.com', '2024-06-01', 1);
""")

# Input the Employee to Client Relationship Table Data
cursor.execute("""
INSERT INTO EmployeeClient (EmployeeID, ClientID, Role) VALUES
(1, 1, 'Financial Advisor'),
(2, 2, 'Financial Advisor'),
(2, 3, 'Financial Advisor'),
(1, 4, 'Financial Advisor'),
(1, 5, 'Financial Advisor'),
(2, 6, 'Financial Advisor'),
(1, 7, 'Financial Advisor'),
(1, 8, 'Financial Advisor'),
(1, 9, 'Financial Advisor'),
(2, 10, 'Financial Advisor'),
(1, 11, 'Financial Advisor'),
(2, 12, 'Financial Advisor'),
(1, 13, 'Financial Advisor'),
(2, 14, 'Financial Advisor'),
(2, 15, 'Financial Advisor'),
(2, 16, 'Financial Advisor'),
(2, 17, 'Financial Advisor');
""")

# Input the Account Data
cursor.execute("""
INSERT INTO Account (ClientID, Balance, AccountType, OpenDate) VALUES
(1, 10000, 'Investment', '2023-11-13'),
(2, 5000, 'Checking', '2023-11-25'),
(3, 3000, 'Retirement', '2023-12-02'),
(4, 50000, 'Brokerage', '2023-12-15'),
(5, 25000, 'Retirement', '2023-12-28'),
(6, 1000, 'Brokerage', '2024-01-07'),
(7, 15000, 'Savings', '2024-01-01'),
(7, 5000, 'Checking', '2024-01-01'),
(8, 25000, 'Investment', '2024-02-01'),
(9, 20000, 'Savings', '2024-01-14'),
(10, 50000, 'Checking', '2024-01-20'),
(11, 100000, 'Checking', '2024-02-03'),
(12, 60000, 'Savings', '2024-02-13'),
(13, 10000, 'Savings', '2024-03-01'),
(14, 50000, 'Investment', '2024-03-26'),
(15, 2000, 'Checking', '2024-04-01'),
(12, 25000, 'Investment', '2024-04-03'),
(16, 30000, 'Investment', '2024-05-01'),
(17, 10000, 'Savings', '2024-06-01');
""")

# Input the Transaction Data
cursor.execute("""
INSERT INTO Transaction (AccountID, TransactionDate, Amount, TransactionType) VALUES
(1, '2023-11-13', 10000, 'Deposit'),
(2, '2023-11-25', 3000, 'Deposit'),
(3, '2023-12-02', 1500, 'Deposit'),
(4, '2023-12-15', 40000, 'Deposit'),
(5, '2023-12-28', 20000, 'Deposit'),
(6, '2024-01-07', 500, 'Deposit'),
(10, '2024-01-14', 20000, 'Deposit'),
(11, '2024-01-20', 50000, 'Deposit'),
(12, '2024-02-03', 100000, 'Deposit'),
(11, '2024-02-04', 10000, 'Deposit'),
(13, '2024-02-13', 60000, 'Deposit'),
(10, '2024-02-14', 20000, 'Deposit'),
(12, '2024-02-25', 1500, 'Withdraw'),
(12, '2024-03-01', 10000, 'Deposit'),
(11, '2024-03-07', 500, 'Withdraw'),
(15, '2024-03-26', 50000, 'Deposit'),
(13, '2024-04-03', 25000, 'Deposit'),
(11, '2024-04-05', 30000, 'Deposit'),
(10, '2024-04-10', 20000, 'Deposit'),
(7, '2024-07-01', 500, 'Deposit'),
(7, '2024-07-02', 200, 'Withdraw'),
(9, '2024-07-03', 1000, 'Deposit'),
(13, '2024-07-04', 500, 'Withdraw'),
(16, '2024-07-05', 300, 'Deposit'),
(18, '2024-07-06', 1500, 'Deposit'),
(19, '2024-07-08', 2000, 'Deposit'),
(8, '2024-07-10', 5000, 'Deposit'),
(8, '2024-07-12', 1000, 'Withdraw'),
(8, '2024-07-15', 3000, 'Deposit'),
(8, '2024-07-17', 2000, 'Withdraw'),
(8, '2024-07-20', 1000, 'Deposit'),
(8, '2024-07-22', 2000, 'Withdraw'),
(8, '2024-07-25', 1500, 'Deposit'),
(8, '2024-07-28', 1000, 'Withdraw'),
(8, '2024-07-30', 2000, 'Deposit'),
(8, '2024-07-31', 500, 'Withdraw');
""")


# Display the Employee Table
cursor.execute("SELECT * FROM Employee;")
tables = cursor.fetchall()
print("\n -- Employees --")
for table in tables:
    print(f"Employee ID: {table[0]}\nFirst Name: {table[1]}\nLast Name: {table[2]}\nPosition: {table[3]}\nHire Date: {table[4]}\n")

# Display the Compliance Manager Table
cursor.execute("SELECT * FROM ComplianceManager;")
tables = cursor.fetchall()
print("\n -- Compliance Manager --")
for table in tables:
    print(f"Compliance Manager ID: {table[0]}\nCompliance Details: {table[1]}\n")

# Display the Employee/Client Table
cursor.execute("SELECT * FROM EmployeeClient;")
tables = cursor.fetchall()
print("\n -- Employees/Clients --")
for table in tables:
    print(f"Employee ID: {table[0]}\nClient ID: {table[1]}\nRole: {table[2]}\n")

# Display the Client Table
cursor.execute("SELECT * FROM Client;")
tables = cursor.fetchall()
print("\n -- Clients --")
for table in tables:
    print(f"Client ID: {table[0]}\nFirst Name: {table[1]}\nLast Name: {table[2]}\nAddress: {table[3]}\nPhone Number: {table[4]}\nEmail: {table[5]}\nDate Added: {table[6]}\nTotal Accounts: {table[7]}\n")

# Display the Accounts Table
cursor.execute("SELECT * FROM Account;")
tables = cursor.fetchall()
print("\n -- Accounts --")
for table in tables:
    print(f"Account ID: {table[0]}\nClient ID: {table[1]}\nBalance: {table[2]}\nAccount Type: {table[3]}\nOpen Date: {table[4]}\n")

# Display the Transactions Table
cursor.execute("SELECT * FROM Transaction;")
tables = cursor.fetchall()
print("\n -- Transactions --")
for table in tables:
    print(f"Transaction ID: {table[0]}\nAccount ID: {table[1]}\nTransaction Date: {table[2]}\nAmount: {table[3]}\nTransaction Type: {table[4]}\n")

input("\nPress Enter key to close Database...")  # Wait for user input so that info can be read, then close database
db.close()
