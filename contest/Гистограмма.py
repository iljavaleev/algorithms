def print_gist(S):
    d = {}
    max_val = 0
    for s in S:
        for c in s:
            d[c] = d.setdefault(c, 0) + 1
            max_val = max(d[c], max_val)
    sorted_sym = sorted(d.keys())
    for i in range(max_val, 0, -1):
        for c in sorted_sym:
            if d[c] >= i:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    print(''.join(sorted_sym), end='')


if __name__ == '__main__':
    lines = []
    with open('input.txt') as f:
        for line in f:
            lines.extend(line.split())
    print_gist(lines)