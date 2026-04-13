"""
Input:  a = 3, mod = 7
Output: 5

Explanation:
3 * 5 % 7 = 1
"""

def main():
    print(modular_inverse(2, 5))


def modular_inverse(a, mod):
    return fast_power_mod(a, mod-2, mod)


def fast_power_mod(base, exponent, mod):
    result = 1

    while exponent > 0:
        if (exponent % 2 == 1):
            result = (result * base) % mod
        base = (base * base) % mod
        exponent //= 2
    
    return result


if __name__ == "__main__":
    main()