'''
Prime number facts:
1. Two is the only even Prime number
2. Every prime number in form of 6n+1 or 6n-1 except 2 and 3,
where n is natural number

3. Two and Three are only two consecutive natural numbers which
are prime too

4. Goldback Conjecture: Every even integer greater than 2 can be
expressed as the sum of two primes

5. Wilson Theorem: Wilson's theorems states that a natural number p > 1
is a prime number if and only if
(p - 1) != -1 mod p || (p - 1) != (p - 1) mod p

6. Fermat's Little Theorem: if n is a prime number, then for every a,
 1 <= a <= n:
 a ** (n - 1) = 1 (mod n) || a ** (n - 1) % n = 1

7. Prime Number Theorem: The probability that a given, randomly chosen
number n is prime is inversely proportional to its number of digits,
or to the lograithm of n

8. Lemoine's Conjecture: Any odd integer greater than 5 can be expressed
as a sum of an odd prime (all primes other than 2 are odd) and an even
semiprime. A semiprime number is a product of two prime numbers.
'''

def checkIfPrime(num):
    isPrime = False
    # corner case
    if num <= 1:
        return isPrime
    else: # 2 to n - 1
        for i in range(2, num):
            if (num % i == 0):
                return isPrime
    return not isPrime

print(checkIfPrime(19))