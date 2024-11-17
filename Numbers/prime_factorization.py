#!/usr/bin/python

"""
    Have the user enter a number and 
    dislay all Prime Factors (if there are any)
"""

"""
    Check whether the given number is prime or not
"""
def isPrime(x):
    # 1 and 2 are both prime numbers...
    if x ==1 or x == 2:
        return True

    # If it's divisible by 2, it's not a prime number...
    if x % 2 == 0:
        return False

    # If x is evenly disivisble by 3, or any number up to sqrt(x) + 1
    # the number is not a prime number 
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False

    return True

def main():
    for i in range(1, 100):
        print "The number %d is prime: %r" % (i, isPrime(i))

if __name__ == "__main__":
    main()
