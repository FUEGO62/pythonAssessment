def get_total(list):

	total = 0

	for score in list:

		total+= score


	return total	

scores = []

score = 1
total = 0

while score!=0 :

	score = int(input("Enter you scores, press 00 to quit: "))

	if score!=0:
		scores.append(score)
		#total+= score
	

print(scores)

print(get_total(scores)/len(scores))

	

		
