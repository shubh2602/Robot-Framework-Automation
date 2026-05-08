def reverse_first_word(sentence):

    words = sentence.split()
    first_word = words[0]
    rev = ""

    for char in first_word:
        rev = char + rev

    words[0] = rev
    result = " ".join(words)

    return result

sentence = input("Enter an sentence - ")
print(reverse_first_word(sentence))