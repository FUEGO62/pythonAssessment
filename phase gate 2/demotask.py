string1 = input("enter a number ")

sum = 5

is_string = False

for char in string1:
		
	mark = 0

	for count in range(10):

		if char == str(count): mark =1

	if mark == 0 and char != "-" and char!="." :

		print("invalid") 
		is_string = True
		break




if is_string == False : print(sum+ float(string1))