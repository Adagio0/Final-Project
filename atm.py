def atm():
    deposit_cash = int(input("How much would you like to deposit?"))
    withdraw =int(input("How much would you like to withdraw?"))
if (depost_cash > withdraw):
    print("your withdraw balance is ", deposit_cash - withdraw)
else: 
    print("Error, not enough money")