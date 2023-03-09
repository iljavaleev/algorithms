def to_europe(s, N):
    l = []
    for i in range(len(s)):
        j = i + 1
        while j < N:
            if s[i] > s[j]:
                l.append(j)
                break
            j += 1
        else:
            l.append(-1)
    return l

def to_europe2(s, N):
    global_min = N - 1
    l = [-1] * N
    local_min = N - 1
    for i in range(N-2, -1, -1):

        if s[i] <= s[global_min]:
            global_min = i
            continue

        if s[i] > s[i + 1]:
            l[i] = i + 1
            local_min = i + 1

        elif s[i] < s[i + 1]:
            if s[local_min] >= s[i]:
                l[i] = global_min
                local_min = i
            else:
                l[i] = local_min

    return l

def to_europe3(s, N):
    l = [-1] * N
    data = tuple(zip(s, range(N)))
    stack = [data[0]]

    for i in range(1, len(data)):
        if stack[-1][0] < data[i][0]:
            stack.append(data[i])
        else:
            while stack and stack[-1][0] > data[i][0]:
                v, it = stack.pop()
                l[it] = data[i][1]
            stack.append(data[i])
    return l


if __name__ == '__main__':
    N = int(input())
    l = [int(x) for x in input().split()]
    print(*to_europe3(l, N))
