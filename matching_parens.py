

def get_closing_paren(sentence: str, opening_paren_index):
    stack = []
    parenthesis = ("(", ")")
    for index, ch in enumerate(sentence):
        if ch == parenthesis[0]:
            stack.append({'char': ch, 'flag': index == opening_paren_index})
        elif ch == parenthesis[1]:
            item = stack.pop()
            if item['flag']:
                return index


    raise Exception()


if __name__ == "__main__":
    print(get_closing_paren('()()((()()))', 5))