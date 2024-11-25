Bank Management System
Overview
This Bank Management System is a simple Python-based program that simulates a basic banking system. Users can create accounts, view account details, credit and debit amounts, and delete accounts. The system stores account information temporarily in a dictionary called bankaccount, with each account uniquely identified by an email address.

Features
Create Account: Allows users to register a new account by providing details such as email, name, age, address, phone number, and gender.
View Account: Retrieves and displays account details using the email ID for login.
Credit Amount: Adds a specified amount to the user's account balance.
Debit Amount: Deducts a specified amount from the user's account balance if sufficient funds are available.
Delete Account: Deletes an existing account after confirmation.


Usage
Run the Program: The program will run continuously until the user chooses the "Exit" option.
User Interface: A command-line menu allows users to navigate through different options.
Code Structure
Dictionary: bankaccount is a dictionary that stores account information, using email IDs as unique keys.


Functions:
createaccount(): Creates a new account with user details.
viewaccount(): Displays account details based on the email ID.
creditamount(): Credits a specified amount to the user's account balance.
debitamount(): Deducts a specified amount from the user's account balance if funds are sufficient.
deleteaccount(): Deletes an account after confirming the user's decision.
Main Loop: The main loop in the main() function provides a menu and prompts the user to select options.


Example Usage
Create an Account: Select "1" and enter details as prompted.
View Account: Select "2" and provide your email ID.
Credit Amount: Select "3" to credit an amount to your balance.
Debit Amount: Select "4" to withdraw an amount from your balance.
Delete Account: Select "5" and confirm deletion when prompted.
Exit: Select "6" to exit the program.


Error Handling
If an invalid email ID is provided during any operation, the program will notify the user.
If the debit amount exceeds the available balance, an "Insufficient balance" message will appear.


Requirements
Python 3.x


Notes
This program does not store data persistently. All data is stored in memory only and will be lost when the program exits.
