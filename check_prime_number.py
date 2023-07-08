# https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/

def is_prime_trial_division(n):

    if n <= 1:
        return False

    # the square root of n (rounded down to the nearest integer)
    for i in range(2, int(n**0.5)+1):
        # If n is divisible by any of these numbers, return False
        if n % i == 0:
            return False
          
    # If n is not divisible by any of these numbers, return True
    return True
