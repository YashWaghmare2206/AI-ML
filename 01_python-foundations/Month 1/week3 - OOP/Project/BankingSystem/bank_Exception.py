
class NegativeAmount(Exception):

    def __init__(self , amount):
        self.amount = amount
        super().__init__(f"The amount entered is negative {amount} or 0..Re - enter the value")

class LowBalance(Exception):

    def __init__(self , amount):
        self.amount = amount
        super().__init__(f"You don't have enough balance")

class NoOverDraft(Exception):

    def __init__(self , type):
        super().__init__(f"No Overdraft for this type of account: {type}")

class NoAccount(Exception):

    def __init__(self, acc_id):
        super().__init__(f"Noaccount with id {acc_id}")
