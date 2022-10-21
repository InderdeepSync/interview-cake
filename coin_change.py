

def change_possibilities(amount, denominations):
    if amount == 0:
        return 1

    if len(denominations) == 0:
        return 0

    number_of_ways = 0

    while amount >= 0:
        number_of_ways += change_possibilities(amount, denominations[:-1])

        highest_denomination = denominations[-1]
        amount -= highest_denomination


    return number_of_ways






if __name__ == "__main__":
    print(change_possibilities(4, (1, 2, 3)))
