def getFactorial(number):

	factorial = 1	

	while number > 0:

		factorial*=number
		number-=1

	return factorial

def isVowel(letter):

	if letter == 'a'or letter == 'e'or letter == 'i'or letter == 'o'or letter == 'u':

		return True

	else: return False

print(isVowel("i"))
print(getFactorial(5))