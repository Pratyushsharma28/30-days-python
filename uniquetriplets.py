""" UNIQUE TRIPLETS
Given a list of integers and a target value, find all unique triplets
whose sum equals to the target. do not use sets,dictionaries,or
sorting. avoid dupliocates triplets in the output"""

numbers = [2,1,3,2,4,0]
target = 6
result = []

for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        for k in range(j+1,len(numbers)):
            
            a = numbers[i]
            b = numbers[j]
            c = numbers[k]
            
            if a + b + c == target:
                triplet = [a,b,c]
                
                if triplet not in result:
                    result.append(triplet)
print(result)


