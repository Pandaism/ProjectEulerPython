# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


# Best Case: O(n) Worst Case: O(n * a + b)
def solution(divisible_limit):
    store = {}
    for num in range(2, divisible_limit + 1):
        if is_prime(num):
            store[num] = 1
        else:
            factors = get_factors(num)
            for factor in factors:
                if store.keys().__contains__(factor):
                    if store[factor] < factors[factor]:
                        store[factor] = factors[factor]
                else:
                    store[factor] = factors[factor]

    ans = 1

    for i in store:
        ans = ans * pow(i, store[i])

    return ans


# Best Case: O(n) Worst Case: O(n + a)
def get_factors(num):
    factors = {}

    # O(n)
    for i in range(2, num):
        if num % i == 0:
            factors[i] = 1
            num = num / i

    # is_prime: O(a) or O(1)
    if is_prime(num) and num > 1:
        if factors.keys().__contains__(num):
            factors[num] = factors[num] + 1

    return factors


# Best Case: O(1) Worst Case: O(a)
def is_prime(num):
    if num <= 2:
        return True

    if num % 2 == 0:
        return False

    for i in range(3, int(num / 2), 2):
        if num % i == 0:
            return False

    return True


print(solution(20))
