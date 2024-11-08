zero_list = 5*[4*[0]]

print(zero_list)

for count in range(len(zero_list)):

	for counter in range(len(zero_list[count])):

		print(zero_list[count][counter],end=" ")

	print()