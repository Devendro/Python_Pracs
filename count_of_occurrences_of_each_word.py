sentence = "This is Hello This is not"
words = sentence.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Word Count:", word_count)
