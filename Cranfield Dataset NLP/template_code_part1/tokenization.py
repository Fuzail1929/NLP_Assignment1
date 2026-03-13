from util import *


import re
import spacy
from nltk.tokenize import TreebankWordTokenizer


class Tokenization():

    def __init__(self):
        
        # Load spaCy language model once to avoid repeated loading
        self.nlp = spacy.load("en_core_web_sm")

    def naive(self, text):
        
        #Tokenization using a Naive Approach
        #  used regex to split words and punctuation
        tokenizedText = []

        for sentence in text:
            
             # Extract words (\w+) and punctuation ([^\w\s])
            
            tokens = re.findall(r"\w+|[^\w\s]", sentence)
            tokenizedText.append(tokens)

        return tokenizedText


    def pennTreeBank(self, text):
        
        # Tokenization done using Penn Treebank Tokenizer (NLTK)

        tokenizer = TreebankWordTokenizer()
        tokenizedText = []

        for sentence in text:
            # Apply PTB tokenizer on each sentence
            tokens = tokenizer.tokenize(sentence)
            tokenizedText.append(tokens)

        return tokenizedText


    def spacyTokenizer(self, text):
    
       # Tokenization using spaCy's linguistic features
        tokenizedText = []

        for sentence in text:
            # applying it on every sentence to get tokens with linguistic features
            doc = self.nlp(sentence)
            tokens = [token.text for token in doc]
            tokenizedText.append(tokens)

        return tokenizedText