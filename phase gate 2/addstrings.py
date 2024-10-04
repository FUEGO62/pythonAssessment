def addstrings(string1 , string2):

	mark = 0		


	for char in string1:
		
		mark = 0

		for count in range(10):

			if char == str(count): mark =1

		if mark == 0 and char != "-" and char!="." : raise ValueError	

	for char in string2:
		
		mark = 0

		for count in range(10):

			if char == str(count): mark =1

		if mark == 0 and char != "-" and char!="." : raise ValueError	
	

	if mark > 0: number1 = float(string1)
	if mark > 0: number2 = float(string2)


	return number1+number2