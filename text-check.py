#Importing necessary libraries
import re
import string
from collections import Counter
from wordcloud import WordCloud
from nltk.tokenize import sent_tokenize, word_tokenize
import matplotlib.pyplot as plt
from nltk.util import ngrams

#CREATING THE FUNCTIOINS:
# To clean the text and generate identifier
def clean_identified_text(text):
    # Remove punctuation
    # Convert text to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    # Generating identifier to the text
    identifier = word_tokenize(text)
    return identifier

# To calculate no.of words
def words_count(identifier):
    return len(identifier)

# To calculate number of unique words
def unique_words_count(identifier):
    return len(set(identifier))

# To calculate average word length
def average_word_length(identifier):
    total_characters = sum(len(word) for word in identifier)
    return total_characters / len(identifier)

# To find the most frequent word
def most_frequent_word(identifier):
    word_counter = Counter(identifier)
    return word_counter.most_common(1)[0][0]


# To count sentences
def sentences_count(text):
    return len(sent_tokenize(text))

# To calculate percentage of uppercase letters
def percentage_uppercase_letters(text):
    total_letters = sum(c.isalpha() for c in text)
    uppercase_letters = sum(c.isupper() for c in text)
    return (uppercase_letters / total_letters) * 100

# To find the longest and shortest sentences
def longest_shortest_sentences(text):
    sentences = sent_tokenize(text)
    longest_sentence = max(sentences, key=lambda sentence: len(word_tokenize(sentence)))
    shortest_sentence = min(sentences, key=lambda sentence: len(word_tokenize(sentence)))
    return longest_sentence, shortest_sentence

# To find the 5 most frequent bigrams
def most_frequent_bigrams(bigrams):
    bigram_counter = Counter(bigrams)
    return bigram_counter.most_common(5)

# To generate bigrams
def generate_bigrams(identifier):
    return list(ngrams(identifier, 2))


# To generate word cloud
def generate_word_cloud(identifier):
    word_freq = Counter(identifier)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

# Read text file
with open('Txt file for Task 01 (Easy).rtf', 'r') as file:
    text = file.read()

# Clean and tokenize text
identifier = clean_identified_text(text)

# Using the functions
num_words = words_count(identifier)
num_unique_words = words_count(identifier)
most_freq_word = most_frequent_word(identifier)
avg_word_length = average_word_length(identifier)
num_sentences = sentences_count(text)
longest_sentence, shortest_sentence = longest_shortest_sentences(text)
uppercase_percentage = percentage_uppercase_letters(text)
bigrams = generate_bigrams(identifier)
top_5_bigrams = most_frequent_bigrams(bigrams)






