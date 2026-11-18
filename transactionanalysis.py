""" Write a function that processes transaction amounts in one pass
and returns the count of amounts above a configurable threshold 
(default 100), the largest amount, the smallest amount, and the 
average; handle empty input safely.
"""
def transaction_analysis(amounts, threshold=100):
    if len(amounts) == 0:
        return None

    count = 0
    total = 0
    largest = amounts[0]
    smallest = amounts[0]

    for amount in amounts:
        total += amount

        # Count amounts greater than the threshold
        if amount > threshold:
            count += 1

        # Update largest and smallest values
        if amount > largest:
            largest = amount

        if amount < smallest:
            smallest = amount

    average = total / len(amounts)

    return count, largest, smallest, average


transactions = [50, 150, 200, 80, 300]

print(transaction_analysis(transactions))