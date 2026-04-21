def count_char_freq(s):
    freq={}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

print(count_char_freq("shubham"))