import json
import os

class BankAccount:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Enter a valid amount to deposit.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a valid amount to withdraw.")
        elif amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print(f"Current balance: ₹{self.balance}")
        return self.balance

    def display_account_summary(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.name}")
        print(f"Balance: ₹{self.balance}\n")

def transfer_funds(accounts, from_account, to_account, amount):
    if from_account in accounts and to_account in accounts:
        if amount <= 0:
            print("Enter a valid amount to transfer.")
            return
        if accounts[from_account].balance >= amount:
            accounts[from_account].withdraw(amount)
            accounts[to_account].deposit(amount)
            print(f"₹{amount} transferred from {from_account} to {to_account}.")
        else:
            print("Insufficient balance for the transfer.")
    else:
        print("One or both accounts do not exist.")

def load_accounts(filename='accounts.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            accounts = {}
            for acc_data in data:
                account = BankAccount(
                    account_number=acc_data["account_number"],
                    name=acc_data["name"],
                    balance=acc_data["balance"]
                )
                accounts[account.account_number] = account
            return accounts
    else:
        return {}

def save_accounts(accounts, filename='accounts.json'):
    data = []
    for account in accounts.values():
        acc_dict = {
            "account_number": account.account_number,
            "name": account.name,
            "balance": account.balance
        }
        data.append(acc_dict)
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    accounts = load_accounts()
    
    while True:
        print("\nWelcome to the Banking System!")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transfer Funds")
        print("6. View Account Summary")
        
        choice = input("Choose an option (1-8): ").strip()
        
        if choice == '1':
            account_number = input("Enter account number: ").strip()
            if account_number in accounts:
                print("Account number already exists.")
            else:
                name = input("Enter account holder's name: ").strip()
                try:
                    initial_deposit = input("Enter initial deposit amount (or press Enter to skip): ").strip()
                    initial_balance = float(initial_deposit) if initial_deposit else 0.0
                    if initial_balance < 0:
                        print("Initial deposit cannot be negative. Setting balance to ₹0.")
                        initial_balance = 0.0
                except ValueError:
                    print("Invalid amount entered. Setting initial balance to ₹0.")
                    initial_balance = 0.0
                accounts[account_number] = BankAccount(account_number, name, initial_balance)
                save_accounts(accounts)
                print(f"Account for {name} created successfully!")

        elif choice == '2':
            account_number = input("Enter account number: ").strip()
            if account_number in accounts:
                try:
                    amount = float(input("Enter deposit amount: "))
                    accounts[account_number].deposit(amount)
                    save_accounts(accounts)
                except ValueError:
                    print("Invalid amount entered.")
            else:
                print("Account not found.")

        elif choice == '3':
            account_number = input("Enter account number: ").strip()
            if account_number in accounts:
                try:
                    amount = float(input("Enter amount to withdraw: "))
                    accounts[account_number].withdraw(amount)
                    save_accounts(accounts)
                except ValueError:
                    print("Invalid amount entered.")
            else:
                print("Account not found.")

        elif choice == '4':
            account_number = input("Enter account number: ").strip()
            if account_number in accounts:
                balance = accounts[account_number].display_balance()
            else:
                print("Account not found.")

        elif choice == '5':
            from_account = input("Enter sender's account number: ").strip()
            to_account = input("Enter receiver's account number: ").strip()
            try:
                amount = float(input("Enter the amount to transfer: "))
                transfer_funds(accounts, from_account, to_account, amount)
                save_accounts(accounts)
            except ValueError:
                print("Invalid amount entered.")

        elif choice == '6':
            account_number = input("Enter account number: ").strip()
            if account_number in accounts:
                accounts[account_number].display_account_summary()
            else:
                print("Account not found.")

if __name__ == '__main__':
    main()
