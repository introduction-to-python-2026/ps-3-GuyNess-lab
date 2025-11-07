n_terms = 10
list_of_numbers = []
for i in range(n_terms):
    list_of_numbers.append(i)
    
list_of_alternating_signs = []
for i in range(n_terms):
    if i % 2 == 0:
        list_of_alternating_signs.append(1)
    else:
        list_of_alternating_signs.append(-1)

leibniz_series = []
for i in range(n_terms):
    leibniz_series.append(1 / (2 * i + 1) * list_of_alternating_signs[i])

leib_sum = sum(leibniz_series)
pi_val = 4 * leib_sum

def approximate_pi(n_terms):
    leibniz_series = [] 

    for k in range(n_terms):
        term = ((-1) ** k) / (2 * k + 1)
        leibniz_series.append(term)

    return 4 * sum(leibniz_series)
