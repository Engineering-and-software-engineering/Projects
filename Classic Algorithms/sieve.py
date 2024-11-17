"""
Sieve of Eratosthenes
find the prime under threshold (default to 1000)
"""
import math


def sievePrime(n=1000):
    lst = range(0, n + 1)
    lst[1] = 0
    thres = int(math.sqrt(n)) + 1
    for i in xrange(2, thres):
        if lst[i] == 0:
            continue
        for j in xrange(i * 2, len(lst), i):
            if lst[j] != 0:
                lst[j] = 0
    return [i for i in lst if i != 0]


if __name__ == "__main__":
    try:
        n = int(raw_input("Enter a positive integer as threshold: "))
    except ValueError:
        print "Enter only a positive integer, n > 1"
        print "default 1000"
    print sievePrime(n)
