import math


def highest_product_of_3(list_of_ints):
    if len(list_of_ints) < 3:
        raise Exception()

    max_a = max_b = max_c = -math.inf
    min_a = min_b = math.inf

    for index, number in enumerate(list_of_ints):
        if number > max_a:
            max_c = max_b
            max_b = max_a
            max_a = number
        elif number > max_b:
            max_c = max_b
            max_b = number
        elif number > max_c:
            max_c = number

        if number < min_a:
            min_b = min_a
            min_a = number
        elif number < min_b:
            min_b = number

    return max(max_a * max_b * max_c, max_a * min_b * min_a)


if __name__ == "__main__":
    print(highest_product_of_3([6, 1, 3, 5, 7, 8, 2]))
