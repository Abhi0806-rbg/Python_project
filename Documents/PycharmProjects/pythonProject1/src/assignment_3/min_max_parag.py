import re
from collections import Counter


def word_frequency_analysis(text):
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)

    max_freq = max(word_counts.values())
    min_freq = min(word_counts.values())

    max_words = [word for word, count in word_counts.items() if count == max_freq]
    min_words = [word for word, count in word_counts.items() if count == min_freq]

    print("Word(s) appearing maximum times:")
    for word in max_words:
        print(f"{word}: {max_freq} times")

    print("\nWord(s) appearing minimum times:")
    for word in min_words:
        print(f"{word}: {min_freq} times")

#  Define the input text before calling the function
text = """Comprehensions are a feature of Python which I would really miss if I ever have to leave it.
Comprehensions are constructs that allow sequences to be built from other sequences.
Several types of comprehensions are supported in both Python 2 and Python 3."""

#  Now call the function
word_frequency_analysis(text)