""" TRIANGLE CLASSIFICATION PUZZLE
Accept three side lengths and classify the triangle
rules:
 1.all sides must be positive
 2.the sum of any two sides must exceed the third side
 3.classify it as equilateral,isosceles or scalene
 4.also check whether it is right-angled using the pythagorean theorem
 Tricky condition: inputs are 1,2,3,4 the sides look almost valid,
 but they do not form a triangle
 Task: reject invalid traiangles before checking their type or angle"""

a = float(input("Enter side1"))
b = float(input("Enter side2"))
c = float(input("Enter side3"))
if a > 0 or b > 0 or c > 0:
    if a+b > c and b+c > a and a+c > b:
        if a == b == c:
            print("equilateral triangle")
        elif a == b or b == c or a == c:
            print("isosceles triangle")
        else:
            print("scalene traiangle")
        if (a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a ):
            print("Right angles triangle")
        else:
            print("Not a right angles triangle")
    else:
        print("Invalid triangle")
else:
    print("sides must be positive")