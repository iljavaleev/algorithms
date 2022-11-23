"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""

def correct_brackets(s):
    l = list(s)
    i = 1
    n = len(l)
    while i < n:
        if i < 0:
            return True
        if 0 < ord(l[i]) - ord(l[i - 1]) <= 2:
            l.pop(i)
            l.pop(i - 1)
            n -= 2
            i -= 1
        else:
            i += 1
    if l:
        return False
    return True

# s = "([{[]}]{({{{}}})})"
s = "(){}}{"
print(correct_brackets(s))
