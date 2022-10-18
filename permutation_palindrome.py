
def has_palindrome_permutation(the_string):
    counts = {}

    for ch in the_string:
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1

    number_of_odd_counts = 0
    for count in counts.values():
        if count % 2 == 1:
            number_of_odd_counts += 1
            if number_of_odd_counts == 2:
                return False

    return True



if __name__ == "__main__":
    print(has_palindrome_permutation("aabccbdd"))