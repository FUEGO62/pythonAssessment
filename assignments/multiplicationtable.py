number = input("Enter a number :")

number = float(number)

float_check = (number*10)%10

	
if float_check!=0 :
	print("ENTER A WHOLE NUMBER!")

if float_check==0 :
	number = int(number)

	count = 1

	while count<11:
		print(number, "x" ,count,"=",number*count)
	
		count+=1