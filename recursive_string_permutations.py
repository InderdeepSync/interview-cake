

def get_permutations(string):
    if len(string) <= 1:
        return {string}

    result = set()
    for permutation in get_permutations(string[1:]):
        for i in range(len(permutation) + 1):
            result.add(permutation[:i] + string[0] + permutation[i:])

    return result


if __name__ == "__main__":
    print(get_permutations(""))