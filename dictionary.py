import string

def word_frequency(sentence):
    word_counts = {}
    translator = str.maketrans("", "", string.punctuation)

    # Remove punctuation
    words = sentence.translate(translator).lower().split()

    # Count the frequency of each word
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

# case
sentence = "This is a test sentence. This sentence is a test."

# Test case
result = word_frequency(sentence)
print(result)
