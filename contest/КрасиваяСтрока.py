def pretty(S, k):
    n = len(S)
    l = 26 * [0]
    maxi = 1
    for s in S:
        l[ord(s) - 97] += 1
        maxi = max(l[ord(s) - 97], maxi)
    if n - 1 >= k:
        print(maxi + k)
    else:
        print(maxi + n - 1)


def pretty2(S, k):
    max_count = 0
    for char in set(S):
        l = r = 0
        count = k
        while r < len(S):
            if char != S[r] and count > 0:
                count -= 1
            elif char != S[r]:
                if S[l] != char:
                    count += 1
                l += 1
                continue
            r += 1
            total = r - l
            max_count = max(max_count, total)
    print(max_count)


if __name__ == '__main__':
    k = int(input())
    S = input()
    pretty2(S, k)