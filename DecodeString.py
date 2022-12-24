import collections


def decodeString(s: str) -> str:
    stack = collections.deque()
    currNum, currStr = 0, ''
    for ch in s:
        if ch == '[':
            stack.append(currStr)
            stack.append(currNum)
            currStr = ''
            currNum = 0
        elif ch == ']':
            num = stack.pop()
            previous = stack.pop()
            currStr = previous + num * currStr
        elif ch.isdigit():
            currNum = currNum * 10 + int(ch)
        else:
            currStr += ch
    return currStr

if __name__ == '__main__':
    print(decodeString("3[a]2[bc]"))
    print(decodeString("3[a2[c]]"))