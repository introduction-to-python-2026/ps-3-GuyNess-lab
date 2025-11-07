def move(my_list, direction):
    index_of_one = my_list.index(1)
    n = len(my_list)

    if direction == 'right':
        if index_of_one < n - 1:
            my_list[index_of_one] = 0
            my_list[index_of_one + 1] = 1

    elif direction == 'left':
        if index_of_one > 0:
            my_list[index_of_one] = 0
            my_list[index_of_one - 1] = 1

    return my_list
