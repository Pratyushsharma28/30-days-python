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
for i in range(1,n+1): # increasing pattern
    
    print(" "*(5-i)+ "*"*i) # print spaces followed by stars
    
for i in range(n-1,0,-1): # decreasing pattern
    
    print(" "*(n-i)+"*"*i) # print spaces followed by decreasing star
