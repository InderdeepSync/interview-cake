

def is_valid(code):
    stack = []
    openers = ('(', '[', '{')
    closers = (')', ']', '}')

    for ch in code:
        if ch in openers:
            stack.append(ch)
        else:
            if not stack or openers.index(stack[-1]) != closers.index(ch):
                return False

            stack.pop()


    return not stack










if __name__ == "__main__":
    print(is_valid('([]{[]})[]{{}()}'))