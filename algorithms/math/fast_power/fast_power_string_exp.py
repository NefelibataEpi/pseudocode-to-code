"""
Input:
base = 2
exponent_str = "10"
mod = 1000

Output:
24
"""

def main():
    print(fast_power_string_exp(2, "10", 1000))


def fast_power_string_exp(base, exponent_str, mod):
    result = 1
    
    for digit in exponent_str:
        digit = int(digit)
        result = fast_power_mod(result, 10, mod)
        result = (result * fast_power_mod(base, digit, mod)) % mod

    return result


def fast_power_mod(base, digit, mod):
    result = 1

    while digit > 0:
        if (digit % 2 == 1):
            result = (result * base) % mod
        base = (base * base) % mod
        digit //= 2

    return result


if __name__ == "__main__":
    main()