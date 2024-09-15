def get_future_value(investment_amount,monthly_interestRate,years):

	months = years*12

	if (years*10)%10 > 0:
	
		raise ValueError("Invalid input")

	
	if investment_amount < 0 or monthly_interestRate < 0 or years < 0:

		raise ValueError("Invalid input")

	else:
		return investment_amount*(1+monthly_interestRate)**(months)

	