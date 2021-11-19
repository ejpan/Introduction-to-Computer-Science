def main():
    import bankaccount

    print("Welcome to the Universal Bank!")
    print("Please enter the account owner name:")
    #asks for bank account owner's name
    owner_name=input("")
    print("\nPlease enter the account initial balance:")
    balance=float(input(""))
    #assigns the class Bankacount to the object user
    user=bankaccount.BankAccount(owner_name,balance)

    again="y"
    #while loop if user wants to run program again
    while again=="y":
        #asks user to select an action
        print("\nSelect one of the choices: (e.g., type 'd' or 'D' for making a deposit)\n"\
              "\tc\tChange account owner name\n\td\tMake a deposit\n\tw\tMake a withdrawl"\
              "\n\ts\tDisplay account info\n\tq\tquit")
        choice=input("")
        #changes account owners name 
        if choice=="c":
            print("\nPlease enter the new account owner name:")
            newName=input("")
            user.set_name(newName)
        #asks for amount and adds amount to balance
        elif choice=="d":
            print("\nEnter an amount to be deposited:")
            amount=int(input(""))
            user.deposit(amount)
        #withdraws amount by subtracting from balance
        elif choice=="w":
            print("\nEnter an amount to be withdrawn:")
            amount=int(input(""))
            user.withdraw(amount)
        #prints account balance
        elif choice=="s":
            print(str(user))
        #ends the while loop
        elif choice=="q":
            again="n"
        #asks if user wants to run program again
        if again=="y" or again=="Y":
            print("\nWant another transaction (y or Y for yes, n or N for no)?")
            again=input("")
    #prints out account summary
    print(str(user))
    print("\nThank you for your business.")
main()

    


