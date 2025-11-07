def move(my_list, direction):

    # בדיקה שיש בדיוק אחד
    if my_list.count(1) != 1:
        raise ValueError("my_list must contain exactly one '1'")

    index_of_one = my_list.index(1)
    n = len(my_list)

    if direction == 'right':
        # בדוק שאפשר לזוז ימינה בלי לצאת מהטווח
        if index_of_one < n - 1:
            my_list[index_of_one] = 0
            my_list[index_of_one + 1] = 1
        # אחרת — נותר ללא שינוי

    elif direction == 'left':
        # בדוק שאפשר לזוז שמאלה בלי לצאת מהטווח (וללא שימוש באינדקסים שליליים)
        if index_of_one > 0:
            my_list[index_of_one] = 0
            my_list[index_of_one - 1] = 1
        # אחרת — נותר ללא שינוי

    else:
        raise ValueError("direction must be 'left' or 'right'")

    return my_list
