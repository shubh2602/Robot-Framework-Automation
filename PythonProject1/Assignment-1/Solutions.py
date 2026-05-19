def Reverse_words_order_in_sentence(sentence):
    words = sentence.split()
    reverse = words[::-1]
    return ' '.join(reverse)

print(Reverse_words_order_in_sentence("messi is the goat"))

def Find_largest_word_in_sentence(sentence):
    words= sentence.split()
    largest = ""
    for word in words:
        if len(word) > len(largest):
            largest = word
    return largest
print(Find_largest_word_in_sentence("messi is the goat"))

def Count_frequency_of_each_word_in_sentence(sentence):
    words = sentence.split()
    freq = {}
    for char in words:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

print(Count_frequency_of_each_word_in_sentence("messi is the goat messi"))

def Find_common_characters_between_two_strings(s1,s2):
    for char in s1:
        if char in s2:
            print(char, end=" ")

Find_common_characters_between_two_strings("shubham","pandeyu")        

def Second_most_non_repeating_character(s):
    freq={}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    values = list(freq.values())
    unique = list(set(values))

    if len(unique)<2:
        return "No second most non repeating character"
    
    unique.sort(reverse=True)
    second = unique[1]
    for char in freq:
        if freq[char] == second:
            return char

print(Second_most_non_repeating_character("shubham"))

lst = [1, 2, 3, 5]

n = 5

expected_sum = n * (n + 1) // 2

actual_sum = sum(lst)

missing_number = expected_sum - actual_sum

print("Missing number is:", missing_number)