#!python


def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text.

    Time Complexity: O(p * t) -- p being length of pattern and t being length of text
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    return find_index(text, pattern) != None


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found.

    Time Complexity: O(p * t) -- p being length of pattern and t being length of text
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    if len(pattern) > len(text):
        return None

    # check if the pattern is an empty string and return 0 if so
    if pattern == '':
        return 0
    # loop through the text keeping the index and current character
    for i, character in enumerate(text):
        # check if the character is the same as the beginning of the pattern
        if character == pattern[0]:
            # check that if the characters starting at character to the length of the pattern is equal to the pattern
            if text[i:i + len(pattern)] == pattern:
                # return the index if the patterns match
                return i
    # return None if no patterns match
    return None


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    if len(pattern) > len(text):
        return []

    # check if the pattern is an empty string and return a list of all the indexes if true
    if pattern == '':
        return [i for i in range(len(text))]

    # list of indexes to return
    indexes = []
    # loop through the text keeping the index and current character
    for i, character in enumerate(text):
        # check if the character is the same as the beginning of the pattern
        if character == pattern[0]:
            # check that if the characters starting at character to the length of the pattern is equal to the pattern
            if text[i:i + len(pattern)] == pattern:
                # append the index to the list to return
                indexes.append(i)
    # return the list of indexes
    return indexes


def test_string_algorithms(text, pattern):
    # found = contains(text, pattern)
    # print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
