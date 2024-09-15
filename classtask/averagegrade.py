total = 0
count = 0

while True:
	score= float(input("Enter score:, enter 00  "))
	total+=score
	count += 1
	if score == 0:

		break

average = total/(count-1)

print(round(average,2))