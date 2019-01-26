# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.'


def solution(num):
    ans = 0
    # Time-Complexity: O(n), Space-Complexity: O(1)
    for i in range(1, num):
        if i % 3 == 0 or i % 5 == 0:
            ans += i
    return ans


print(solution(1000))
