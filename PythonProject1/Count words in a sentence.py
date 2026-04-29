def count_words(str):

    words = str.split()
    count = len(words)
    return count

str1 = "I love my family"
print(count_words(str1))