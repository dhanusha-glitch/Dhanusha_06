# -------------------- Base Account Class --------------------

class Account:
    def __init__(self, acc_no, holder_name, balance):
        self._acc_no = acc_no
        self._holder_name = holder_name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        self.__balance = amount

    def deposit(self, amount):
        if amount > 0:
            self.set_balance(self.get_balance() + amount)
            print("Amount Deposited Successfully.")
        else:
            print("Invalid Amount.")

    def withdraw(self, amount):
        if amount <= self.get_balance():
            self.set_balance(self.get_balance() - amount)
            print("Withdrawal Successful.")
        else:
            print("Insufficient Balance.")

    def show_details(self):
        print("\nAccount Number :", self._acc_no)
        print("Holder Name    :", self._holder_name)
        print("Balance        : ₹", self.get_balance())


# -------------------- Savings Account --------------------

class SavingsAccount(Account):

    def withdraw(self, amount):
        minimum_balance = 500

        if self.get_balance() - amount >= minimum_balance:
            self.set_balance(self.get_balance() - amount)
            print("Withdrawal Successful.")
        else:
            print("Minimum balance of ₹500 must be maintained.")


# -------------------- Current Account --------------------

class CurrentAccount(Account):

    def withdraw(self, amount):
        overdraft_limit = 2000

        if self.get_balance() + overdraft_limit >= amount:
            self.set_balance(self.get_balance() - amount)
            print("Withdrawal Successful.")
        else:
            print("Overdraft Limit Exceeded.")


# -------------------- Bank Class --------------------

class Bank:

    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.accounts = []

    def create_account(self):
        acc_no = input("Enter Account Number: ")

        for acc in self.accounts:
            if acc._acc_no == acc_no:
                print("Account Number Already Exists.")
                return

        name = input("Enter Holder Name: ")
        balance = float(input("Enter Initial Deposit: "))

        print("1. Savings Account")
        print("2. Current Account")
        choice = input("Choose Account Type: ")

        if choice == "1":
            account = SavingsAccount(acc_no, name, balance)

        elif choice == "2":
            account = CurrentAccount(acc_no, name, balance)

        else:
            print("Invalid Choice.")
            return

        self.accounts.append(account)
        print("Account Created Successfully.")

    def find_account(self, acc_no):
        for acc in self.accounts:
            if acc._acc_no == acc_no:
                return acc
        return None

    def deposit_money(self):
        acc = self.find_account(input("Enter Account Number: "))

        if acc:
            amount = float(input("Enter Amount: "))
            acc.deposit(amount)
        else:
            print("Account Not Found.")

    def withdraw_money(self):
        acc = self.find_account(input("Enter Account Number: "))

        if acc:
            amount = float(input("Enter Amount: "))
            acc.withdraw(amount)
        else:
            print("Account Not Found.")

    def transfer_money(self):
        sender = self.find_account(input("Sender Account Number: "))
        receiver = self.find_account(input("Receiver Account Number: "))

        if sender and receiver:

            amount = float(input("Enter Amount: "))

            old_balance = sender.get_balance()

            sender.withdraw(amount)

            if sender.get_balance() != old_balance:
                receiver.deposit(amount)
                print("Transfer Successful.")

        else:
            print("Invalid Account Number.")

    def check_balance(self):
        acc = self.find_account(input("Enter Account Number: "))

        if acc:
            print("Available Balance : ₹", acc.get_balance())
        else:
            print("Account Not Found.")

    def show_account(self):
        acc = self.find_account(input("Enter Account Number: "))

        if acc:
            acc.show_details()
        else:
            print("Account Not Found.")

    def delete_account(self):
        acc = self.find_account(input("Enter Account Number: "))

        if acc:
            self.accounts.remove(acc)
            print("Account Deleted Successfully.")
        else:
            print("Account Not Found.")

    def show_all_accounts(self):

        if len(self.accounts) == 0:
            print("No Accounts Available.")
            return

        print("\n------ Account List ------")

        for acc in self.accounts:
            print(acc._acc_no, "-", acc._holder_name,
                  "- ₹", acc.get_balance())


# -------------------- Main Program --------------------

bank = Bank("ABC Bank")

while True:

    print("\n========== BANK ACCOUNT MANAGEMENT ==========")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Money")
    print("5. Check Balance")
    print("6. Account Details")
    print("7. Show All Accounts")
    print("8. Delete Account")
    print("9. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        bank.create_account()

    elif choice == "2":
        bank.deposit_money()

    elif choice == "3":
        bank.withdraw_money()

    elif choice == "4":
        bank.transfer_money()

    elif choice == "5":
        bank.check_balance()

    elif choice == "6":
        bank.show_account()

    elif choice == "7":
        bank.show_all_accounts()

    elif choice == "8":
        bank.delete_account()

    elif choice == "9":
        print("Thank You for Using ABC Bank.")
        break

    else:
        print("Invalid Choice. Try Again.")