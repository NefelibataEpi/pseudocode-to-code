"""
## Task: Build Shift Table

Write a function:
    def build_shift_table(pattern):

The function should build the shift table used in Horspool's Algorithm.

---

Functionalities:
- Let m be the length of pattern.
- For each character in pattern except the last character:
    shift[char] = m - 1 - index
- Characters not in the table are assumed to have shift value m.

---

Return rules:
- Return a dictionary containing shift values for characters in the pattern.
- Do not include the last character unless it appears earlier in the pattern.

---

Example:
Input:  pattern = "ABCD"
Output: {"A": 3, "B": 2, "C": 1}

Input:  pattern = "ABCA"
Output: {"A": 3, "B": 2, "C": 1}
"""

def build_shift_table(pattern):
    shift = {}
    length = len(pattern)

    for i in range(length - 1):
        shift[pattern[i]] = length - 1 - i

    return shift


def main():
    pattern_1 = "ABCD"
    print(build_shift_table(pattern_1))

    pattern_2 = "ABCA"
    print(build_shift_table(pattern_2))


if __name__ == "__main__":
    main()