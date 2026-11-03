""" EQUILATERAL TRIANGLE WITH SPACED STARS
     *
    **
   ***
  ****
 *****
 
 """
 
n = 5

for i in range(1,n+1): # outer loop controls rows
    
    print(" "*(n-i)+"*"*i) # print spaces then stars
