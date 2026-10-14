""" Scholarship Eligibility Trap

A college awards scholarships based on marks and family income.

Rules:

ITAHW

If any subject mark is below 35, the student fails.

Otherwise, calculate the average of 3 subjects.

Average ≥ 90 and income below ₹3,00,000: 100% scholarship.

Average ≥ 80 and income below 5,00,000: 50% scholarship.

Average ≥ 70: admission without scholarship.

Otherwise: admission rejected.

Tricky condition: A student scores 95, 96, and 30, with family income of ₹1,00,000. The average is

high, but should the student receive a scholarship?

Task: Write the complete program with input validation and nested conditions"""


marks1 = int(input("enter marks1:"))
marks2 = int(input("enter marks2:"))
marks3 = int(input("enter marks3:"))
income = float(input("enter family income"))
if marks1 < 0 or marks1 > 100 or marks2 < 0 or marks2 > 100 or marks3 < 0 or marks3 > 100:
    print("Invalid input")
else:
    if marks1 <= 35 or marks2 <= 35 or marks3 <= 35:
        print("student failed")
    else:
        avg = (marks1 + marks2 + marks3)/3
        print("Average",avg)
        
        if avg >= 90:
            if income < 300000:
                print("100% Scholarship")
            elif income < 500000:
                print("50% Scholarship")
            else:
                print("Admission without scholarship")
        elif avg >= 80:
            if income < 500000:
                print("50% Scholarship")
            else:
                print("Admission without scholarship")
        elif avg >= 70:
            print("Admission without scholarship")
        else:
            print("Admission Rejected")

