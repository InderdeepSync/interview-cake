
def is_subsequence(str1, str2):
    if not str1:
        return True

    p1 = 0
    for i in range(len(str2)):
        if str2[i] == str1[p1]:
            p1 += 1
            if p1 == len(str1):
                return True
    else:
        return False


def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    return is_subsequence(take_out_orders, served_orders) and is_subsequence(dine_in_orders, served_orders) and len(served_orders) == len(take_out_orders) + len(dine_in_orders)



if __name__ == "__main__":
    print(is_first_come_first_served([27, 12, 18], [55, 31, 8], [55, 31, 8, 27, 12, 18]))
