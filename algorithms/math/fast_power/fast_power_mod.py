"""
Example:
Input:  base = 2, exponent = 10, mod = 1000
Output: 24

Explanation:
2^10 = 1024
1024 % 1000 = 24

---

Input:  base = 3, exponent = 5, mod = 7
Output: 5

Explanation:
3^5 = 243
243 % 7 = 5
"""


def main():
    print(fast_power_mod(3, 5, 7))
    print(fast_power_mod(2, 10, 1000))


def fast_power_mod(base, exponent, mod):
    if (exponent < 0):
        exponent = -exponent
        base = 1 / base
    
    result = 1

    while (exponent > 0):
        if (exponent % 2 == 1):
            result = (result * base) % mod
        base = (base * base) % mod
        exponent //= 2

    return result


if __name__ == "__main__":
    main()