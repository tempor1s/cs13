#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # LMAOOO
    # return int(digits, base) # i feel like this was cheating... haha

    decoded_val = 0  # final return value
    # Get the power of the right most digit (highest power)
    power = len(digits) - 1
    # string of digits (0-9 + a-z)
    convert_string = string.digits + string.ascii_lowercase
    # loop through the digits
    for i in digits:
        # decode the current digit
        decoded_digit = (convert_string.index(i) * pow(base, power))
        # add that value to our total
        decoded_val += decoded_digit

        power -= 1  # decrease the power by 1

    return decoded_val  # return the final total of all of the digits


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    # convert_string = 0-9 + a-z
    convert_string = string.digits + string.ascii_lowercase
    # If the number is less than the base, just return the index of that character
    # because strings can be indexed like arrays to get the char at that position
    if number < base:
        return convert_string[number]
    # Otherwise, divide the number by the base to be the new number, and pass
    # it and the base into encode recursivly Also add that string + the remainder
    # of the current number % the base
    else:
        return encode(number // base, base) + convert_string[number % base]


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    return encode(decode(digits, base1), base2)


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(
            digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')
    val = encode(10, 2)
    print(val)


if __name__ == '__main__':
    main()
