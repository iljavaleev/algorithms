def contains_rotation(str1, str2):
    return str2.lower() in str1.lower() * 2

print(contains_rotation('ABCD', 'ABC'))
print(contains_rotation('ABCDEF', 'EFAB'))
print(contains_rotation('BCDE', 'EC'))
print(contains_rotation('Challenge', 'GECH'))
