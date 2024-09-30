numbers = [1,2,3]

sorted_numbers = [1,2,3]

flag = 0

numbers[0] = int(input("Enter your number : "))

numbers[1] = int(input("Enter your number : "))

numbers[2] = int(input("Enter your number : "))

largest = numbers[0]
smallest = numbers[0]

for counter in range(3):

	for count in range(3):

		if numbers[count]<smallest:

			smallest = numbers[count]


		if numbers[count]>largest:

			largest = numbers[count]
			flag = count

	
	sorted_numbers[2-counter] = largest
	largest = smallest
	numbers[flag]= smallest



print(sorted_numbers)