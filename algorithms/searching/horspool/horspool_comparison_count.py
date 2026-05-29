"""
Task: Count Character Comparisons

Write a function:
    def horspool_comparison_count(text, pattern):

The function should use Horspool's Algorithm
and count how many character comparisons are performed.

Functionalities:
- Count every comparison between text[i] and pattern[j].
- Return:
    1. match index
    2. total comparison count

Return rules:
- If pattern exists:
    return (index, comparisons)
- Otherwise:
    return (-1, comparisons)

Example:
Input:
text = "ABCXABCD"
pattern = "ABCD"

Possible Output:
(4, 6)
"""

from build_shift_table import build_shift_table


def horspool_comparison_count(text, pattern):
    n = len(text)
    m = len(pattern)
    count = 0

    if m == 0:
        return 0, 0
    
    shift = build_shift_table(pattern)

    pos = m - 1

    while pos < n:
        j = m - 1
        i = pos

        while j >= 0 and text[i] == pattern[j]:
            count += 1
            i -= 1
            j -= 1

        if j < 0:
            return i + 1, count
        
        current = text[pos]
        pos += shift.get(current, m)
        count += 1

    return -1, count


def main():
    text = "ABCXABCD"
    pattern = "ABCD"
    print(horspool_comparison_count(text, pattern))


if __name__ == "__main__":
    main()