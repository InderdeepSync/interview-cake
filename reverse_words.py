from reverse_string_in_place import reverse

def reverse_words(msg: list[str]):
    temp = 0
    word = []
    for i in range(len(msg)):
        if msg[i] == " ":
            msg[temp] = word
            msg[temp + 1] = " "
            temp += 2
            word = []
        else:
            word.append(msg[i])

            if i == len(msg) - 1:
                msg[temp] = word
                temp += 1

    del msg[temp:]
    reverse(msg)

    index = len(msg) - 1
    while index >= 0:
        msg[index: index + 1] = msg[index]
        index = index - 2


if __name__ == "__main__":
    message = list('rat the ate cat the')
    reverse_words(message)
    print(message)
    # print("".join(message))