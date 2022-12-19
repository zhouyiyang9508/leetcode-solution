

def characterReplacement(s: str, k: int) -> int:
    left, right = 0, 0

    max_freq = 0
    freq_map = {}
    longest = 0

    while right < len(s):
        freq_map[s[right]] = freq_map.get(s[right], 0) + 1
        max_freq = max(max_freq, freq_map[s[right]])
        valid = (right - left + 1 - max_freq) <= k
        if not valid:
            freq_map[s[left]] -= 1
            left += 1
        longest = max(longest, right - left + 1)
        right += 1
    return longest

if __name__ == '__main__':
    print(characterReplacement("AABABBA", 1))