q = 123
R = 100003
s = 'HaSH'

# print(ord('a') % R)
# if len(s) == 1:
#     print(ord('a') % R)
# else:
#     a = ord(s[0]) * q + ord(s[1])
#     n = 2
#     while n < len(s):
#         a = a * q + ord(s[n])
#         n += 1
#     print(a % R)


# print(r % R)


def poly_hash(s, q, R):
    p_power = 1
    hash_val = 0

    for c in s[::-1]:
        hash_val = (hash_val + ord(c) * p_power) % R
        p_power = (p_power * q) % R

    return hash_val


def get(s, q, R):
    n = len(s)
    r = ord(s[0])
    for i in range(0, n):
        r = r * q + ord(s[i])
    return r % R


def get_hash_dict(s, q, R):
    d = {}
    for i in range(1, len(s) + 1):
        d[i] = get(s[:i], q, R)
    for c in s:
        d[f'{c}'] = get(c, q, R)
    return d


def slice_hash(s, q, R, i, j):
    d = get_hash_dict(s, q, R)
    if i == j:
        return d[s[i-1]] % R
    elif i == 1:
        return d[j] % R
    else:
        n = j - i + 1
        return (d[j] - d[j - n] * q**n) % R


if __name__ == '__main__':
    q = int(input())
    R = int(input())
    s = input()
    m = int(input())
    for i in range(m):
        l, r = [int(x) for x in input().split()]
        print(poly_hash(s[l - 1:r], q, R))


