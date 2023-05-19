def sieve_of_eratosthenes(limit):
    primes = []
    sieve = [True] * (limit + 1)
    for num in range(2, int(limit**0.5) + 1):
        if sieve[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False
    for num in range(int(limit**0.5) + 1, limit + 1):
        if sieve[num]:
            primes.append(num)
    return primes

def first_n_primes(n):
    limit = 30
    while True:
        primes = sieve_of_eratosthenes(limit)
        if len(primes) >= n:
            return primes[:n]
        limit *= 2

n = 1000
prime_numbers = first_n_primes(n)
print(prime_numbers)
