def Second_most_frequent_character(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    values = list(freq.values())

    unique_values = list(set(values))

    if len(unique_values)<2:
        return "No second most frequent character"

    unique_values.sort(reverse=True)

    second_most_value = unique_values[1]

    result = []
    for char in freq:
        if freq[char] == second_most_value:
            result.append(char)
    return result

print(Second_most_frequent_character("aabbbcddeee"))