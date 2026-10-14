""" ATM WITHDRAWL LOGIC
create an ATM program with balance ₹12000
rules:
 1. correct pin: 4321
 2. withdrawl must be positive
 3. the balance must never fail below ₹2,000
 4. withdrawls above ₹10,000 require manager approval
 5. An incorrect pin must prevent all further transaction
 
Tricky condition: The balance is ₹12,000 and the customer tries to
withdraw ₹11,000 without manager approval

Task: use nested if statements to handle every condition and display
the correct remaining balance """

Balance = 12000
pin = int(input("enter your pin"))
if pin == 4321:
    amount = int(input("enter withdrawl amount:"))
    if amount > 0:
        if Balance - amount >= 2000:
            if amount >= 10000:
                manager_approval = input("Manager approval yes or no")
                if manager_approval == "yes":
                    Balance = Balance - amount
                    print("amount withdrawn")
                else:
                    print("Manger approval required")
            else:
                Balance = Balance - amount
                print("amount withdrawn")
        else:
            print("Balance insufficient")
    else:
        print("enter positive balane")
else:
    print("Invalid pin")
print("Remaining balance",Balance)

