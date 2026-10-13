""" Very advanced: Employee Bonus and Promotion eligilbilty
write a python program that accepts an employee's annual salary,
years of experience,performance rating(out of 10), and attendance 
percentage
Requirements
 1. print "bonus eligible" if experience is at least 3 years, rating
 is at least 8, and attendance is at least 90%
 2. print "prmotion eligible" if experience is at least 5 years and
 rating is at least 9.
 3. print "high performer" if the rating is at least 9, regardless
 of the other conditions.
 4. Each result must be checked independently
 5. if the salary is greater than ₹1,000,000, print "high salary band"
 
 restriction: use independent if statements with appropriate logical
 operator. multiple message may appear."""
 
annual_salary = int(input("enter annual salary:"))
experience = float(input("enter years of experience:"))
rating = float(input("enter rating (out of 10):"))
attendance = float(input("enter attendance percentage:"))
if experience >= 3 and rating >= 8 and attendance >= 90:
    print("Bonus Eligible")
if experience >= 5 and rating >=9:
    print("Promotion Eligible")
if experience >= 9:
    print("High Performer")
if annual_salary > 1000000:
    print("High Salary Band")
 
 
