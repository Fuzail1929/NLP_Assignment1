from util import *

# Add your import statements here
import re
import nltk
import spacy
from nltk.tokenize import sent_tokenize


class SentenceSegmentation():

    def __init__(self):
        # Loading the  spaCy model
        self.nlp = spacy.load("en_core_web_sm")

    def naive(self, text):

        # First we do the Splitting using punctuation marks
        segmentedText = re.split(r'[.!?]+', text)

        # Then , we removed all extra spaces and empty strings
        segmentedText = [
            sent_text.strip()
            for sent_text in segmentedText
            if sent_text.strip()
        ]

        return segmentedText


    def punkt(self, text):

        # first Perform sentence segmentation using NLTK's Punkt tokenizer
        segmentedText = sent_tokenize(text)

        # Then Return list of segmented sentences
        return segmentedText


    def spacySegmenter(self, text):

        # Use spaCy NLP pipeline to identify sentence boundaries
        doc = self.nlp(text)

        # Use spaCy NLP pipeline to identify sentence boundaries 
        segmentedText = [sent.text.strip() for sent in doc.sents]

        # Return list of segmented sentences
        return segmentedText