def Move_vowels_left_consonants_middle_special_char(str1):

    vowels = ""
    consonants = ""
    special = ""

    for char in str1:
        if char.isalpha():
            if char.lower() in "aeiou":
                vowels+=char
            else:
                consonants+=char
        else:
            special += char
    result = vowels + consonants + special
    return result

print(Move_vowels_left_consonants_middle_special_char("Hell0 shubHAm@+"))