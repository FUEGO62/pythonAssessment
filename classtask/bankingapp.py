deposit = 0.00
balance = 0.00
withdraw = 0.00
total_deposit = 0.00
total_withdraw = 0.00

def homepage(total_deposit=0,total_withdraw=0):
	choice = int(input("Hello, press \n1. to deposit\n2. to withdraw\n3. to check balance \n"))

	match(choice):
		case 1:
			deposit()
		case 2 :
			withdraw(total_deposit)
		case 3:
			checkbalance(total_deposit,total_withdraw)
			


def deposit():

	total_deposit = 0.00

	while True:

		print("Enter 00 to end deposit")

		balance = float(input("How much do you want to deposit?: ")) 
		
		total_deposit = balance + total_deposit

		if balance == 0.00:

			homepage(total_deposit)
			break

def withdraw(total_deposit = 0):

	total_withdraw = 0.00

	while True:

		print("Enter 00 to end withdrawal")

		withdraw = float(input("How much do you want to withdraw?: ")) 
		
		total_withdraw = withdraw + total_withdraw

		if total_withdraw > total_deposit:

			print("INSUFFICIENT FUNDS!!!")
			break

		if withdraw == 0.00:

			homepage(total_deposit,total_withdraw)
			break

def checkbalance(total_deposit=0,total_withdraw=0):

	balance =(total_deposit - total_withdraw)

	print("your balance is #",balance)



homepage(total_deposit,total_withdraw)