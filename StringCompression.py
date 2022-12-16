from typing import List


def compress(chars: List[str]) -> int:
    fast, slow = 0, 0

    while fast < len(chars):
        chars[slow] = chars[fast]

        count = 1
        # count duplicate chars
        while fast + 1 < len(chars) and chars[fast + 1] == chars[fast]:
            fast += 1
            count += 1
        # deal with count >= 10
        if count > 1:
            for c in str(count):
                chars[slow + 1] = c
                slow += 1
        slow += 1
        fast += 1

    return slow

if __name__ == '__main__':
    print(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
