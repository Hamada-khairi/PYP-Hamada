
# 🏦 Bank Management System

## Overview

The **Bank Management System** is a Python-based, command-line application that simulates a basic banking environment. The system enables users to perform essential banking tasks such as opening new accounts, logging into their accounts, and utilizing a currency converter. Additionally, the system includes a **Super User** account for administrative control. This project is designed as a learning exercise in Python, focusing on user account management, basic banking operations, and system security.

### Project Author:
- **Name:** Mohamed Khairy Mohamed Abdelraouf
- **TP Number:** TP066168

---

## 🛠️ Features

The Bank Management System includes the following key features:

### 1. **Open a New Account**
Users can open one of three types of bank accounts:
- **Islamic Account:** This account follows Sharia principles, avoiding interest-based transactions.
- **Current Account:** Ideal for everyday transactions, this account supports deposits, withdrawals, and transfers.
- **Savings Account:** This account is designed to help users save money over time, possibly earning interest.

Each new account creation requires the user to input personal details such as their name, age, and initial deposit. The system assigns each account a unique account number.

### 2. **User Login**
Once an account is created, the user can log into their account by providing the correct account number and password. Upon successful login, the user can:
- View their account balance
- Make deposits and withdrawals
- View account details
- Log out from the system

### 3. **Currency Converter**
A built-in currency converter allows users to convert their local currency into various foreign currencies. The conversion rates are predefined, and users can input the amount they wish to convert, choosing from several currencies.

### 4. **Super User Access**
The system has a special **Super User** account with administrator privileges. The Super User can:
- View and manage all accounts
- Perform system maintenance
- Reset user passwords

**Super User Credentials:**
- **Username:** MuhammedSU
- **Password:** 12345678

### 5. **Exit/Quit**
The user can choose to exit the application from the main menu, safely terminating their session.

---

## 📂 Project Structure

The project is structured around key functions that handle different aspects of the system. Each function encapsulates a specific feature or task within the system. Below is a breakdown of the main functions and their roles.

### 1. `main_menu()`
This function is the entry point to the system. It continuously displays the main menu until the user selects an option. The menu offers the following choices:
- Open a new account
- Login to an existing account
- Access the currency converter
- Exit the program

#### Example:
```plaintext
*==================================================*
| ---------Welcome to Hamada's Bank Management------ |
*==================================================*
| =<< 1.            Open a new account         >>= |
| =<< 2.                  login                >>= |
| =<< 3.       Currency Converter Calculator   >>= |
| =<< 4.                Exit/Quit              >>= |
*==================================================*
```

### 2. `OPenAccMenu()`
This function handles the "Open a New Account" feature. It presents users with the option to choose between:
- Islamic Account
- Current Account
- Savings Account

After selecting an account type, the user will be prompted to provide personal details and an initial deposit. The system then generates a new account with a unique number.

#### Example:
```plaintext
*==================================================*
| ------- Welcome to Opening Account Menu -------- |
*==================================================*
| =<< 1.              Islamic Account          >>= |
| =<< 2.              Current Account          >>= |
| =<< 3.              Saving Account           >>= |
*==================================================*
```

### 3. `Login()`
The login function allows users to securely access their accounts by entering their account number and password. Once logged in, users have access to various account operations such as:
- **Check Balance:** Displays the current balance of the user's account.
- **Deposit Money:** Allows users to deposit funds into their account.
- **Withdraw Money:** Allows users to withdraw funds (provided there are sufficient funds in the account).
- **View Account Details:** Displays the user's account information including name, age, and account type.
- **Logout:** Logs the user out and returns to the main menu.

### 4. `Currncy_Conv_Calc()`
This function provides a simple currency conversion tool. Users can input an amount in their local currency and convert it to one of several foreign currencies using predefined exchange rates. 

#### Supported Currencies:
- USD (US Dollar)
- EUR (Euro)
- GBP (British Pound)
- JPY (Japanese Yen)

The function ensures that users receive a real-time conversion result based on the chosen currency.

---

## 🧑‍💻 Super User Operations

The **Super User** has access to administrative controls within the system. Once logged in with the special Super User credentials, the administrator can:
- View a list of all accounts
- Delete accounts if necessary
- Reset user passwords
- Perform system maintenance tasks such as cleaning up inactive accounts

The Super User can access these special functions by selecting the relevant option from the main menu.

---

## 🔑 Security

- **Account Numbers:** Each account is uniquely identified by an account number.
- **Passwords:** Passwords are required for both regular user accounts and the Super User account to ensure secure access.
- **Error Handling:** The system validates user inputs to avoid crashes and ensure smooth operation.

---

## 🛠️ How to Run the Project

1. Clone or download the project files to your local machine.
2. Ensure that Python 3.x is installed on your system.
3. Run the project by executing the following command in your terminal or command prompt:

```bash
python bank_system.py
```

Upon running the script, the system will present the main menu. Users can then select an option to perform various operations.

---

## 🔮 Future Enhancements

There are several areas where this project could be extended and improved:
1. **Transaction History:** Implementing a feature to track and display transaction history for each user.
2. **Inter-Account Transfers:** Allowing users to transfer money between different accounts.
3. **Real-Time Currency Rates:** Integrating an API to fetch real-time currency exchange rates.
4. **Interest Calculation for Savings Accounts:** Automatically calculating and applying interest for savings accounts.
5. **Enhanced Security:** Implementing encryption for account data and user passwords for enhanced security.
6. **Graphical User Interface (GUI):** Building a GUI using libraries like `Tkinter` or `PyQt` to make the system more user-friendly.

---

## 👨‍💻 Author

This project was developed by **Mohamed Khairy Mohamed Abdelraouf** as part of a Python learning exercise to simulate a real-world bank management system.

For any questions or contributions, feel free to contact the author.

---

## 📜 License

This project is open-source and free to use for educational purposes. [License]



