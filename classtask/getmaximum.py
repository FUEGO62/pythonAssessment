def getmaximum(greatest,number2,number3):

	if number2 > greatest:

		greatest = number2

	if number3 > greatest:

		greatest = number3

	return greatest

print(getmaximum(5,1,10))


	

def getminimum(smallest,number2,number3):

	if number2 < smallest:

		smallest = number2

	if number3 < smallest:

		smallest = number3

	return smallest

print(getminimum(0.4,0,-9))

