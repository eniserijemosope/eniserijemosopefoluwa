#Simple ATM
import time
ac_balance = 1000

print(f"Your Balance is £{ac_balance}!.")

choices = ["1. Withdraw", "2. Deposit", "3. Transfer ", "4. Recharge"]

for x in choices:
    print(x)

user_choice = (input("Pick an option using the number that stands for it: "))

while not user_choice or user_choice.isalpha():
    print("You've made an invalid selection!.")
    user_choice = (input("Pick an option using the number that stands for it: "))

if user_choice == "1":
    print("You've selected the withdrawal option.")
    withdraw = float(input("Please select the amount you'll like to withdraw?: "))
    ac_balance = float(ac_balance - withdraw)
    print(f"Your withdrawal of £{round(withdraw, 3)} is successful and your balance is now £{round(ac_balance, 3)}")

elif user_choice == "2":
    print("You've selected the deposit option.")
    deposit = float(input("Please select the amount you'll like to deposit?: "))
    ac_balance = float(ac_balance + deposit)
    print(f"Your deposit of £{round(deposit, 3)} is successful and your balance is now £{round(ac_balance, 3)}")

elif user_choice == "3":
    print("You've selected the transfer option.")
    transfer = float(input("Please select the amount you'll like to transfer?: "))
    ac_number = int(input("please input the account number you'll like to send the money to: "))
    ac_balance = float(ac_balance - transfer)
    print(f"Your transfer of £{round(transfer, 3)} to {ac_number} is successful and your balance is now £{round(ac_balance, 3)}")

elif user_choice == "4":
    print("You've selected the Recharge option.")
    recharge = int(input("Please select the amount you'll like to recharge?: "))
    time.sleep(0.5)
    p_number = float(input("Please input the phone number you'll like to recharge?: (+234)- "))
    time.sleep(0.5)
    p_number = str(p_number)
    ac_balance = float(ac_balance - recharge)
    print(f"Your recharge of £{round(recharge, 3)} to (+234){p_number} is successful and your balance is now £{round(ac_balance, 3)}")












