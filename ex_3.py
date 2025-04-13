Balance = 10000


    
while True:
        print("bank console")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance")
        print("4. Exit")

        choice = int(input("Enter the choice:"))

        if(choice == 1):
            AmountDeposited = int(input("Enter the amount to be depositied"))
            if(AmountDeposited>=0):
                print("bank balance = ", AmountDeposited + Balance)
            else:
                print("Amount to be deposited is not valid")

        elif(choice == 2):
            WithdrawAmount = int(input("Enter the amount to be withdrawn"))
            if(0<WithdrawAmount<Balance):
                print("bank balance = ", Balance - WithdrawAmount)
            else:
                ("Insufficient Balance")

        elif(choice == 3):
            print("bank balance = ", Balance)

        elif(choice ==4):
            print("Thank You")
            break
        else:
            print("Please enter valid choice:")

    
