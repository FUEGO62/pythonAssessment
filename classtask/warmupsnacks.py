def construct_list():
    sequential_list = []
    for number in range(1,16):
        sequential_list.append(number)

    return sequential_list

def duplicate(array):
    for index in range(len(array)):
        array[index] *=2
    return array

def remove_duplicates(array):
    new_array = []
    present = False

    for index in range(len(array)):
        present = False
        for index2 in range(len(new_array)):
            if array[index]==new_array[index2]:
                present = True
        if not present:
            new_array.append(array[index])

    return new_array

def add_every_third(array):
    total = 0
    for index in range(len(array)):
        if (index+1) % 3 == 0:
            total += array[index]

    return total

def add_first_last_and_middle(array):
    total =array[0] + array[len(array) - 1]
    if len(array) % 2 == 0:
        total += (array[len(array)//2] + array[(len(array)//2)-1])/2
    else: total += array[len(array)//2]
    return total



