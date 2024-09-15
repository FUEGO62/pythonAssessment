def my_discount(price,discount):

	if price < 0 or discount < 0:
		raise ValueError("Invalid input")

	else:
		return price-((discount/100)*price)