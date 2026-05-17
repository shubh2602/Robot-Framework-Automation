# def Reverse_words_order_in_sentence(sentence):
#     words = sentence.split()
#     reversed_words = words[::-1]
#     return ' '.join(reversed_words)

# print(Reverse_words_order_in_sentence("python is easy to learn"))

# def Find_largest_word_in_sentence(sentence):
#     words= sentence.split()
#     largest_word = ""
#     for word in words:
#         if len(word) > len(largest_word):
#             largest_word = word
#     return largest_word
# print(Find_largest_word_in_sentence("python is easy to learn"))

# def Count_frequency_of_each_word_in_sentence(sentence):
#     words = sentence.split()
#     freq = {}
#     for char in words:
#         if char in freq:
#             freq[char] += 1
#         else:
#             freq[char] = 1
#     return freq

# print(Count_frequency_of_each_word_in_sentence("messi is the goat messi"))

def Find_common_characters_between_two_strings(s1,s2):
    for char in s1:
        if char in s2:
            print(char, end=" ")

Find_common_characters_between_two_strings("shubham","pandeyu")        