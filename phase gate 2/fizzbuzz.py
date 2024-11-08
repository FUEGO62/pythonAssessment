for count in range(1,51):

	if count%3==0 and count%5!=0: print("fizz ",end="")

	elif count%5==0 and count%3!=0: print("buzz ",end="")

	elif count%3==0 and count%5==0: print("fizzbuzz ",end="")

	else: print(count ,end=" ")