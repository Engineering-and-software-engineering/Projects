"""
Sieve of Eratosthenes -
It is a simple, ancient algorithm
for finding all prime numbers up to any given limit.
It does so by iteratively marking as composite (i.e. not prime),
the multiples of each prime, starting with the multiples of 2.
"""

def sieve(n):
    is_prime = [False] * 2 + [True] * (n - 1) 
    for i in xrange(int(n**0.5 + 1.5)): # stop at ``sqrt(n)``
        if is_prime[i]:
            for j in xrange(i*i, n+1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]

def main():
    try:
        n = int(raw_input('Enter a number: '))
        print sieve(n)
    except ValueError:
        print 'Enter only an integer value, n > 1.'
        main()
        
if __name__ == '__main__':
    main()
