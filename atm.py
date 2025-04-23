import random

cust_data = {}
new_user_attributes = ['name', 'address', 'phone num', 'govt id', 'amount']

def new_user():
    acc_num = random.randint(10000, 99999)
    while acc_num in cust_data:
        acc_num = random.randint(10000, 99999)
    
    new_user_input = []
    for attr in new_user_attributes:
        user_input = input(f"Enter {attr}: ")
        if attr == "amount":
            new_user_input.append(int(user_input))
        else:
            new_user_input.append(user_input)
    
    cust_data[acc_num] = dict(zip(new_user_attributes, new_user_input))
    print(f"""\nYour details are added successfully.
Your account number is {acc_num}
Please don't lose it.\n""")

def existing_user():
    account_number = int(input("Enter your account number: "))
    while account_number not in cust_data:
        print("Account not found. Please enter your correct account number:")
        account_number = int(input("Enter your account number: "))
    
    user = cust_data[account_number]
    print(f"""\nWelcome, {user['name']}!
Enter 1 to check your balance.
Enter 2 to withdraw an amount.
Enter 3 to deposit an amount.\n""")
    
    user_input = int(input())
    while user_input not in [1, 2, 3]:
        print('''Invalid input!
Enter 1 to check your balance.
Enter 2 to withdraw an amount.
Enter 3 to deposit an amount.''')
        user_input = int(input())

    if user_input == 1:
        print(f"Your current balance is ₹{user['amount']}")
    
    elif user_input == 2:
        withdrawal = int(input("Enter the amount to withdraw: "))
        if withdrawal > user['amount']:
            print("Insufficient funds")
        else:
            user['amount'] -= withdrawal
            print("Withdrawal successful")
        print(f"Your current balance is ₹{user['amount']}")

    elif user_input == 3:
        deposit = int(input("Enter amount to deposit: "))
        user['amount'] += deposit
        print("Deposit successful")
        print(f"Your current balance is ₹{user['amount']}")

# Main loop
while True:
    print("""\nWelcome to the Horizon Bank!

Enter 1 if you are a new customer.
Enter 2 if you are an existing customer.
Enter 3 to terminate the application.""")
    
    try:
        user_input = int(input())
        if user_input == 1:
            new_user()
        elif user_input == 2:
            existing_user()
        elif user_input == 3:
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid option. Please try again.")
    except ValueError:
        print("Please enter a valid number (1, 2, or 3).")
