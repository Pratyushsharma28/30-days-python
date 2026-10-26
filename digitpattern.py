""" DIGIT PATTERN
Print all numbers from 100 to 999 whose digits are strictly increasing
from left to right and whose digit sum is divisible by 3"""

for i in range(100,1000):
   s = str(i)
   a,b,c = int(s[0]),int(s[1]),int(s[2])
   if a<b<c and a+b+c % 3 == 0:
       print(i)

