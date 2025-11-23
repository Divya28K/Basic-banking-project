def show_balance():
    print(f"Your balance is ${balance:.2f}")


def deposit():
    amount = float(input("Enter the amount to be deposited: "))
    if amount <= 0:
        print("That's not a valid amount.")
        return 0
    else:
        print(f"${amount:.2f} has been deposited.")
        return amount


def withdraw():
    global balance
    amount = float(input("Enter the amount to withdraw: "))
    if amount <= 0:
        print("That's not a valid amount.")
    elif amount > balance:
        print("Insufficient funds!")
    else:
        balance -= amount
        print(f"${amount:.2f} has been withdrawn.")
        return amount


balance = 0
is_running = True

while is_running:
    print("\nBanking Program")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        show_balance()
    elif choice == '2':
        balance += deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        is_running = False
    else:
        print("This is not a valid choice.")  

print("Thank you! Have a nice day!")
