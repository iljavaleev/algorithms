def reverse(text):
    l = list(text)
    for i in range(len(l)):
        l.insert(i, (l.pop()))
    return ''.join(l)

print(reverse('peter'))
