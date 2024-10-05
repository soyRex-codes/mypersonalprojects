def show_balance(balance):
    print(f"your balance is ${balance:.2f}")
    
def deposite():
    amount = float(input("Enter an amount to be deposited: "))
    
    if amount<0:
        print("Not valid amount")
        return 0
    else:
        return amount    
       
def withdraw(balance):
    amount=float(input("Enter an amount to be withdrawn: "))
    if amount>balance:
        print("Insufficient funds")
        return 0 
    elif amount<0:
        print("Amount must be equal to or less than balance")
        return 0    
    else:
        return amount    



def main():
    balance=0
    is_running=True 

    while is_running:
        print("*************************************************************")
        print("*************************************************************")
        print("Banking program")
        print("1.show Balance")
        print("2.Deposite")
        print("3.WIthdraw")
        print("4.Exit")
        
        choice=input("Enter your choice (1-4): ")
        if choice == '1':
            show_balance(balance)
            print("*************************************************************")
            print("*************************************************************")    
        elif choice =='2':
            balance += deposite()
            print("*************************************************************")
            print("*************************************************************")    
        elif choice =='3':
            balance -= withdraw(balance)
            print("*************************************************************")
            print("*************************************************************")
        elif choice =='4':
            is_running=False
        else:
            print("not Valid choice")  

    print(" Thankyou, Have  a nice day!")    
    
if __name__  == '__main__':
    main()    
