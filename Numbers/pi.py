#!/usr/bin/python

"""
**Find PI to the Nth Digit**
Enter a number and have the program generate PI up to
that many decimal places. Keep a limit to how far the program will go.
"""

def gregory_leibniz_series(n):
    assert n > 0

def nilakantha_series(n):
    assert n > 0

def chudnovsky_algorithm(n):
    assert n > 0

def main():
    print "1) Gregory-Leibniz Series\n"
    print "2) Nilakantha Series\n"
    print "3) Chudnovsky Algorithm\n"

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
        elif method == 2:
            print "Calculating pi using the Nilakantha series..."
        elif method == 3:
            print "Calculating pi using the Chudnovsky algorithm..."
        else:
            print "Invalid option.  Exiting..."
    else:
        print "You must enter a number larger than 0.  Try again..."
        main()

if __name__ == "__main__":
    main()
