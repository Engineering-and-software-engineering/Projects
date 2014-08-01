#!/usr/bin/python

"""
**Fibonacci Sequence**
Enter a number and have the program generate the Fibonacci sequence
to that number or to the Nth number.
"""

def fibonnaciSequence(n):
    assert n > 0

    sequence = [1]  # Initialize sequence to 1
    while len(sequence) < n:
        if len(sequence) == 1:
            # If the length of sequence is 1, append 1 to the end so the series is 1, 1 so far
             sequence.append(1)
        else:
            # Add the previous 2 numbers in the series, and append it to the list
            sequence.append(sequence[-1] + sequence[-2]) 
    for i in range(len(sequence)):
        # Convert the numbers to strings
        sequence[i] = str(sequence[i])
    # Return the sequence, separated by commas
    return (', '.join(sequence))

def main():
    n = raw_input('How many numbers do you need? ')
    try:
        n = int(n)
    except ValueError:
        print "Invalid input.  Exiting..."
        exit(0)

    if n > 0:
        print fibonnaciSequence(n)
    else:
        print "You must enter a number larger than 0.  Try again..."
        main()

if __name__ == "__main__":
    main()
