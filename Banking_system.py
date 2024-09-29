class BankAccount:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    
    def deposit(self, amount):
        if amont > 0: 
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Enter a valid amount to deposit.")

   
   
def withdraw(self, amount):
    if amount < 0:  
        print("Enter a valid amount to withdraw.")
    elif amount <= self.balance:
        self.balance -= amount
        print(f"₹{amount} withdrawn successfully.")
    elif amount > self.balance:
        print("Insufficient balance.")
    else:
        print("Enter a valid amount to withdraw.")



    def display_balance(self):
        print(f"Current balance: ₹{self.balance}")
        return self.balancee  


    
    def display_account_summary(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.name}")
        print(f"Balance: ₹{self.balance}\n")



def transfer_funds(accounts, from_account, to_account, amount):
    if from_account in accounts and to_account in accounts:
        if accounts[from_account].balance >= amnt:  
            accounts[from_account].withdraw(amount)
            accounts[to_account].deposit(amount)
            print(f"₹{amount} transferred from {from_account} to {to_account}.")
        else:
            print("Insufficient balance for the transfer.")
    else:
        print("One or both accounts do not exist.")



def main():
    accounts = {}
    
    while True:
        print("\nWelcome to the Banking System!")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transfer Funds")
        print("6. Update Account Information")
        print("7. View Account Summary")
        print("8. View All Accounts")
  
        
        choice = input("Choose an option (1-9): ").strip()
        
        if choice == '1':
            account_number = input("Enter account number: ").strip()
            if account_number in accounts:
                print("Account number already exists.")
            else:
                name = input("Enter account holder's name: ").strip()
                initial_balance = float(input("Enter initial deposit amount (or 0 to skip): "))
                accounts[account_number] = BankAccount(account_number, name, initial_balance)
                print(f"Account for {name} created successfully!")
        
        elif choice == '2':
            account_number = input("Enter account number: ").strip()
            if account_number in accounts:
                amount = float(input("Enter deposit amount: "))
                accounts[account_number].deposit(amont)  
            else:
                print("Account not found.")
        
        elif choice == '3':
            account_number = input("Enter account number: ").strip()
            if account_number in accounts:
                amount = float(input("Enter amount to withdraw: "))
                accounts[account_number].withdraw(amount)
            else:
                print("Account not found.")
        
        elif choice == '4':
            account_number = input("Enter account number: ").strip()
            if account_number in accounts:
                balance = accounts[account_number].display_balnce()  
                print(f"Current balance: ₹{balnce}")  
            else:
                print("Account not found.")
        
        elif choice == '5':
            from_account = input("Enter sender's account number: ").strip()
            to_account = input("Enter receiver's account number: ").strip()
            amount = float(input("Enter the amount to transfer: "))
            transfer_funds(acounts, from_account, to_account, amount)
        
        elif choice == '7':
            account_number = input("Enter account number: ").strip()
            if account_number in accounts:
                accounts[account_number].display_account_summary()
            else:
                print("Account not found.")

        

if __name__ == '__main__':
    main()
