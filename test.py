from palindrome import isPalindrome

strings = ['arara',
           'Hannah', 
           'only', 
           'radar', 
           'level', 
           'amora', 
           "A man, a plan, a canal – Panama", 
           "A Toyota! Race fast, safe car! A Toyota!",
           "Are we not drawn onward to new era?",
           "Are Mac ‘n’ Oliver ever evil on camera?"]

for string in strings:
    print(string, isPalindrome(strings))