""" HOLLOW INVERTED RIGHT TRIANGLE
*****
*  *
* *
**
* 
"""

n = 5
for i in range(n,0,-1): # outer loop controls rows
    
    for j in range(1,i+1): # inner loop controls coloumns
        
        if i==n or j==1 or j==i: # check first row,first column,last coloumn
            
            print("*",end=" ") # print star
        else:
            print(" ",end=" ") # print space inside the triangle
    print() # move to next row
