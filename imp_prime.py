from sympy import sieve

# Generate the first 1000 primes using the sieve function from sympy
primes = [p for p in sieve.primerange(2, 1001)]

print(primes)