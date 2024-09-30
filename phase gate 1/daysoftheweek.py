
def getDay(day):

	match(day):

		case 0 : day = "Sunday"

		case 1 : day = "Monday"

		case 2 : day = "Tuesday"

		case 3 : day = "Wednesday"

		case 4 : day = "Thursday"

		case 5 : day = "Friday"

		case 6 : day = "Saturday"

	return day


day = int(input("Enter todays day "))

future_day = int(input("Enter number of days elapsed since today ")) + day

day = getDay(day)

future_day = getDay(future_day)

	
print("Todays day is", day, "and the future day is",future_day )