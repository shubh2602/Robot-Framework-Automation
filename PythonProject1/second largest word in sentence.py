def  Find_second_largest_word_in_sentence(sentence):
    words = sentence.split()
    largest = words[0]
    
    for word in words:
        if len(word)>len(largest):
            largest = word
    
    sec_largest = ""
    
    for word in words:
        if word == largest:
            continue
        if len(word)>len(sec_largest):
            sec_largest=word
    
    return sec_largest

print(Find_second_largest_word_in_sentence("python automation framework selenium"))