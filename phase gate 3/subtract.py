import random

def check_answer (difference,answer,score):

	if difference == answer:

		score +=1
		print("correct")

	return score	

count = 0
score = 0

while count<3:

	number1 = random.randrange(0,100)
	number2 = random.randrange(0,100)



	difference = number1 - number2

	if number2 < number1 :print("number1 is ", number1, "number2 is", number2)
	else : 

		print("number1 is ", number2, "number2 is", number1)

		difference*=-1

	answer = int(input("Enter the difference of these numbers : "))
	
	score = check_answer(difference,answer,score)
	
	count+=1
	
print("you got ",score, "/10")


