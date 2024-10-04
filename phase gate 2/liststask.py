list = [1,2,3,4,5,6,7,8,9,0]
list_length = 0
sum = 0
even_sum = 0
odd_sum = 0
product = 1

for object in list:

	if list_length%2 != 0: even_sum += object
	else : odd_sum += object
	if (list_length+1) %3 == 0: product*= object
	list_length+=1
	sum+=object


average = sum/list_length

print(list_length,even_sum,odd_sum,product,average)