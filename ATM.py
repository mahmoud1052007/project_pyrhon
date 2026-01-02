def show_balance():
    print(f"your balance is : {balance:.2f} le")
def deposit():
    amount=float(input("plase enter an amount to be deposited :"))
    if amount<0:
        print("this is not a valid amount")
        return 0
    else:
        return amount
def withdraw():
    amount=float(input("plase enter an amount to be withdraw :"))
    if amount>balance:
        print("insufficint funds")
        return 0
    elif amount<0:
        print("amount must be greader then 0")
        return 0
    else:
        return amount
balance=0
is_running=True
while is_running:
    print("******************************")
    print("Welcome to your account ⭐\n")
    print("1. show_balance")
    print("2. deposit")
    print("3. withdraw")
    print("4. exit")
    print("******************************")
    choose=input("please choose form (1,2,3,4) :")
    print("******************************")
    if choose=="1":
        show_balance()
    elif choose=="2":
        balance=balance+deposit()
    elif choose=="3":
        balance=balance-withdraw()
    elif choose=="4":
        is_running=False
    else:
        print("this is not a valid choose")
print(" Thank you for using our bank")