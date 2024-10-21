def sum_of_evens(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(sum_of_evens(numbers))