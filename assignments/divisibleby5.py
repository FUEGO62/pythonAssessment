def divide_or_square(number):

	if number < 0:
		raise ValueError("Enter a valid input")

	if number % 5 == 0 and number >0:

		return number**0.5
	else:
		return number % 5