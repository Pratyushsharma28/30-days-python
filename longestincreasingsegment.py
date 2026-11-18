""" Write a function that returns the length and starting index 
of the longest contiguous strictly increasing segment in a list; 
if multiple segments have the same length, return the earliest 
one without sorting or creating another list."""

def longest_increasing(nums):
    if len(nums) == 0:
        return (0, -1)

    count = 1
    max_count = 1
    start = 0
    max_start = 0

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            count += 1
        else:
            # Start a new increasing segment
            count = 1
            start = i

        # Update only when a longer segment is found
        if count > max_count:
            max_count = count
            max_start = start

    return (max_count, max_start)


numbers = [1, 2, 3, 2, 4, 5, 6]

print(longest_increasing(numbers))
