def Character_frequency_in_sequence(s):

    freq = {}

    for char in s:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1

    result = ""
    for char in freq:
        result += char + str(freq[char])

    return result

print(Character_frequency_in_sequence("aabbcaadb"))