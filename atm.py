Account_balance = 1000000
print ("Hello users welcome to the ATM")
PIN = 1994
print("Please enter your 4 digit pin code")
enter = int(input())
if enter == PIN:
    print ("Pin enter successfully")
else:
    print ("you have entered an invalid pin")
    
d = "1"
c = "2"    
print("Select type of your account \n press 1 to deposit money \n press 2 to withdraw money")
enter2 = input()
if enter2 == d:
    print ("How much money you want to deposit")
elif enter2 == c:
    print ("How much you want to withdraw")
    print("select the options how much amount you want to withdraw \n press 1 to withdraw 5000 \n press 2 to withdraw 10000 \n press 3 to withdraw 100000 \n press 4 to withdraw custom amount ")
enter3 = int(input("Enter  the number "))

amount1 = 5000
amount2 = 10000
amount3=100000
if (enter3 == amount1):
    Account_balance=Account_balance-amount1
    print(Account_balance)
elif(enter3 == amount2):
    Account_balance=Account_balance-amount2
    print(Account_balance) 
elif(enter3 == amount3):
    Account_balance=Account_balance-amount3
    print(Account_balance)
    
else:
    Account_balance=Account_balance-enter3
    print( Account_balance)
