
def generatepassword():

	import random

	small_letters = ""
	big_letters = ""
	numbers = ""
	symbols = ""
	password = ""

	password_length = random.randint(16,20)

	for count in range(5):

		small_letters += chr(random.randint(97,122))
		big_letters += chr(random.randint(65,90))
		numbers += chr(random.randint(48,57))
		symbols += chr(random.randint(33,47))

	password = small_letters + big_letters + numbers + symbols

	strong_password = ""

	for count in range(password_length):

		strong_password += password[random.randint(0,15)]

	return strong_password
	

print(generatepassword())