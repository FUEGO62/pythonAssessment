
deposit = 1

withdraw = 1

total_deposit = 0

total_withdraw=0


userInput = int(input("press 00 to quit enter 1 to deposit: "))


if userInput == 1:

	while deposit!=0:

		deposit = float(input(" how much do you want to deposit : "))
		total_deposit+=deposit

userInput = int(input("press 00 to quit  enter 2 to withdraw : "))

if userInput == 2:

	while withdraw!=0:

		withdraw = float(input(" how much do you want to withdraw : "))
		total_withdraw+=withdraw

balance = total_deposit - total_withdraw

if balance>=0:

	print("your balance is ",balance)

if balance<0:

	print("YOU CANT WITHDRAW MORE THAN YOU DEPOSIT!!!")



	