# Exercises
import re
import random

def read_file(filename):
    """Read the content of a file and return it as a string."""
    with open(filename, 'r', encoding="utf-8") as file:
        return file.read()

def extract_words(text):
    """Extract words from text and return a list of words (case-insensitive)."""
    return re.findall(r'\b\w+\b', text.lower())

def count_unique_words(text):
    """Count the number of unique words in the text."""
    words = extract_words(text)
    return len(set(words))

def find_longest_word(text):
    """Find the longest word in the text."""
    words = extract_words(text)
    return max(words, key=len) if words else None

def count_word_occurrences(text, target_word):
    """Count occurrences of a specific word (case-insensitive)."""
    words = extract_words(text)
    return words.count(target_word.lower())

def percentage_longer_than_avg(text):
    """Calculate the percentage of words that are longer than the average word length."""
    words = extract_words(text)
    if not words:
        return 0.0

    avg_length = sum(len(word) for word in words) / len(words)
    longer_words = [word for word in words if len(word) > avg_length]

    return (len(longer_words) / len(words)) * 100

def get_random_word(text):
    """Pick a random word from the text."""
    words = extract_words(text)
    return random.choice(words) if words else None

def get_random_unique_word(text):
    """Pick a random unique word from the text."""
    unique_words = list(set(extract_words(text)))
    return random.choice(unique_words) if unique_words else None

def random_word_occurrences(text):
    """Select a random word and return its occurrences."""
    word = get_random_unique_word(text)
    return word, count_word_occurrences(text, word) if word else (None, 0)





