def remove_vowel(str):
    vowels = "aeiouAEIOU"
    result = ""

    for char in str:
        if char not in vowels:
            result = result+char

    return result

print(remove_vowel("elephant"))