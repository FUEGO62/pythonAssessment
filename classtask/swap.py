word = "EOB"



def reverse_string(word):

	reverse = ""

	count = 0

	for i in word:

		count+=1

	counter = count-1

	while(counter>-1):

		reverse += word[counter]

		counter-=1

	return reverse

print(reverse_string(word))