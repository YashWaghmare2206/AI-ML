
from bank_Exception import *



class BankAccount:

    acc_list = []
    _id_counter = 0

    def __init__(self, acc_type, acc_name, acc_balance):
        self.id = BankAccount._generate_id()
        self.acc_type = acc_type
        self.acc_name = acc_name
        self.acc_balance = float(acc_balance) # Ensure it's a number
        BankAccount.acc_list.append(self)

    @classmethod
    def _generate_id(cls):
        cls._id_counter += 1
        return cls._id_counter

    @staticmethod
    def get_acc(acc_id):
        for i in BankAccount.acc_list:
            if i.id == acc_id:
                return i
        raise NoAccount(acc_id)

    def deposit(self , amount):

        if amount <= 0:
            raise NegativeAmount(amount)
        else:
            self.acc_balance += amount

    def withdraw(self , amount):

        if amount <= 0:
            raise NegativeAmount(amount)

        if self.acc_balance < amount:
            raise LowBalance(amount)

        self.acc_balance -= amount
        print("Withdraw Successful")
        print(f"Current Balance is {self.acc_balance}")

    def get_balance(self):
        return self.acc_balance

    @staticmethod
    def get_all_acc():
        for i in BankAccount.acc_list:
            print(i)


    def __str__(self):
        return f"{self.id} | {self.acc_type} | {self.acc_name} | {self.acc_balance}"

    def to_dict(self):

        return {"id": self.id,
                "type": self.acc_type,
                "name": self.acc_name,
                "balance": self.acc_balance
            }

class SavingAccount(BankAccount):

    def __init__(self  ,acc_type , acc_name , acc_balance):
        super().__init__(acc_type , acc_name , acc_balance)

    def interest(self , _rate):
        self.acc_balance += (_rate * self.acc_balance)

class CheckingAccount(BankAccount):

    def __init__(self  , acc_type , acc_name , acc_balance):
        super().__init__(acc_type , acc_name , acc_balance)

    def get_overdraft(self):

        if self.acc_type == "CHECKING":
            limit = 500
            self.acc_balance += limit
        else:
            raise NoOverDraft(self.acc_type)






