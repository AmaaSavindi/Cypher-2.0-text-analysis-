#Importing necessary libraries
import re
import string
from collections import Counter
from wordcloud import WordCloud
from nltk.tokenize import sent_tokenize, word_tokenize
import matplotlib.pyplot as plt
from nltk.util import ngrams

# Function to clean the text and generate identifier
def clean_identified_text(text):
    # Remove punctuation
    # Convert text to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    # Generating identifier to the text
    identifier = word_tokenize(text)
    return identifier