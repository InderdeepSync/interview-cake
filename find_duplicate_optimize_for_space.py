


def find_repeat(numbers):
    lower = 1
    upper = len(numbers) - 1

    while lower < upper:
        mid = (lower + upper) // 2
        count = 0
        for num in numbers:
            if lower <= num <= mid:
                count += 1

        if count > (mid - lower + 1):
            upper = mid
        else:
            lower = mid + 1

    return lower




if __name__ == "__main__":
    print(find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5]))