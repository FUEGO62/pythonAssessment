count = 1000
number = 1;
digit = 0
even_count = 0


while count <= 3000:
	
	number = count
	even_count = 0

	while number!=0:
	
		digit = number%10
		number//=10
		if digit%2 == 0:

			even_count+=1
		if even_count == 4:

			print(count , end="")
			if count !=2888: print("," , end="")

	count+=1