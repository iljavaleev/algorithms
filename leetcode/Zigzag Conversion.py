"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"


Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
"""

def convert(s, numRows):
    l = [list() for _ in range(numRows)]

    if numRows == 1:
        return s

    row = 0
    in_row = True

    for i in range(len(s)):
        l[row].append(s[i])

        if row == numRows - 1:
            in_row = False
        elif row == 0:
            in_row = True

        if in_row:
            row += 1
        else:
            row -= 1

    return ''.join([item for sublist in l for item in sublist])

str = "A"
n = 4

assert convert(str, n) == "A"

