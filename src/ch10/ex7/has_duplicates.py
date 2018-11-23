def has_duplicates(s):
    t = list(s)
    t.sort()

    for i in range(len(t) - 1):
        if t[i] == t[i + 1]:
            return True
    return False

print(has_duplicates('cba'))
print(has_duplicates('abba'))
