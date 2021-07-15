def frac_knapsack(list_of_tuple_weight_val, capacity):
    """
    input --> list_of_tuple_weight_val = [(2, 8), (3,4)], capacity : int
    return ---> {(2,8): 1, (3,4): 0.75}
    """
    density = []
    knapsack = {}
    for weight_val in list_of_tuple_weight_val:
        density.append((weight_val, weight_val[1]/weight_val[0]))
    density = list(
        sorted(density, key=lambda item: item[1], reverse=True))

    while capacity and density:
        weight = density[0][0][0]
        if capacity >= weight:
            knapsack[density[0][0]] = 1
            capacity -= weight
            density.pop(0)
        else:
            fraction = capacity / weight
            knapsack[density[0][0]] = fraction
            capacity = 0

    return knapsack


print(frac_knapsack([(2, 8), (3, 4), (7, 3), (10, 12)], 1))
