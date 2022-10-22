
def find_duplicate(int_list):
    slow = fast = head = len(int_list)

    while True:
        slow = int_list[slow - 1]
        fast = int_list[int_list[fast - 1] - 1]

        if slow == fast:
            break

    while head != slow:
        head = int_list[head - 1]
        slow = int_list[slow - 1]

    return head


if __name__ == "__main__":
    print(find_duplicate([4, 1, 4, 8, 3, 2, 7, 6, 5]))