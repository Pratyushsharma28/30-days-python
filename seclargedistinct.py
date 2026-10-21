""" SECOND-LARGEST DISTINCT NUMBER
Given a list of integers, find the second-largest distinct value
using loops.
example: [10,25,25,8,20]

constraints:
1. do not use sort(),sorted(),or max().
2. handle duplicate values
3. display a suitable message if no second-largest distinct
value exists"""

numbers = [10,25,25,8,20]
largest = None
second = None

for num in numbers:
    if largest is None or num > largest:
        second = largest
        largest = num 
    elif num != largest:
        if second is None or num > second:
            second = num 
if second is None:
    print("No second-largest distinct number")
else:
    print("Second largest",second)
        
        
    
    