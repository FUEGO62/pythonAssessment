number =int(input("Enter your number: "))



def number_processing(number):
	number2 = number
	sum =  0
	temp = 0
	count = 0
	digit_counter = 0
	difference = 0

	
	if number<10 and number>1:

		return number

	if number>10 and number < 1000:

		while number!=0:

			remainder = number % 10
	
			number//=10

			checker = remainder % 2

			sum += remainder

			temp += remainder

			difference = remainder-temp+1

			if checker != 0:

				count+=1

			digit_counter+=1
	
	if digit_counter<4 and digit_counter>1:

		if count == 0:

			return sum

	if digit_counter == 3:

		if count == 3:

			return difference

	if digit_counter == 2:

		if count == 2:

			return difference
	
	if number2>999 or number2<2:

		return "Invalid input!!!"	

print(number_processing(number))

	
	