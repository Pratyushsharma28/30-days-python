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
experience = int(input("Enter experience:"))
rating = float(input("Enter rating:"))
if experience >= 10 and rating >= 4.5:
    print("25% Bonus and Promotion")
elif experience >=10 and rating >= 3.5:
    print("15% Bonus and Promotion")
elif experience >= 5 and rating >= 4.0:
    print("12% Bonus ")
elif experience < 5 and rating >= 4.5:
    print("8% Bonus")
else:
    print("No Bonus")