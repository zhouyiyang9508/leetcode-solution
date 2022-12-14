
def checkValidString(s: str) -> bool:
    balance = 0
    for char in s:
        if char in '(*':
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            return False

    balance = 0
    for char in reversed(s):
        if char in ')*':
            balance += 1
        else:
            balance -= 1

        if balance < 0:
            return False

    return True

if __name__ == '__main__':
    print(checkValidString("()"))
    print(checkValidString("(*))"))