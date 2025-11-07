def move(my_list, direction):

    index_of_one = my_list.index(1)

    try:
        if direction == 'right':
            my_list[index_of_one] = 0
            my_list[index_of_one + 1] = 1

        elif direction == 'left':
            my_list[index_of_one] = 0
            my_list[index_of_one - 1] = 1

    except IndexError:
        my_list[index_of_one] = 1

    return my_list
