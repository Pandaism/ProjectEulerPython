# The sum of the squares of the first ten natural numbers is,
#
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


# Time Complexity: O(n)
def solution(limit):
    sum_of_square = 0
    square_of_sum = 0

    for num in range(limit + 1):
        sum_of_square = sum_of_square + pow(num, 2)
        square_of_sum = square_of_sum + num

    return pow(square_of_sum, 2) - sum_of_square


print(solution(100))
