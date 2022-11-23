"""
Given a string s. Return all the words vertically in the same order in which they appear in s.
Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
Each word would be put on only one column and that in one column there will be only one word.

Input: s = "HOW ARE YOU"
Output: ["HAY","ORO","WEU"]
Explanation: Each word is printed vertically.
 "HAY"
 "ORO"
 "WEU"

Input: s = "TO BE OR NOT TO BE"
Output: ["TBONTB","OEROOE","   T"]

Input: s = "CONTEST IS COMING"
Output: ["CIC","OSO","N M","T I","E N","S G","T"]
"""

def get_words(s):
    l = [list(x) for x in s.split()]
    max_l = 0
    for i in l:
        inner_len = len(i)
        if inner_len > max_l:
            max_l = inner_len

    for i in l:
        inner_len = len(i)
        if max_l > inner_len:
            add_to = max_l - inner_len
            i += [' '] * add_to
    result = []
    print(l)
    for i in range(max_l):
        a = ''
        for s in l:
            a += s[i]
        result.append(a.rstrip())

    return result


print(get_words("TO BE OR NOT TO BE"))
