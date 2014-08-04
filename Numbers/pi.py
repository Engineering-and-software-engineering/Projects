#!/usr/bin/python
import math

"""
**Find PI to the Nth Digit**
Enter a number and have the program generate PI up to
that many decimal places. Keep a limit to how far the program will go.
"""

def gregory_leibniz_series(n):
    assert n > 0

    pi = 1
    limit = 10000
    
    for i in range(2, limit, 1):
        pi += ((-1.0) ** (i + 1.0)) / (2.0 * i - 1.0)
    pi = 4 * pi
    print """
        Gregory-Leibniz Series
        pi = 4 (1 - (1/3) + (1/5) - (1/7) + ... (-1)^(i+1) / (2i -1))

        Leibniz's formula converges extremely slowly and is fairly inaccurate
        Calculating pi to 10 correct decimal places using direct summation
        of the series requires about 5,000,000,000 terms
        """        
    return pi    

def nilakantha_series(n):
    assert n > 0

def chudnovsky_algorithm(n):
    assert n > 0

def main():
    print "1) Gregory-Leibniz Series\n"
    print "2) Nilakantha Series\n"
    print "3) Chudnovsky Algorithm\n"
    print "4) Built in math library\n"

    method = raw_input("Which method would you like to use? ")
    try:
        method = int(method)
    except ValueError:
        print "Invalid input.  Exiting..."
        exit(0)

    n = raw_input("How many numbers do you need? ")
    try:
        n = int(n)
    except ValueError:
        print "Invalid input.  Exiting..."
        exit(0)
    if n > 0:
        if method == 1:
            print "Calculating pi using the Gregory-Leibniz series..."
            pi = gregory_leibniz_series(n)
        elif method == 2:
            print "Calculating pi using the Nilakantha series..."
        elif method == 3:
            print "Calculating pi using the Chudnovsky algorithm..."
        elif method == 4:
            print "Calculating pi using the built in math library..."
            pi = math.pi
        else:
            print "Invalid option.  Exiting..."
            exit(0)
        print '%.*f' % (n, pi)
    else:
        print "You must enter a number larger than 0.  Try again..."
        main()

if __name__ == "__main__":
    main()
