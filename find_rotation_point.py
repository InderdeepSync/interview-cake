

def word_comes_before(word1, word2):
    p = 0

    while p <= len(word1) - 1 and p <= len(word2) - 1:
        diff = ord(word1[p]) - ord(word2[p])
        if diff != 0:
            return diff < 0

        p += 1

    return True if p == len(word2) else False

def find_rotation_point(words):
    for index, word in enumerate(words[1:], start=1):
        if word_comes_before(word, words[index - 1]):
            return index



if __name__ == "__main__":
    print(find_rotation_point(['cape', 'cake']))