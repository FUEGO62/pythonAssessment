try:
	width = int(input("Enter the width: "))
	length = int(input("Enter the length: "))

	if(width>0 and length>0):

		lst = length*[width*[0]]

		for count in range(len(lst)):

			for counter in range(len(lst[count])):

				lst[count][counter] = counter*count
				
				print((5-(len(str(lst[count][counter]))))*" ",end="")
				print(lst[count][counter],end="")
				
			print()

	else: print("invalid input")

except ValueError: print("Invalid input")

numbers = [1,3,2]

for count in range(len(numbers)):
	
	for counter in range(len(numbers)-1):

		if numbers[counter]>numbers[counter+1]:

			numbers[counter+1]= numbers[counter] + numbers[counter+1]
			numbers[counter] = numbers[counter+1]- numbers[counter]
			numbers[counter+1] = numbers[counter+1] - numbers[counter]

product = 1

for object in numbers:

	list_length = 0
	if (list_length+1) %3 == 0: product*= object
	list_length+=1


for object in numbers:

	object*=2