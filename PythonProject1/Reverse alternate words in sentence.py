def reverse(word):
    rev = ""

    for char in word:
        rev = char + rev

    return rev

def reverse_alternate_words_in_sentence(sentence):
    words = sentence.split()
    result = []

    for i in range(len(words)):
        if i%2!=0:
            reverse_word = reverse(words[i])
            result.append(reverse_word)
        else:
            result.append(words[i])

    final = " ".join(result)
    return final

print(reverse_alternate_words_in_sentence("hello how are you"))