number1 = 0
sum = 0
number2 = 1
count =0

limit  = int(input("Enter your number\n"))
list = [0]
list [0] = 0

while count!= limit:

	number1 = number2 + sum
	number2 = number1 + sum
	sum = number1 + number2

	list.append(number1)
	list.append(number2)
	list.append(sum)

	count+=1

for count in range(limit):

	print(list[count],end=" ")

