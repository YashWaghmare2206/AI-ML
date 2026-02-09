
# 🏦 Banking Management System with JSON Persistence

A Python-based banking application that allows users to create accounts, perform financial transactions, and ensures all data is saved permanently using JSON.

## 📑 Table of Contents

* Features
* File Structure
* Technical Implementation
* Installation & Usage
* Exception Handling
---

## ✨ Features

* **Account Types**: Support for both **Savings** and **Checking** accounts.
* **Persistent Storage**: Uses a `data.json` file to store account balances and user information so data is not lost when the program closes.
* **Automated ID Generation**: A class-level counter ensures every new account receives a unique, incremental ID.
* **Financial Operations**: Deposit, withdraw (with balance checks), and check real-time balances.
* **Overdraft Facility**: Specific to Checking accounts, allowing a credit limit of 500.

---

## 📂 File Structure

1. **`bank_Classes.py`**: Contains the core logic for the `BankAccount` parent class and its children (`SavingAccount`, `CheckingAccount`).
2. **`bank_Exception.py`**: Custom error classes to handle negative deposits, insufficient funds, and invalid account IDs.
3. **`bank_System.py`**: The main execution loop that handles the user interface and JSON saving/loading logic.

---

## ⚙️ Technical Implementation

### The JSON "Bridge"

Since Python objects cannot be saved directly to text files, this project uses a **Serialization** process:

* **`to_dict()`**: Each account object has a method to convert its attributes (ID, Name, Balance) into a dictionary.
* **Metadata**: The system saves the `last_id` used. Upon restarting, it sets the class-level `_id_counter` to this value so new IDs start at the correct number (e.g., if you have 5 accounts, the next created will be 6).

### Class Hierarchy

* **`BankAccount`**: The base class holding shared attributes like `acc_name` and methods like `deposit()`.
* **`SavingAccount`**: Inherits from BankAccount; designed for interest-bearing logic.
* **`CheckingAccount`**: Inherits from BankAccount; includes the `get_overdraft()` method.

---

## 🚀 Installation & Usage

1. **Clone the project** and ensure all three files are in the same folder.
2. **Run the system**:
```bash
python bank_System.py

```


3. **Follow the Menu**:
* Choose **1** to create your first account.
* Choose **7** to exit and save your data to `data.json`.



---

## ⚠️ Exception Handling

The system is robust against user errors:
| Exception | Trigger Condition |
| :--- | :--- |
| **`NegativeAmount`** | User tries to deposit or withdraw a negative number or zero. |
| **`LowBalance`** | Withdrawal amount exceeds the current account balance. |
| **`NoAccount`** | User enters an ID that does not exist in the database. |
| **`NoOverDraft`** | User tries to use the overdraft feature on a Savings account. |

---