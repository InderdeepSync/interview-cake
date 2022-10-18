

def merge_lists(list1, list2):
    l1 = l2 = 0

    merged = []
    while l1 < len(list1) and l2 < len(list2):
        if list1[l1] < list2[l2]:
            merged.append(list1[l1])
            l1 += 1
        else:
            merged.append(list2[l2])
            l2 += 1

    if l1 == len(list1):
        while l2 < len(list2):
            merged.append(list2[l2])
            l2 += 1
    else:
        while l1 < len(list1):
            merged.append(list1[l1])
            l1 += 1

    return merged



if __name__ == "__main__":
    my_list = [3, 4, 6, 10, 11, 15]
    alices_list = [1, 5, 8, 12, 14, 19]

    print(merge_lists(my_list, alices_list))