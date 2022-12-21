import collections


def removeDuplicates(s: str) -> str:
    stack = collections.deque()
    for i in range(len(s)):
        if stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    return ''.join(stack)

if __name__ == '__main__':
    print(removeDuplicates("abbaca"))

