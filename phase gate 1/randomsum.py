import random

def check_answer (total,answer):

	if total == answer:

		return True

	else :

		return False



number1 = random.randrange(0,100)
number2 = random.randrange(0,100)

total = number1 + number2

print("number1 is ", number1, "number2 is", number2)

answer = int(input("Enter the sum of these numbers : "))

print(check_answer(total,answer))


