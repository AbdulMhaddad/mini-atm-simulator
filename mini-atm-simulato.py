# mini-atm-simulator

## question  Write a program that simulates a simple ATM machine.

# The program should:
# Start with a fixed account balance (e.g. 1000).
# Show a of options:
# Check Balance
# Deposit Money
# Withdraw Money
# Exit
# Ask the user to choose an option (with input).
# Perform the action:
# If balance check → print the balance.
# If deposit → ask how much, add to balance, and show new balance.
# If withdraw → ask how much, subtract if enough money, otherwise show error.
# If exit → stop the program.
# Keep showing the menu until the user chooses Exit.


# we will breake the outpot into 3 funtions for each option and then we will add main funtion to run our code

#start with checking balanc 

def check_balance(balance):
    print(f"Your Current balance is {int(balance)} \n")

#funtion to Depositee money1

def deposit(balance):
    amount = float(input("Enter the amout to deposit: "))
    if amount > 0 :
        balance += amount 
        print(f"Deposite successful. New Balance ={int(balance)}\n")
    else:
        print("Invalid deposit amount.\n")
    return balance

# funtion to withdraw money

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds!\n")
    elif amount <= 0:
        print("Invalid withdrawal amount.\n")
    else:
        balance -= amount
        print(f"Withdrawal successful. New balance = {int(balance)}\n")
    return balance

#main funtion we call it bank account simulator

def bank_account_simulator():
    balance = 1000
    print("Welcome to the Bank Account Simulator")
    print(f"Your balance is {balance}\n")

    while True:
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit\n")

        choice = input("Choose an option: ")

        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.\n")

# Run the Bank Account Simulator
bank_account_simulator()