# Implementation of the Fizz Buzz problem
# Write a program that prints the numbers from 1 to 100. But for multiples of 
# three print “Fizz” instead of the number and for the multiples of five print
# “Buzz”. For numbers which are multiples of both three and five print 
# “FizzBuzz”.

def fizzbuzz(n):
    for n in range (1, n+1):
        if (n % 3 == 0 and n % 5 == 0):
            print("FizzBuzz")
        elif (n % 5 == 0):
            print("Buzz")
        elif (n % 3 == 0):
            print("Fizz")
        else:
            print(n)

fizzbuzz(100)
