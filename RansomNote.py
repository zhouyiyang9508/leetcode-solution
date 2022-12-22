from collections import Counter

def canConstruct(ransomNote: str, magazine: str) -> bool:
    counter_r = Counter(ransomNote)
    counter_m = Counter(magazine)

    for ch, freq in counter_r.items():
        if counter_m[ch] < freq:
            return False

    return True

if __name__ == '__main__':
    print(canConstruct('aa', 'aab'))