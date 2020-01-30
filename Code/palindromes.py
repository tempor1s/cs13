#!python

import string
import re
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


# def is_palindrome_iterative(text):
#     text_lower = re.sub("[ ,.;:?!]", "", text.lower())
#     lower_reversed = text_lower[::-1]
#     if text_lower == lower_reversed:
#         return True
#     else:
#         return False

# my version
def is_palindrome_iterative(text):
    # clean the text with a joined filter (remove punctuation)
    clean_text = ''.join(filter(
        lambda character: character not in " ,.;:?!-_'", text.lower()))

    # get the length so we dont need to calculate twice
    length = len(clean_text)

    # loop through half the array
    for i in range(length//2):
        # check if the index we are at is not same in the second half of the array going in reverse
        if clean_text[i] != clean_text[length-(i + 1)]:
            return False
    # the string is a palindrome if we never return false
    return True


def is_palindrome_recursive(text):
    # clean up the text
    clean_text = ''.join(filter(
        lambda character: character not in " ,.;:?!-_'", text.lower()))

    return _palindrome_helper(clean_text)


def _palindrome_helper(text):
    # If the length of the text is less than 1 return true, because it is a palindrome and we do not want to go out of range
    if len(text) < 1:
        return True
    else:
        # check if the left most and right most characters are the same
        if text[0] == text[-1]:
            # return the string but with those two characters removed
            return _palindrome_helper(text[1:-1])
        else:
            # return false
            return False


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
