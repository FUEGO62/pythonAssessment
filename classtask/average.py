'''
request the numbers
store them
find the sum of the numbers
store it
divide the sum by 3
store it as average
display result
'''

print("Enter three numbers and we'll calculate the average ")

number1 = int(input("Number1 :"))

number2 = int(input("Number2 :"))

number3 = int(input("Number3 :"))

sum= number1 + number2 + number3

average = sum/3

print(" The average is",average)