

def convert(s: str, numRows: int) -> str:
    words = [''] * numRows
    index = 0
    upper = False

    for x in s:
        words[index] += x
        if index == 0:
            upper = False
        if index == numRows - 1:
            upper = True
        if upper:
            index -= 1
        if not upper:
            index += 1

    return ''.join(words)


if __name__ == '__main__':
    print(convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR')