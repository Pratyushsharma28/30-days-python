""" HOLLOW RIGHT ALLIGNED TRIANGLE
    *
   **
  * *
 *  *
*****

"""

n = 5

# Outer loop controls rows
for i in range(1, n+1):

    # Print spaces before stars
    print("  " * (n-i), end="")

    # Inner loop controls columns
    for j in range(1, i+1):

        # Check boundary conditions
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    # Move to next row
    print()