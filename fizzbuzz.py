'''
Write a program that prints the numbers 1-100, each on a new line
For each number that is a multiple of 3, print “Fizz” instead of the number
For each number that is a multiple of 5, print “Buzz” instead of the number
For each number that is a multiple of both 3 and 5, print “FizzBuzz” instead of the number
'''

for number in range(100):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
