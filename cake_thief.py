from pprint import pprint

import math


def max_duffel_bag_value(cake_tuples, weight_capacity):
    table = [[0 for _ in range(weight_capacity + 1)] for _ in range(len(cake_tuples) + 1)]

    for i in range(1, len(cake_tuples) + 1):
        for j in range(1, weight_capacity + 1):
            temp = -math.inf

            # To account for the case when item weight = 0 but item value is non-zero
            if cake_tuples[i - 1][0] == 0 and cake_tuples[i - 1][1] != 0:
                temp = math.inf
            elif cake_tuples[i - 1][0] <= j:
                temp = cake_tuples[i - 1][1] + table[i][j - cake_tuples[i - 1][0]]

            table[i][j] = max(table[i - 1][j], temp)


    return table[-1][-1]






if __name__ == "__main__":
    # (weight, value)
    print(max_duffel_bag_value([(0, 5)], 5))