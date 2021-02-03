# Bank-Management-System
A banking system that uses the sqlite3 database system with a graphical user interface. Used for the creation, deletion, maintenance of user bank accounts that is stored in a ".db" file. Users are given an account number and they create a password which they can use to log in from time to time. Once logged in, users can view their acount information, deposit/withdraw from their account, or delete their account.
## Instructions
- Requirements: Python 3.9.1 or higher installed
- Clone the "Bank System" directory onto your system. 
- In the terminal, inside the directory run the command. 

          python3 Bank.py

- A GUI should appear on the screen for use.
- When finished using the program, make sure you are logged out and on the "Main Menu" screen before quitting.
## About the Code
### Bank.py
- Bank.py is broken up into two parts:
#### Part 1: sqlite3 database
- Uses the sqlite3 module in Python3 which allows all the data about the individuals to be stored in a database.
- The database stores 7 items: first name, last name, account number, password, balance, latest transaction.
- Functions that allows for user input from the GUI to be inserted, updated, or deleted into the database.
#### Part 2: graphical user interface
- There are 7 frames in total, each frame consists of individual labels and buttons.
- The functions in this section perform tasks such as transitioning between frames, getting user input, taking the user input and calling the functions from the sqlite3 code above.
### Account.py
- Program uses object oriented programming with an Account class.
- Account is used to create objects to keep information about the current user along with defining what actions the users can do.
- Integrated the objects created along with the sqlite3 database to store the information.
### useraccounts.db
- the database file the is used to store all the user information
