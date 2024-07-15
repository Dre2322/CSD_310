import mysql.connector

db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'yourpassword', auth_plugin = 
                             'mysql_native_password')

cursor = db.cursor()

#Create the Database and select it
cursor.execute("-- Create the Database and all the respective Tables")
cursor.execute("CREATE DATABASE willson_financial;")
cursor.execute("USE willson_financial;")

#Create the new fresh Database Tables
cursor.execute("-- Create the new fresh Tables for the Database")
cursor.execute("-- Create the Employee Table")
cursor.execute("CREATE TABLE Employee (EmployeeID int NOT NULL AUTO_INCREMENT, FirstName varchar(50) NOT NULL, "
               "LastName varchar(50) NOT NULL, Position varchar(50) NOT NULL, HireDate date NOT NULL, "
               "PRIMARY KEY(EmployeeID));")

cursor.execute("-- Create the Compliance Manager Table")
cursor.execute("""CREATE TABLE ComplianceManager (ComplianceManagerID int NOT NULL, 
               ComplianceDetails varchar(2000) NOT NULL, PRIMARY KEY(ComplianceManagerID), 
               FOREIGN KEY(ComplianceManagerID) REFERENCES Employee(EmployeeID));""")

cursor.execute("-- Create the Compliance Activity Table")
cursor.execute("""CREATE TABLE ComplianceActivity (ComplianceActivityID int NOT NULL AUTO_INCREMENT, 
               ComplianceManagerID int NOT NULL, ActivityDate date NOT NULL, ActivityType varchar(255) 
               NOT NULL, Description varchar(2000) NOT NULL, PRIMARY KEY(ComplianceActivityID), 
               CONSTRAINT fk_ComplianceManager FOREIGN KEY(ComplianceManagerID) REFERENCES 
               ComplianceManager(ComplianceManagerID));""")

cursor.execute("-- Create the Client Table")
cursor.execute("""CREATE TABLE Client (ClientID int NOT NULL AUTO_INCREMENT, FirstName varchar(50) NOT NULL, 
               LastName varchar(50) NOT NULL, Address varchar(80) NOT NULL, PhoneNumber varchar(20) NOT NULL, 
               Email varchar(50) NOT NULL, DateAdded date NOT NULL, TotalAccounts int NOT NULL, 
               PRIMARY KEY(ClientID));""")

cursor.execute("-- Create the Employee to Client Relationship Table")
cursor.execute("""CREATE TABLE EmployeeClient (EmployeeID int NOT NULL AUTO_INCREMENT, ClientID int NOT NULL, 
               Role varchar (50) NOT NULL, FOREIGN KEY(EmployeeID) REFERENCES Employee(EmployeeID), 
               FOREIGN KEY(ClientID) REFERENCES Client(ClientID));""")

cursor.execute("-- Create the Accounts Table")
cursor.execute("""CREATE TABLE Account (AccountID int NOT NULL AUTO_INCREMENT, ClientID int NOT NULL, 
               Balance dec(15, 2) NOT NULL, AccountType varchar(50) NOT NULL, OpenDate date NOT NULL, 
               PRIMARY KEY (AccountID), FOREIGN KEY(ClientID) REFERENCES Client(ClientID));""")

cursor.execute("-- Create the Billing Table")
cursor.execute("""CREATE TABLE Billing (BillingID int NOT NULL AUTO_INCREMENT, ClientID int NOT NULL, 
               Amount dec(15, 2) NOT NULL, BillingDate date NOT NULL, BillingPeriod varchar(10) NOT NULL, 
               PRIMARY KEY(BillingID), FOREIGN KEY(ClientID) REFERENCES Client(ClientID));""")

cursor.execute("-- Create the Transactions Table")
cursor.execute("""CREATE TABLE Transaction (TransactionID int NOT NULL AUTO_INCREMENT, AccountID int NOT NULL, 
               TransactionDate date NOT NULL, Amount dec(15, 2) NOT NULL, TransactionType varchar(50) 
               NOT NULL, PRIMARY KEY(TransactionID), CONSTRAINT fk_Account FOREIGN KEY(AccountID) REFERENCES 
               Account(AccountID));""")


#Input the Employee Data, should be four employees total
cursor.execute("-- Input the Employee Data, should be four employees total")
cursor.execute("""INSERT INTO Employee (EmployeeID, FirstName, LastName, Position, HireDate) VALUES
               ('1', 'Jake', 'Willson', 'Financial Advisor', '2023-11-12'),
               ('2', 'Ned', 'Willson', 'Financial Advisor', '2023-11-12'),
               ('3', 'Pheonix', 'Two Star', 'Secretary', '2023-11-12'),
               ('4', 'June', 'Santos', 'Compliance Manager', '2023-11-12');""")

#Input the Compliance Manager Data
cursor.execute("-- Input the Compliance Manager Data")
cursor.execute("""INSERT INTO ComplianceManager (ComplianceManagerID, ComplianceDetails) 
               VALUES((SELECT EmployeeID FROM Employee WHERE Position = 'Compliance Manager'), 
               'Ensures SEC Compliance');""")

#Input the Compliance Activity Data
cursor.execute("-- Input the Compliance Activity Data")
cursor.execute("""INSERT INTO ComplianceActivity (ComplianceActivityID, ComplianceManagerID, ActivityDate, 
               ActivityType, Description) VALUES
               ('1', (SELECT ComplianceManagerID FROM ComplianceManager 
               WHERE ComplianceManagerID = 4), '2023-11-13', 'Training', 
               'Staff meeting to go over Compliance Standards for the new business'),
               ('2', (SELECT ComplianceManagerID FROM ComplianceManager 
               WHERE ComplianceManagerID = 4), '2024-01-16', 'Inspection', 
               'Internal inspection of business process'),
               ('3', (SELECT ComplianceManagerID FROM ComplianceManager 
               WHERE ComplianceManagerID = 4), '2024-01-30', 'Review', 
               'Reviewed new client records for compliance'),
               ('4', (SELECT ComplianceManagerID FROM ComplianceManager 
               WHERE ComplianceManagerID = 4), '2024-01-31', 'Report', 
               'Filed Compliance Report with SEC'),
               ('5', (SELECT ComplianceManagerID FROM ComplianceManager 
               WHERE ComplianceManagerID = 4), '2024-02-05', 'Meeting', 
               'Meeting to review results of Compliance Report'),
               ('6', (SELECT ComplianceManagerID FROM ComplianceManager 
               WHERE ComplianceManagerID = 4), '2024-02-20', 'Inspection', 
               'Internal inspection of business processes'),
               ('7', (SELECT ComplianceManagerID FROM ComplianceManager 
               WHERE ComplianceManagerID = 4), '2024-02-28', 'Report', 
               'Filed Compliance Report with SEC'),
               ('8', (SELECT ComplianceManagerID FROM ComplianceManager 
               WHERE ComplianceManagerID = 4), '2024-03-04', 'Meeting', 
               'Meeting to review results of Compliance Report'),
               ('9', (SELECT ComplianceManagerID FROM ComplianceManager 
               WHERE ComplianceManagerID = 4), '2024-03-07', 'Training', 
               'Staff meeting to review Compliance Standards'),
               ('10', (SELECT ComplianceManagerID FROM ComplianceManager 
               WHERE ComplianceManagerID = 4), '2024-03-31', 'Report', 
               'Filed Compliance Report with SEC'),
               ('11', (SELECT ComplianceManagerID FROM ComplianceManager 
               WHERE ComplianceManagerID = 4), '2024-04-05', 'Meeting', 
               'Meeting to review results of Compliance Report'),
               ('12', (SELECT ComplianceManagerID FROM ComplianceManager 
               WHERE ComplianceManagerID = 4), '2024-04-14', 'Audit', 
               'Quarterly audit of all financial transactions'),
               ('13', (SELECT ComplianceManagerID FROM ComplianceManager 
               WHERE ComplianceManagerID = 4), '2024-07-01', 'Audit', 
               'Quarterly audit of all financial records'),
               ('14', (SELECT ComplianceManagerID FROM ComplianceManager 
               WHERE ComplianceManagerID = 4), '2024-07-05', 'Training', 
               'Compliance training for all staff'),
               ('15', (SELECT ComplianceManagerID FROM ComplianceManager 
               WHERE ComplianceManagerID = 4), '2024-07-10', 'Report', 
               'Filed compliance report with SEC'),
               ('16', (SELECT ComplianceManagerID FROM ComplianceManager 
               WHERE ComplianceManagerID = 4), '2024-07-15', 'Review', 
               'Reviewed new client records for compliance'),
               ('17', (SELECT ComplianceManagerID FROM ComplianceManager 
               WHERE ComplianceManagerID = 4), '2024-07-20', 'Inspection', 
               'Internal inspection of financial processes'),
               ('18', (SELECT ComplianceManagerID FROM ComplianceManager 
               WHERE ComplianceManagerID = 4), '2024-07-25', 'Meeting', 
               'Compliance meeting with management');""")

#Input the Client Data
cursor.execute("-- Input the Client Data")
cursor.execute("""INSERT INTO Client (ClientID, FirstName, LastName, Address, PhoneNumber, Email, DateAdded, 
               TotalAccounts) VALUES
               ('1', 'William', 'Harris', '827-172-2836', '123 Rose St', 
               'W.Harris@yahoo.com', '2023-11-13', '1'),
               ('2', 'Peter', 'Smith', '871-384-2910', '456 Lily Ln', 
               'P.Smith@gmail.com', '2023-11-25', '1'),
               ('3', 'Timothy', 'Brown', '762-918-7648', '789 Carnation Ct', 
               'T.Brown@msn.com', '2023-12-02', '1'),
               ('4', 'Gina', 'Fisher', '871-889-8473', '101 Daisy Blvd', 
               'G.Fisher@aol.com', '2023-12-15', '1'),
               ('5', 'Roberta', 'Cooper', '829-324-3298', '112 Tulip Ln', 
               'R.Cooper@yahoo.com', '2023-12-28', '1'),
               ('6', 'Samuel', 'Cross', '871-281-9872', '134 Orchid St', 
               'S.Cross@yahoo.com', '2024-01-07', '1'),
               ('7', 'Alice', 'Johnson', '632-555-1234', '123 Elm St', 
               'alice@aol.com', '2024-01-01', '2'),
               ('8', 'Bob', 'Smith', '295-555-5678', '456 Oak St', 
               'bob@gmail.com', '2024-01-01', '1'),
               ('9', 'Bob', 'Grayson', '513-654-9697', '8374 Keening Way', 
               'bob.grayson@gmail.com', '2024-01-14', '1'),
               ('10', 'Steve', 'Smith', '632-975-9302', '7454 Smith Ave', 
               'steve.smith@gmail.com', '2024-01-20', '1'),
               ('11', 'Heather', 'Grant', '295-942-2452', '9502 Turtle Dr', 
               'hgrant2076@aol.com', '2024-02-03', '1'),
               ('12', 'Gina', 'Swarez', '513-928-5923', '859 Deter Lane', 
               'ginaswarez11@yahoo.com', '2024-02-13', '2'),
               ('13', 'Charlie', 'Brown', '513-555-9012', '789 Pine St', 
               'charlie@sbcglobal.net', '2024-03-01', '1'),
               ('14', 'Hank', 'Ross', '632-204-9255', '309 Spring Pine St', 
               'hank.ross@gmail.com', '2024-03-26', '1'),
               ('15', 'Diana', 'Prince', '632-555-3456', '101 Maple St', 
               'diana@yahoo.com', '2024-04-01', '1'),
               ('16', 'Edward', 'Nigma', '513-555-7890', '202 Birch St', 
               'edward@aol.com', '2024-05-01', '1'),
               ('17', 'Fiona', 'Shrek', '295-555-2345', '303 Cedar St', 
               'fiona@aol.com', '2024-06-01', '1');""")

#Input the Employee to Client Relationship Table Data
cursor.execute("-- Input the Employee to Client Relationship Table Data")
cursor.execute("""INSERT INTO EmployeeClient (EmployeeID, ClientID, Role) VALUES
               ((SELECT EmployeeID FROM Employee WHERE EmployeeID = 1), (SELECT ClientID FROM 
               Client WHERE ClientID = 1), 'Financial Advisor'),
               ((SELECT EmployeeID FROM Employee WHERE EmployeeID = 2), (SELECT ClientID FROM 
               Client WHERE ClientID = 2), 'Financial Advisor'),
               ((SELECT EmployeeID FROM Employee WHERE EmployeeID = 2), (SELECT ClientID FROM 
               Client WHERE ClientID = 3), 'Financial Advisor'),
               ((SELECT EmployeeID FROM Employee WHERE EmployeeID = 1), (SELECT ClientID FROM 
               Client WHERE ClientID = 4), 'Financial Advisor'),
               ((SELECT EmployeeID FROM Employee WHERE EmployeeID = 1), (SELECT ClientID FROM 
               Client WHERE ClientID = 5), 'Financial Advisor'),
               ((SELECT EmployeeID FROM Employee WHERE EmployeeID = 2), (SELECT ClientID FROM 
               Client WHERE ClientID = 6), 'Financial Advisor'),
               ((SELECT EmployeeID FROM Employee WHERE EmployeeID = 1), (SELECT ClientID FROM 
               Client WHERE ClientID = 7), 'Financial Advisor'),
               ((SELECT EmployeeID FROM Employee WHERE EmployeeID = 1), (SELECT ClientID FROM 
               Client WHERE ClientID = 8), 'Financial Advisor'),
               ((SELECT EmployeeID FROM Employee WHERE EmployeeID = 1), (SELECT ClientID FROM 
               Client WHERE ClientID = 9), 'Financial Advisor'),
               ((SELECT EmployeeID FROM Employee WHERE EmployeeID = 2), (SELECT ClientID FROM 
               Client WHERE ClientID = 10), 'Financial Advisor'),
               ((SELECT EmployeeID FROM Employee WHERE EmployeeID = 1), (SELECT ClientID FROM 
               Client WHERE ClientID = 11), 'Financial Advisor'),
               ((SELECT EmployeeID FROM Employee WHERE EmployeeID = 2), (SELECT ClientID FROM 
               Client WHERE ClientID = 12), 'Financial Advisor'),
               ((SELECT EmployeeID FROM Employee WHERE EmployeeID = 1), (SELECT ClientID FROM 
               Client WHERE ClientID = 13), 'Financial Advisor'),
               ((SELECT EmployeeID FROM Employee WHERE EmployeeID = 2), (SELECT ClientID FROM 
               Client WHERE ClientID = 14), 'Financial Advisor'),
               ((SELECT EmployeeID FROM Employee WHERE EmployeeID = 2), (SELECT ClientID FROM 
               Client WHERE ClientID = 15), 'Financial Advisor'),
               ((SELECT EmployeeID FROM Employee WHERE EmployeeID = 2), (SELECT ClientID FROM 
               Client WHERE ClientID = 16), 'Financial Advisor'),
               ((SELECT EmployeeID FROM Employee WHERE EmployeeID = 2), (SELECT ClientID FROM 
               Client WHERE ClientID = 17), 'Financial Advisor');""")


#Input the Account Data
cursor.execute("-- Input the Account Data")
cursor.execute("""INSERT INTO Account (AccountID, ClientID, Balance, AccountType, OpenDate) VALUES
               ('1', (SELECT ClientID FROM Client WHERE ClientID = 1), '10000', 'Investment', '2023-11-13'),
               ('2', (SELECT ClientID FROM Client WHERE ClientID = 2), '5000', 'Checking', '2023-11-25'),
               ('3', (SELECT ClientID FROM Client WHERE ClientID = 3), '3000', 'Retirement', '2023-12-02'),
               ('4', (SELECT ClientID FROM Client WHERE ClientID = 4), '50000', 'Brokerage', '2023-12-15'),
               ('5', (SELECT ClientID FROM Client WHERE ClientID = 5), '25000', 'Retirement', '2023-12-28'),
               ('6', (SELECT ClientID FROM Client WHERE ClientID = 6), '1000', 'Brokerage', '2024-01-07'),
               ('7', (SELECT ClientID FROM Client WHERE ClientID = 7), '15000', 'Savings', '2024-01-01'),
               ('8', (SELECT ClientID FROM Client WHERE ClientID = 7), '5000', 'Checking', '2024-01-01'),
               ('9', (SELECT ClientID FROM Client WHERE ClientID = 8), '25000', 'Investment', '2024-02-01'),
               ('10', (SELECT ClientID FROM Client WHERE ClientID = 9), '20000', 'Savings', '2024-01-14'),
               ('11', (SELECT ClientID FROM Client WHERE ClientID = 10), '50000', 'Checking', '2024-01-20'),
               ('12', (SELECT ClientID FROM Client WHERE ClientID = 11), '100000', 'Checking', '2024-02-03'),
               ('13', (SELECT ClientID FROM Client WHERE ClientID = 12), '60000', 'Savings', '2024-02-13'),
               ('14', (SELECT ClientID FROM Client WHERE ClientID = 13), '10000', 'Savings', '2024-03-01'),
               ('15', (SELECT ClientID FROM Client WHERE ClientID = 14), '50000', 'Investment', '2024-03-26'),
               ('16', (SELECT ClientID FROM Client WHERE ClientID = 15), '2000', 'Checking', '2024-04-01'),
               ('17', (SELECT ClientID FROM Client WHERE ClientID = 12), '25000', 'Investment', '2024-04-03'),
               ('18', (SELECT ClientID FROM Client WHERE ClientID = 16), '30000', 'Investment', '2024-05-01'),
               ('19', (SELECT ClientID FROM Client WHERE ClientID = 17), '10000', 'Savings', '2024-06-01');""")

#Input the Billing Data
cursor.execute("-- Input the Billing Data")
cursor.execute("""INSERT INTO Billing (BillingID, ClientId, Amount, BillingDate, BillingPeriod) VALUES
               ('1', (SELECT ClientID FROM Client WHERE ClientID = 1), '900', '2023-11-13', 'Quarterly'),
               ('2', (SELECT ClientID FROM Client WHERE ClientID = 2), '180', '2023-11-13', 'Quarterly'),
               ('3', (SELECT ClientID FROM Client WHERE ClientID = 3), '0', '2023-12-02', 'Quarterly'),
               ('4', (SELECT ClientID FROM Client WHERE ClientID = 4), '4500', '2023-12-15', 'Quarterly'),
               ('5', (SELECT ClientID FROM Client WHERE ClientID = 5), '0', '2023-12-28', 'Quarterly'),
               ('6', (SELECT ClientID FROM Client WHERE ClientID = 6), '60', '2024-01-07', 'Quarterly'),
               ('7', (SELECT ClientID FROM Client WHERE ClientID = 7), '150', '2024-01-01', 'Quarterly'),
               ('8', (SELECT ClientID FROM Client WHERE ClientID = 8), '200', '2024-02-01', 'Quarterly'),
               ('9', (SELECT ClientID FROM Client WHERE ClientID = 9), '150', '2024-01-14', 'Quarterly'),
               ('10', (SELECT ClientID FROM Client WHERE ClientID = 10), '223.75', '2024-01-20', 'Quarterly'),
               ('11', (SELECT ClientID FROM Client WHERE ClientID = 11), '271.25', '2024-02-03', 'Quarterly'),
               ('12', (SELECT ClientID FROM Client WHERE ClientID = 12), '212.50', '2024-02-13', 'Quarterly'),
               ('13', (SELECT ClientID FROM Client WHERE ClientID = 13), '250', '2024-03-01', 'Quarterly'),
               ('14', (SELECT ClientID FROM Client WHERE ClientID = 14), '125', '2024-03-26', 'Quarterly'),
               ('15', (SELECT ClientID FROM Client WHERE ClientID = 15), '300', '2024-04-01', 'Quarterly'),
               ('16', (SELECT ClientID FROM Client WHERE ClientID = 16), '350', '2024-05-01', 'Quarterly'),
               ('17', (SELECT ClientID FROM Client WHERE ClientID = 17), '400', '2024-06-01', 'Quarterly');""")

#Input the Transaction Data
cursor.execute("-- Input the Transaction Data")
cursor.execute("""INSERT INTO Transaction (TransactionID, AccountID, TransactionDate, Amount, TransactionType) VALUES
               ('1', (SELECT AccountID FROM Account WHERE AccountID = 1), '2023-11-13', '10000', 'Deposit'),
               ('2', (SELECT AccountID FROM Account WHERE AccountID = 2), '2023-11-25', '3000', 'Deposit'),
               ('3', (SELECT AccountID FROM Account WHERE AccountID = 3), '2023-12-02', '1500', 'Deposit'),
               ('4', (SELECT AccountID FROM Account WHERE AccountID = 4), '023-12-15', '40000', 'Deposit'),
               ('5', (SELECT AccountID FROM Account WHERE AccountID = 5), '2023-12-28', '20000', 'Deposit'),
               ('6', (SELECT AccountID FROM Account WHERE AccountID = 6), '2024-01-07', '500', 'Deposit'),
               ('7', (SELECT AccountID FROM Account WHERE AccountID = 10), '2024-01-14', '20000', 'Deposit'),
               ('8', (SELECT AccountID FROM Account WHERE AccountID = 11), '2024-01-20', '50000', 'Deposit'),
               ('9', (SELECT AccountID FROM Account WHERE AccountID = 12), '2024-02-03', '100000', 'Deposit'),
               ('10', (SELECT AccountID FROM Account WHERE AccountID = 11), '2024-02-04', '10000', 'Deposit'),
               ('11', (SELECT AccountID FROM Account WHERE AccountID = 13), '2024-02-13', '60000', 'Deposit'),
               ('12', (SELECT AccountID FROM Account WHERE AccountID = 10), '2024-02-14', '20000', 'Deposit'),
               ('13', (SELECT AccountID FROM Account WHERE AccountID = 12), '2024-02-25', '1500', 'Withdraw'),
               ('14', (SELECT AccountID FROM Account WHERE AccountID = 12), '2024-03-01', '10000', 'Deposit'),
               ('15', (SELECT AccountID FROM Account WHERE AccountID = 11), '2024-03-07', '500', 'Withdraw'),
               ('16', (SELECT AccountID FROM Account WHERE AccountID = 15), '2024-03-26', '50000', 'Deposit'),
               ('17', (SELECT AccountID FROM Account WHERE AccountID = 13), '2024-04-03', '25000', 'Deposit'),
               ('18', (SELECT AccountID FROM Account WHERE AccountID = 11), '2024-04-05', '30000', 'Deposit'),
               ('19', (SELECT AccountID FROM Account WHERE AccountID = 10), '2024-04-10', '20000', 'Deposit'),
               ('20', (SELECT AccountID FROM Account WHERE AccountID = 7), '2024-07-01', '500', 'Deposit'),
               ('21', (SELECT AccountID FROM Account WHERE AccountID = 7), '2024-07-02', '200', 'Withdraw'),
               ('22', (SELECT AccountID FROM Account WHERE AccountID = 9), '2024-07-03', '1000', 'Deposit'),
               ('23', (SELECT AccountID FROM Account WHERE AccountID = 13), '2024-07-04', '500', 'Withdraw'),
               ('24', (SELECT AccountID FROM Account WHERE AccountID = 16), '2024-07-05', '300', 'Deposit'),
               ('25', (SELECT AccountID FROM Account WHERE AccountID = 18), '2024-07-06', '1500', 'Deposit'),
               ('26', (SELECT AccountID FROM Account WHERE AccountID = 19), '2024-07-08', '2000', 'Deposit');""")


#Display the Employee Table
cursor.execute("-- Display the Employee Table")
cursor.execute("SELECT * FROM Employee;")

tables = cursor.fetchall()
print("\n -- Employees --") #Print the appropriate title

for table in tables: #Using a for loop, print the information from the table
    print("Employee ID: {}\nFirst Name: {}\nLast Name: {}\nPosition: {}\nHire Date: {}\n"
          .format(table[0], table[1], table[2], table[3], table[4]))
    
#Display the Compliance Manager Table
cursor.execute("-- Display the Compliance Manager Table")
cursor.execute("SELECT * FROM ComplianceManager;")

tables = cursor.fetchall()
print("\n -- Compliance Manager --") #Print the appropriate title

for table in tables: #Using a for loop, print the information from the table
    print("Compliance Manager ID: {}\nCompliance Details: {}\n".format(table[0], table[1]))

#Display the Compliance Activity Table
cursor.execute("-- Display the Compliance Activity Table")
cursor.execute("SELECT * FROM ComplianceActivity;")

tables = cursor.fetchall()
print("\n -- Compliance Activity --") #Print the appropriate title

for table in tables: #Using a for loop, print the information from the table
    print("""Compliance Activity ID: {}\nCompliance Manager ID: {}\nActivity Date: {}\nActivity Type: {}\nDescription: {}\n"""
          .format(table[0], table[1], table[2], table[3], table[4]))
    
#Display the Employee/Client Table
cursor.execute("-- Display the Employee/Client Table")
cursor.execute("SELECT * FROM EmployeeClient;")

tables = cursor.fetchall()
print("\n -- Employees/Clients --") #Print the appropriate title

for table in tables: #Using a for loop, print the information from the table
    print("Employee ID: {}\nClient ID: {}\nRole: {}\n".format(table[0], table[1], table[2]))

#Display the Client Table
cursor.execute("-- Display the Client Table")
cursor.execute("SELECT * FROM Client;")

tables = cursor.fetchall()
print("\n -- Clients --") #Print the appropriate title

for table in tables: #Using a for loop, print the information from the table
    print("""Client ID: {}\nFirst Name: {}\nLast Name: {}\nAddress: {}\nPhone Number: {}\nEmail: {}\nDate Added: {}\nTotal Accounts: {}\n"""
          .format(table[0], table[1], table[2], table[3], table[4], table[5], table[6], table[7]))

#Display the Accounts Table
cursor.execute("-- Display the Accounts Table")
cursor.execute("SELECT * FROM Account;")

tables = cursor.fetchall()
print("\n -- Accounts --") #Print the appropriate title

for table in tables: #Using a for loop, print the information from the table
    print("Account ID: {}\nClient ID: {}\nBalance: {}\nAccount Type: {}\nOpen Date: {}\n"
          .format(table[0], table[1], table[2], table[3], table[4]))
    
#Display the Billing Table
cursor.execute("-- Display the Billing Table")
cursor.execute("SELECT * FROM Billing;")

tables = cursor.fetchall()
print("\n -- Billing --") #Print the appropriate title

for table in tables: #Using a for loop, print the information from the table
    print("Billing ID: {}\nClient ID: {}\nAmount: {}\nBilling Date: {}\nBilling Period: {}\n"
          .format(table[0], table[1], table[2], table[3], table[4]))

#Display the Transactions Table
cursor.execute("-- Display the Transactions Table")
cursor.execute("SELECT * FROM Transaction;")

tables = cursor.fetchall()
print("\n -- Transactions --") #Print the appropriate title

for table in tables: #Using a for loop, print the information from the table
    print("Transaction ID: {}\nAccount ID: {}\nTransaction Date: {}\nAmount: {}\nTransaction Type: {}\n"
          .format(table[0], table[1], table[2], table[3], table[4]))


input("\nPress any key to close Database...") #Wait for user input so that info can be read, then close database
db.close()