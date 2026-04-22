def duplicate_no(lst):
    seen = set()
    dup = set()

    for char in lst:
        if char in seen:
            dup.add(char)
        else:
            seen.add(char)
    return dup

numb = [1,2,3,2,3,4,5,4,3,4,7,6]
print(duplicate_no(numb))