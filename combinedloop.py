""" COMBINED LOOP CHALLENGE
write a program that examines every pair of integersi and j from
1 to 20, subject to these rules:
1. Skip pairs where i==j
2. skip pairs where both numbers are even
3. stop the inner loop when i*j > 100
4. print only pairs whose sum is a prime number
5. count and display the total number of pairs printed

use nested loops and conditional statements to solve the problem"""

count = 0

for i in range(1,21):
    for j in range(1,21):
        if i==j:
            continue
        if i % 2 == 0 and j % 2 == 0:
            continue
        if i * j > 100:
            break
        s = i+j
        prime = True
        
        if s < 2:
            prime = False
            
        for k in range(2,s):
            if s%k==0:
                prime = False
                break
        if prime:
            print(i,j)
            count += 1
print("total pairs",count)
        
