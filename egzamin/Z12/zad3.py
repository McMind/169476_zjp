class Account:
    def __init__(self, owner: str, balance: float | int, interest_rate: float | int = 0):
        self.owner = owner
        self.balance = balance
        self.interest_rate = interest_rate

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, new_owner: str):
        if new_owner is None or str(new_owner).strip() == "":
            raise ValueError("Owner cannot be empty")
        self._owner = new_owner.strip()

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance: float | int):
        if new_balance <= 0:
            raise ValueError("Balance has to be positive")
        self._balance = new_balance

    @property
    def interest_rate(self):
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, new_interest_rate: float | int):
        if 0 <= new_interest_rate <= 100:
            self._interest_rate = new_interest_rate
        else:
            raise ValueError("Interest rate has to be between 0 and 100")

    @property
    def final_balance(self):
        return self._balance * (1 + self.interest_rate / 100)

    def __str__(self):
        return f"{self.owner}, ${self.balance}, {self.interest_rate:.2f}% -> ${self.final_balance}"


obj1 = Account("adam", 10000, .75)
print(obj1)
obj1.interest_rate = 1
print(obj1)
try:
    obj1.balance = 0
except ValueError as e:
    print(e)
