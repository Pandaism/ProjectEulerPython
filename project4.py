# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.


# Solution is O(n^2)
def solution(digits):
    upper_limit = pow(10, digits) - 1
    lower_limit = pow(10, digits - 1)
    largest_palindrome = 0

    for a in range(upper_limit, lower_limit, -1):
        for b in range(a, lower_limit, -1):
            ans = a * b

            if is_palindrome(ans):
                if ans > largest_palindrome:
                    largest_palindrome = ans
    return largest_palindrome


def is_palindrome(num):
    return str(num) == str(num)[::-1]


print(solution(3))
