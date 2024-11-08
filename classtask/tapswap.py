def swap(numbers):
	
	for counter in range(len(numbers)):

		if counter%2==0:

			numbers[counter+1]= numbers[counter] + numbers[counter+1]
			numbers[counter] = numbers[counter+1]- numbers[counter]
			numbers[counter+1] = numbers[counter+1] - numbers[counter]

	return numbers

  