def count_digits(s):
    count = 0

    for char in s:
        if char.isdigit():
            count +=1
    return count

print(count_digits("s1h2u3b4ha5m"))