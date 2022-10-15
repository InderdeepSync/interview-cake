import math


def reverse(list_of_chars: list[str]):
    for i in range(math.floor(len(list_of_chars)/2)):
        temp = list_of_chars[i]
        list_of_chars[i] = list_of_chars[len(list_of_chars) - i - 1]
        list_of_chars[len(list_of_chars) - i - 1] = temp


if __name__ == "__main__":
    list1 = ["A", "B", "C", "D", "E"]
    reverse(list1)

    print(list1)