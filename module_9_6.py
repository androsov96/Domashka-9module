def all_variants(text):
    x = len(text)
    for g in range(x):
        yield text[g]
    for j in range(2, x + 1):
        for y in range(x - j + 1):
            z = y + j
            yield text[y:z]

a = all_variants('abc')

for i in a:
    print(i, end=' ')
