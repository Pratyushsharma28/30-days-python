""" BASIC + CHALLENGING: SMART TRANSACTION VALIDATOR
Write a python program that accepts bank balance and a withdrawl amount
Requirements
 1. check whether the withdrawl amount is positive
 2. check whether the amount is a multiple of ₹100
 3. check whether the account has suffiecient balance
 4. print "Transaction succsessful" only if all three conditions
 are satisfied
 5. otherwise, print the appropriate reason for rejection
 
 Restriction: use only if statements and logical operators. Do not
 use elif and else."""

Bank_balance = int(input("Enter bank balance: -Rs."))
withdrawl_amount = int(input("Enter withdrawl amount: -Rs."))
# check positive amount
if withdrawl_amount <= 0:
    print("Rejected amount should be positive")
if withdrawl_amount > 0 and withdrawl_amount % 100 != 0:
    print("Rejected amount should be in multiple of 100")
if withdrawl_amount > 0 and withdrawl_amount > Bank_balance:
    print("Rejected withdrawl amount must be less that bank balance")
if 