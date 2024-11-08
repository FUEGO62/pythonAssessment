list = ["1","*","3","*","5"]

for count in range(6):

	for counter in range(count):

		print(list[counter],end=" ")

	print()

for count in range(5):

	print(list[count],end=" ")

print()

for count in range(6):

	for counter in range((4-count)):

		print(list[counter],end=" ")

	print()