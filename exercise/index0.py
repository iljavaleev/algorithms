import re
import sys

# WORD_RE = re.compile(r'\w+')
# index = {}
#
# with open(sys.argv[1], encoding='utf-8') as fp:
#     for line_no, line in enumerate(fp, 1): # start from 1
#         for match in WORD_RE.finditer(line):
#             word = match.group()
#             column_no = match.start() + 1
#             location = (line_no, column_no)
#             occurrences = index.get(word, [])
#             occurrences.append(location)
#             index[word] = occurrences
#
# # display in alphabetical order
# for word in sorted(index, key=str.upper):
#     print(word, index[word])


WORD_RE = re.compile(r'\w+')
index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index.setdefault(word, []).append(location)

    # display in alphabetical order
for word in sorted(index, key=str.upper):
    print(word, index[word])


l = ['spam', 'spam', 'eggs', 'spam', 'bacon', 'eggs']
# dict.fromkeys(l).keys()
# list(dict.fromkeys(l).keys())