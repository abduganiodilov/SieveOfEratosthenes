import random            # Imports the 'random' module to generate random numbers
import math              # Imports the 'math' module for mathematical functions (e.g., sqrt)


def sieve_of_eratosthenes(arr: list, n: int):
    # Defines a function that implements the Sieve of Eratosthenes.
    # 'arr' is a list of booleans indicating whether a number is prime.
    # 'n' is the upper bound for the range in which we search for prime numbers.

    for k in range(2, int(math.sqrt(n)) + 1):
        # Loops from 2 up to the integer part of the square root of 'n'.
        # We only need to sieve multiples up to sqrt(n).

        if arr[k]:
            # Checks if 'k' is still marked as True (meaning 'k' is prime).

            for j in range(k * k, n, k):
                # For each multiple of 'k' starting from k*k up to 'n', step by 'k'.

                arr[j] = False
                # Marks each multiple of 'k' as False (not prime).

    return [i for i, val in enumerate(arr) if val]
    # Returns a list of all indices 'i' where the corresponding value 'val' is True (prime).


N = random.randint(2, 1000)
# Generates a random integer 'N' between 2 and 1000.

primes = [True] * N
# Creates a list called 'primes' of length 'N' and initializes all elements to True.

primes[0] = primes[1] = False
# Sets the first two elements (indices 0 and 1) to False,
# because 0 and 1 are not considered prime numbers.

prime_numbers = sieve_of_eratosthenes(primes, N)
# Calls the sieve_of_eratosthenes function with the 'primes' list and the upper bound 'N',
# and stores the resulting list of prime numbers in 'prime_numbers'.

print(prime_numbers)
# Prints out the list of prime numbers.
