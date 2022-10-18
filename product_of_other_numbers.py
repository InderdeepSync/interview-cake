

def get_products_of_all_ints_except_at_index(int_list):
    if len(int_list) <= 1:
        raise Exception()

    products_before_index = [1]
    for number in int_list[:-1]:
        products_before_index.append(products_before_index[-1] * number)

    products_after_index = [1]
    for number in reversed(int_list[1:]):
        products_after_index.insert(0, products_after_index[0] * number)

    result = []
    for i in range(len(int_list)):
        result.append(products_before_index[i] * products_after_index[i])

    return result



if __name__ == "__main__":
    print(get_products_of_all_ints_except_at_index([1]))