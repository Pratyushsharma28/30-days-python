""" EMPLOYEE BONUS AND PROMOTION 
Determne an employee's bonus and promotion eligibility
rule:
 1. Experience ≥ 10 years and rating ≥ 4.5: 25% bonus and promotion.

Experience ≥ 10 years and rating ≥ 3.5: 15% bonus, no promotion.

Experience ≥ 5 years and rating ≥ 4.0: 12% bonus.

Experience below 5 years and rating ≥ 4.5: 8% bonus.

All other cases: no bonus.


Tricky condition: An employee has 12 years of experience but a rating of 3.2.

Task: Accept salary, experience, and rating; calculate the bonus amount and promotion status. Validate all inputs."""

salary = int(input("Enter salary:"))
experience = float(input("Enter experience:"))
rating = float(input("Enter rating:"))
Bonus = 0
if experience >= 10 and rating >= 4.5:
    Bonus = 25
elif experience >=10 and rating >= 3.5:
    Bonus = 15
elif experience >= 5 and rating >= 4.0:
    Bonus = 12
elif experience < 5 and rating >= 4.5:
    Bonus = 8 
else:
    Bonus = 0    
Bonus_amount = salary * Bonus/100
Total_salary = salary + Bonus_amount
print("Total salary including Bonus",Total_salary)
print("Bonus amount",Bonus_amount)
