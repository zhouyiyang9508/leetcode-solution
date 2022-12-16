from typing import List

def restoreIpAddresses(s: str) -> List[str]:
    def dfs(s, index, temp, res):
        # too many parts
        if index > 4:
            return
        # just the same as valid IP, empty s, remove redundant '.' of temp
        if index == 4 and not s:
            res.append(temp[:-1])

        # start from 1
        for i in range(1, len(s) + 1):
            # if s has a leading zero or in range of 1-255
            if s[:i] == '0' or (s[0] != '0' and 0 < int(s[:i]) < 256):
                dfs(s[i:], index + 1, temp + s[:i] + '.', res)

    res = []
    dfs(s, 0, '', res)
    return res

if __name__ == '__main__':
    print(restoreIpAddresses('25525511135'))
    print(restoreIpAddresses('0000'))
