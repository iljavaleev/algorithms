'Петя записал все числа от 1 до 123 (без пробелов). А потом вычеркнул все девятки. Какая строка у него получилась?'

# def solve():
#     s = ''.join(map(str, range(1, 123 + 1)))
#     s = s.replace('9', '')
#     print(s)

def get_dictionary(s):
    return dict(zip(s, range(len(s))))


def encrypt(s):
    s1 = 'aeiou'
    s2 = 'bcdfghjklmnpqrstvwxyz'

    vovels = get_dictionary(s1)
    n_v = len(vovels)

    sogl = get_dictionary(s2)
    m_sogl = len(sogl)

    d = {}
    for i in s:
        d[i] = d.setdefault(i, 0) + 1

    word = [0] * len(s)

    i = 0
    while i < len(s):
        char = s[i]
        if char in vovels:
            for j in range(d[char]):
                idx = vovels[char] + j * n_v
                word[i] = s2[idx % m_sogl]
                i += 1
        else:
            for j in range(d[char]):
                idx = sogl[char] + j * m_sogl
                word[i] = s1[idx % n_v]
                i += 1

    return ''.join(word)







if __name__ == '__main__':
    # solve()
    print(encrypt('bhao'))