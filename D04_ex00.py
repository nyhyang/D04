#!/usr/bin/env python
# D04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports
import random 
# Body

random_integer = random.randint(1, 25)


guesses_left = 5
while guesses_left > 0:
	try:
		number = float(input('Enter a number: '))
		if int(number) == random_integer:
			print("You're awesome!")
		elif int(number) < random_integer:
			print("Too low, give it another try.")
		else:
			print("Too high, give it another try.")
			break
		guesses_left -= 1
	except:
		print('Nice try, enter a number')




################################################################################
def main():


    print("Hello World!") # Remove this and replace with your function calls
    

if __name__ == '__main__':
    main()