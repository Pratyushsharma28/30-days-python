""" Write a function that finds two different list indices whose values 
add up to a target; return the pair with the smallest second index and 
then the smallest first index, or None if no pair exists, without sorting."""

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)

    return None


numbers = [2, 7, 11, 15]
target = 9

print(two_sum(numbers, target))
