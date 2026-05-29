"""
## Task: Horspool Search First Match

### Write a function:
    def horspool_search(text, pattern):

The function should use Horspool's Algorithm to find the first occurrence of pattern in text.

### Functionalities:
- Build the shift table from pattern.
- Align pattern with text.
- Compare characters from right to left.
- If all characters match, return the starting index.
- If mismatch occurs, shift the pattern based on the text character aligned with the last pattern character.

### Return rules:
- Return the index of the first match.
- Return -1 if pattern is not found.

### Example:
Input:  text = "ABCXABCD", pattern = "ABCD"
Output: 4

Input:  text = "HELLO WORLD", pattern = "WORLD"
Output: 6

Input:  text = "ABCDEFG", pattern = "XYZ"
Output: -1
"""

from build_shift_table import build_shift_table


def horspool_search(text, pattern):
    n = len(text)
    m = len(pattern)

    if m == 0:
        return 0
    
    shift = build_shift_table(pattern)

    pos = m - 1

    while pos < n:
        j = m - 1
        i = pos

        while j >= 0 and text[i] == pattern[j]:
            i -= 1
            j -= 1

        if j < 0:
            return i + 1
        
        current = text[pos]
        pos += shift.get(current, m)

    return -1


def main():
    text_1 = "ABCXABCD"
    pattern_1 = "ABCD"
    print(horspool_search(text_1, pattern_1)) # 4

    text_2 = "HELLO WORLD"
    pattern_2 = "WORLD"
    print(horspool_search(text_2, pattern_2)) # 6

    text_3 = "ABCDEFG"
    pattern_3 = "XYZ"
    print(horspool_search(text_3, pattern_3)) # -1


if __name__ == "__main__":
    main()