"""
Task: Horspool Search All Matches

Write a function:
    def horspool_all_matches(text, pattern):

The function should return all starting indices where pattern appears in text using Horspool's Algorithm.

Functionalities:
- Use Horspool's shifting logic.
- Continue searching after a successful match.
- Store all match positions in a list.

Return rules:
- Return a list of all starting indices.
- Return an empty list if no match exists.

Example:
Input:
text = "ABCDABCDABCD"
pattern = "ABCD"

Output:
[0, 4, 8]

Example:
Input:
text = "AAAAAA"
pattern = "AAA"

Output:
[0, 1, 2, 3]
"""

from build_shift_table import build_shift_table


def horspool_all_matches(text, pattern):
    ans = []
    n = len(text)
    m = len(pattern)

    if m == 0 or m > n:
        return ans
    
    shift = build_shift_table(pattern)

    pos = m - 1

    while pos < n:
        j = m - 1
        i = pos

        while j >= 0 and text[i] == pattern[j]:
            i -= 1
            j -= 1

        if j < 0:
            ans.append(i + 1)
            pos += 1
        else:
            current = text[pos]
            pos += shift.get(current, m)

    return ans


def main():
    text_1 = "ABCDABCDABCD"
    pattern_1 = "ABCD"
    print(horspool_all_matches(text_1, pattern_1))

    text_2 = "AAAAAA"
    pattern_2 = "AAA"
    print(horspool_all_matches(text_2, pattern_2))


if __name__ == "__main__":
    main()