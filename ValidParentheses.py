

def isValid(s: str) -> bool:
    stack = []
    mapping = {')':'(', ']':'[', '}':'{'}

    for char in s:
        # closed bracket
        if char in mapping:
            if stack:
                element = stack.pop()
                # is matched brackets
                if element != mapping[char]:
                    return False
            else:
                return False
        # open bracket
        else:
            stack.append(char)

    # case like ((())
    return not stack


if __name__ == '__main__':
    print(isValid("()"))
    print(isValid("(]"))
    print(isValid("((())"))

