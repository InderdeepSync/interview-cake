import random


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def shuffle(the_list: list):
    shuffled = []

    while the_list:
        random_index = get_random(0, len(the_list) - 1)
        num = the_list.pop(random_index)
        shuffled.append(num)

    the_list.extend(shuffled)



if __name__ == "__main__":
    input_list = [1, 2, 3, 4, 5]
    shuffle(input_list)
    print(input_list)