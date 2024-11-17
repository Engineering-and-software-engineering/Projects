num = int(raw_input('What is your number? '))

sequence = [num]

while sequence[-1] != 1:
	if sequence[-1] % 2 == 1:
		sequence.append(sequence[-1]/2)
	else:
		sequence.append(sequence[-1] * 3 + 1)

print(sequence)
print(len(sequence) - 1)
