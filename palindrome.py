from string import digits, ascii_letters

def isPalindrome(string):
    """
    Returns True if the string word is a palindrome.

    Input:
        word (string)

    Return:
        bool
    """
    string = ''.join([char for char in string if char in ascii_letters + digits]).lower()
    stringLength = len(string)
    oddLength = stringLength % 2 != 0

    for i in range(stringLength // 2 - oddLength):
        if string[i] == string[-1 - i]:
            continue
        else:
            return False
    return True