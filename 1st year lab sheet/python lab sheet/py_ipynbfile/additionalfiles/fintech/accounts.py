#5
# 4

class Account:
    instance_count = 0  # Class variable to keep track of instances

    def __init__(self, account_number, account_holder, opening_balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self._balance = opening_balance  # Private attribute
        
        Account.instance_count += 1
        print(f"New account instance created. Total instances: {Account.instance_count}")
    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise AmountError(self, "Cannot withdraw negative amounts")
        if self._balance - amount >= -100.0:  # Overdraft limit threshold
            self._balance -= amount
        else:
            raise BalanceError(self)

    def __str__(self):
        return f'Account[{self.account_number}] - {self.account_holder}, balance = {self._balance}'


    def __str__(self):
        return f'Account[{self.account_number}] - {self.account_holder}, balance = {self._balance}'


class CurrentAccount(Account):
    def __init__(self, account_number, account_holder, opening_balance, overdraft_limit):
        super().__init__(account_number, account_holder, opening_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount < 0:
            raise AmountError(self, "Cannot withdraw negative amounts")
        if self._balance - amount >= -self.overdraft_limit:
            self._balance -= amount
        else:
            raise BalanceError(self)

class DepositAccount(Account):
    def __init__(self, account_number, account_holder, opening_balance, interest_rate):
        super().__init__(account_number, account_holder, opening_balance)
        self.interest_rate = interest_rate

    def __str__(self):
        return f'Deposit Account[{self.account_number}] - {self.account_holder}, balance = {self._balance}, ' \
               f'interest rate = {self.interest_rate}'


class InvestmentAccount(Account):
    def __init__(self, account_number, account_holder, opening_balance, investment_type):
        super().__init__(account_number, account_holder, opening_balance)
        self.investment_type = investment_type

    def __str__(self):
        return f'Investment Account[{self.account_number}] - {self.account_holder}, balance = {self._balance}, ' \
               f'investment type = {self.investment_type}'

class AmountError(Exception):
    def __init__(self, account, message):
        super().__init__(f"{type(self).__name__} ({message}) on {account}")


class BalanceError(Exception):
    def __init__(self, account):
        super().__init__(f"BalanceError (Balance would go below overdraft limit) on {account}")


# Test Application
acc1 = CurrentAccount('123', 'John', 10.05, 100.0)

try:
    acc1.deposit(-1)
except AmountError as e:
    print(e)

try:
    acc1.deposit(23.45)
    acc1.withdraw(12.33)
    print('balance:', acc1.balance)
    acc1.withdraw(300.00)
    print('balance:', acc1.balance)
except BalanceError as e:
    print('Handling Exception')
    print(e)
