""" RIGHT ALLIGNED HALF DIAMOND
    *
   **
  ***
 ****
*****
 ****
  ***
   **
    *

"""
n = 5
for i in range(1,n+1):
    print(" "*(5-i)+ "*"*i)
for i in range(n-1,0,-1):
    print(" "*(n-i)+"*"*i)
