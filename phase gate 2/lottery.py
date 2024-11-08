lucky_numbers = ["31","15","61"]

numbers = input("enter your numbers ")

numbers = numbers.split(" ")

count_check = 0

done = False

for count in range(3) :

	if numbers[count] == lucky_numbers[count] : count_check+=1


if count_check == 3 : 

	print("You have won $5000.0!!")
	done = True

if done == False:

	count_check = 0

	for count in range(3) :

		for counter in range(3) :

			if numbers[count] == lucky_numbers[counter] : numbers[count] = '*'


	for count in range(3):

		if numbers[count] == '*' : count_check +=1


	if count_check == 3 : print("You have won $4000.0!!")
	if count_check == 2 : print("You have won $3000.0!!")
	if count_check == 1 : print("You have won $2000.0!!")

