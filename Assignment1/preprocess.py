import nltk
import pandas as pd
import numpy as np
import re
import unicodedata
import os
import warnings

nltk.download('punkt')
# nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')

from bs4 import BeautifulSoup

from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords

from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
warnings.filterwarnings("ignore", category=DeprecationWarning)

# A part of this code was derived and developed from the following webpage tutorial: https://michael-fuchs-python.netlify.app/2021/05/22/nlp-text-pre-processing-i-text-cleaning/#text-cleaning

# Reading in the documents for preprocessing from the coll folder
cwd = os.getcwd()
path = cwd + "/coll"
files = os.listdir(path)
os.chdir(path)
with open("StopWords.txt", "r") as f:
    stop_words = f.read().splitlines()

# Preprocessing helper functions
def remove_tags(text):
    # Removes the HTML tags from the text
    soup = BeautifulSoup(text, "html.parser")
    strip= soup.get_text(separator=" ")
    return strip

def remove_punctuation(text):
    return re.sub(r'[^\w\s]', '', text) # regex command to remove punctuation

def remove_numbers(text):
    return re.sub(r'\d+', '', text) # regex command to remove numbers

def removeextrawhitespace(text):
    return re.sub(r'^\s*|\s\s*', ' ', text).strip()

def remove_stopwords(text):
    # Removes stopwords from text
    tokens = word_tokenize(text)
    filtered = [word for word in tokens if not word in stop_words]
    return filtered


for file in files:
    with open(file,'r') as f:
        text = f.read()
        text = text.lower()
        text = remove_tags(text)
        text = remove_punctuation(text)
        text = remove_numbers(text)
        text = removeextrawhitespace(text)
        text = remove_stopwords(text)
    
    with open(file,'w') as f:
        for word in text:
            f.write(word)
            f.write(" ")
    f.close()

# def remove_numbers(text):
#     retru
