user_accounts = {
    "user 1": {"balance": 1000, "pin": "1234"},
    "user 2": {"balance": 500, "pin": "5678"}
   
}

# Welcome message
print("Welcome to Simple Bank Console Server")

# Main program logic
is_logged_in = False
current_user = ""

while True:
    if not is_logged_in:
        # Login process
        username = input("Enter username (or 'exit' to quit): ")
        
        if username.lower() == "exit":
            print("Thank you for using Simple Bank Console Server. Goodbye!")
            break
            
        if username in user_accounts:
            pin = input("Enter your PIN: ")
            if pin == user_accounts[username]["pin"]:
                is_logged_in = True
                current_user = username
                print(f"Login successful. Welcome {current_user}!")
            else:
                print("Incorrect PIN. Please try again.")
        else:
            print("Username not found. Please try again.")
    
    else:
        # Display menu
        print("\n----- MENU -----")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer Money")
        print("5. Logout")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        # Check balance
        if choice == "1":
            print(f"Your current balance: ${user_accounts[current_user]['balance']}")
        
        # Deposit
        elif choice == "2":
            try:
                amount = float(input("Enter amount to deposit: $"))
                if amount > 0:
                    user_accounts[current_user]["balance"] += amount
                    print(f"${amount} deposited successfully.")
                    print(f"New balance: ${user_accounts[current_user]['balance']}")
                else:
                    print("Please enter a positive amount.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        # Withdraw
        elif choice == "3":
            try:
                amount = float(input("Enter amount to withdraw: $"))
                if amount > 0:
                    if amount <= user_accounts[current_user]["balance"]:
                        user_accounts[current_user]["balance"] -= amount
                        print(f"${amount} withdrawn successfully.")
                        print(f"New balance: ${user_accounts[current_user]['balance']}")
                    else:
                        print("Insufficient funds.")
                else:
                    print("Please enter a positive amount.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        # Transfer Money
        elif choice == "4":
            recipient = input("Enter recipient's username: ")
            if recipient in user_accounts and recipient != current_user:
                try:
                    amount = float(input(f"Enter amount to transfer to {recipient}: $"))
                    if amount > 0:
                        if amount <= user_accounts[current_user]["balance"]:
                            user_accounts[current_user]["balance"] -= amount
                            user_accounts[recipient]["balance"] += amount
                            print(f"Transfer successful!")
                            print(f"${amount} debited from your account.")
                            print(f"${amount} credited to {recipient}'s account.")
                            print(f"Your new balance: ${user_accounts[current_user]['balance']}")
                        else:
                            print("Insufficient funds for this transfer.")
                    else:
                        print("Please enter a positive amount.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            elif recipient == current_user:
                print("Cannot transfer money to yourself.")
            else:
                print("Recipient username not found.")
        
        # Logout
        elif choice == "5":
            is_logged_in = False
            print(f"Logged out successfully. Goodbye, {current_user}!")
            current_user = ""
        
        # Exit
        elif choice == "6":
            print(f"Logged out successfully. Goodbye, {current_user}!")
            print("Thank you for using Simple Bank Console Server.")
            break
        
        else:
            print("Invalid choice. Please try again.")
