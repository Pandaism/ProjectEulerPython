# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?


# Solution is O(1)
def solution(num):
    largest_prime = 0

    for count in range(2, num, 1):
        if num % count == 0:
            largest_prime = count
            num = num / count

            if num == 1:
                break
    return largest_prime


print(solution(600851475143))
