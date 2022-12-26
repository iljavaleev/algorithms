def capitalize(s):
    lower = range(97, 123)
    diff = 32

    list_of_words = s.split()
    for i in range(len(list_of_words)):
        w = list_of_words[i]
        if ord(w[0]) in lower:
            list_of_words[i] = chr(ord(w[0]) - diff) + w[1:]

    return ' '.join(list_of_words)


print(capitalize('this is a very special title'))


def capitalize_special_2(words, ignorable_words):
    lower = range(97, 123)
    diff = 32

    for i in range(len(words)):
        w = words[i]
        if ord(w[0]) in lower and w not in ignorable_words:
            words[i] = chr(ord(w[0]) - diff) + w[1:]

    return words


print(capitalize_special_2(['this', 'is', 'a', 'title'], ['is', 'a']))