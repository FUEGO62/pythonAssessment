try:

	year = int(input("enter the time in years "))
	
	if year<= 0: raise ValueError

	amount = 0
	investment = float(input("enter your investment "))

	if investment <= 0: raise ValueError
	
	rate = float(input("enter the rate "))

	if rate < 0: raise ValueError

	for count in range(year):

		amount = investment*(1+(rate/100))

		print("year",(count+1)," N{:,.2f}".format(amount))
	
		

		investment = amount

except ValueError: print("invalid")