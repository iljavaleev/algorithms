'''
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

st = "abcabcbb"

def ind_substr_l(s):
    n = len(s)
    if n == 0: return 0
    m = 1
    for i in range(n):
        if i + 1 == n:
            return m
        result = [s[i]]
        count = 1
        for j in range(i + 1, n):
            if s[j] not in result:
                result.append(s[j])
                count += 1
                if count == n:
                    return count
                if m < count:
                    m = count
            else:
                break

    return m

print(ind_substr_l(st))