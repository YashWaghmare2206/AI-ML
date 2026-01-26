import json
import os
from bank_Classes import *

# Function to save all data to JSON
def save_to_json():
    data = {
        "last_id": BankAccount._id_counter,
        "accounts": [acc.to_dict() for acc in BankAccount.acc_list]
    }
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

# Function to load data from JSON
def load_from_json():
    if not os.path.exists("data.json"):
        return

    with open("data.json", "r") as f:
        data = json.load(f)

    # Sync the ID counter so the next new account gets the correct ID
    BankAccount._id_counter = data["last_id"]

    for acc in data["accounts"]:
        # We manually assign the ID back to the object after creation
        # to ensure it matches the stored data perfectly.
        if acc["type"] == "SAVINGS":
            new_acc = SavingAccount(acc["type"], acc["name"], acc["balance"])
        else:
            new_acc = CheckingAccount(acc["type"], acc["name"], acc["balance"])

        # Override the auto-generated ID with the one from the file
        new_acc.id = acc["id"]

# Initialize data at startup
load_from_json()

print("Welcome to Bank System")

while True:
    print("\n1: Create Account | 2: Deposit | 3: Withdraw | 4: Check Balance")
    print("5: Get Overdraft | 6: Get all Accounts | 7: Exit System")

    try:
        ch = int(input("Choice: "))

        if ch == 7:
            save_to_json()
            print("Closing... Data Saved.")
            break

        if ch == 1:
            t = input("Type (SAVINGS/CHECKING): ").upper()
            name = input("Name: ")
            bal = float(input("Balance: "))
            if t == "SAVINGS":
                a = SavingAccount(t, name, bal)
            else:
                a = CheckingAccount(t, name, bal)
            print(f"Account created! ID is: {a.id}")
            save_to_json() # Save immediately after creation
            continue

        if ch == 6:
            print("All accounts:")
            BankAccount.get_all_acc()
            continue

        # For choices 2, 3, 4, 5, we need to locate the account
        acc_id = int(input("Enter account ID: "))
        a = BankAccount.get_acc(acc_id)

        if ch == 2:
            amt = float(input("Amount to deposit: "))
            a.deposit(amt)
        elif ch == 3:
            amt = float(input("Amount to withdraw: "))
            a.withdraw(amt)
        elif ch == 4:
            print(f"Balance: {a.get_balance()}")
        elif ch == 5:
            if isinstance(a, CheckingAccount):
                a.get_overdraft()
                print("Overdraft applied.")
            else:
                raise NoOverDraft(a.acc_type)

        save_to_json() # Save after every successful transaction

    except (NegativeAmount, LowBalance, NoOverDraft, NoAccount) as e:
        print(f"Error: {e}")
    except ValueError:
        print("Invalid input! Please enter numbers where required.")