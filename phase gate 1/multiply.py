def multiply(number1, number2):

	product = 0
	is_negative = False
	denominator = 1
	

	if type(number1)!=type("string") and type(number2)!=type("string"):

		if number1 < 0:

			number1 = -number1
			is_negative = True
	
		if type(number1)== type(3.3):

			while(number1 != int(number1)):

				for number in range(10):

					number1 += number1

				for number in range(10):

					denominator += denominator

		
			for number in range(int(number1)):
	
				product += number2
	
			product/=denominator
		
		if type(number1)== type(3):

			for number in range(number1):

				product += number2



		if is_negative :

			product = -product

	return product


