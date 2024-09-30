number = int(input("Enter your number "))

sum = 0;

if number>0 and number<1000:

	while number!=0:

		digits = number%10

		sum+= digits

		number //=10

	print(sum)

else : 

	print("invalid number")


