""" MATRIX CHALLENGE
Given a square matrix,find every element that is the smallest
in its row and the largests in his column . print the element
and its position. If no such elements exists, print an appropriate 
message."""

a = [
    [3,7,8],
    [9,11,13],
    [15,16,17]
]

found = False

for i in range(3):
    for j in range(3):
        num = a[i][j]
        row = min(a[i])
        
        col = max(a[0][j],a[1][j],a[2][j])
        
        if num==row and num==col:
            print("Numbers:",num)
            print("Position",i,j)
            found = True
if found == False:
    print("No element found ")
