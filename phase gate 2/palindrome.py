def reverse(number):

	reverse = 0

	while number!=0:
	
		digit = number%10
		number//=10
		reverse = reverse*10 + digit

	return reverse


def is_palindrome(number):

	if number == reverse(number): 

		return True

	else:

		return False


print(is_palindrome(121))