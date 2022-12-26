def check_no_duplicate_chars(text):
    return len(set(text.lower())) == len(text)


print(check_no_duplicate_chars('Micha'))