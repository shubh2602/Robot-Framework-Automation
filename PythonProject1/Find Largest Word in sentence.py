def Find_Largest_Word_in_sentence(sentence):
    words = sentence.split()

    largest_word = sentence[0]

    for word in words:
        if len(word)>len(largest_word):
            largest_word = word
        
    return largest_word

print(Find_Largest_Word_in_sentence("fifa world cup in coming"))