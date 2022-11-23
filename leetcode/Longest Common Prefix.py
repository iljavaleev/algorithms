"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string ''

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

def find_pref(strings):
    strings.sort(key=len)
    res = []
    first_string = strings[0]
    len_first = len(first_string)
    len_strings = len(strings)
    j = 0
    if not first_string:
        return ''
    if len_strings == 1:
        return strings[0]
    while j < len_first:
        sym = first_string[j]
        for i in range(1, len_strings):
            if sym != strings[i][j]:
                return ''.join(res)
        j += 1
        res.append(sym)
    return ''.join(res)

strs = ["ab", 'a']
print(find_pref(["flower","flow","flight"]))
# print(find_pref(strs))

# s = ["ab", "b"]
# s.sort(key=len)
# print(s)


