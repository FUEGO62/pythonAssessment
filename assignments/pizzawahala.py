

print("_________________________________________________")
print("|    Pizza type |Number of Slices|Price per box |")
print("|1.) Sapa Size  |              4 |        2,200 |")
print("|2.) Small Money|              6 |        2,400 |")
print("|3.) Big boys   |              8 |        3,000 |")
print("|4.) Odogwu     |             12 |        4,200 |")
print("_________________________________________________")
print()

number_of_boxes = 0
price = 0
leftover = 0

order = int(input("Place your order...(i.e '3' for 'Big boys') : "))
print()
number = int(input("How many people are eating? : "))
print()

if order == 1:
    order = 4
    number_of_boxes = number // order
    if number % order == 0:
        print("You should buy", number_of_boxes, "boxes!!")
        print("your price is #", 2200 * number_of_boxes)
        print("you have no slices leftover")
    else:
        print("You should buy", number_of_boxes + 1, "boxes!!")
        print("your price is #", 2200 * (number_of_boxes + 1))
        leftover = ((number_of_boxes + 1) * order) - number
        print("you have", leftover, "slices leftover")

elif order == 2:
    order = 6
    number_of_boxes = number // order
    if number % order == 0:
        print("You should buy", number_of_boxes, "boxes!!")
        print("your price is #", 2400 * number_of_boxes)
        print("you have no slices leftover")
    else:
        print("You should buy", number_of_boxes + 1, "boxes!!")
        print("your price is #", 2400 * (number_of_boxes + 1))
        leftover = ((number_of_boxes + 1) * order) - number
        print("you have", leftover, "slices leftover")

elif order == 3:
    order = 8
    number_of_boxes = number // order
    if number % order == 0:
        print("You should buy", number_of_boxes, "boxes!!")
        print("your price is #", 3000 * number_of_boxes)
        print("you have no slices leftover")
    else:
        print("You should buy", number_of_boxes + 1, "boxes!!")
        print("your price is #", 3000 * (number_of_boxes + 1))
        leftover = ((number_of_boxes + 1) * order) - number
        print("you have", leftover, "slices leftover")

elif order == 4:
    order = 12
    number_of_boxes = number // order
    if number % order == 0:
        print("You should buy", number_of_boxes, "boxes!!")
        print("your price is #", 4200 * number_of_boxes)
        print("you have no slices leftover")
    else:
        print("You should buy", number_of_boxes + 1, "boxes!!")
        print("your price is #", 4200 * (number_of_boxes + 1))
        leftover = ((number_of_boxes + 1) * order) - number
        print("you have", leftover, "slices leftover")
