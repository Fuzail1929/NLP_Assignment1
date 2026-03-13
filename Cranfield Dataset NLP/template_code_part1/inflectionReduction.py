from util import *

from nltk.stem import PorterStemmer, WordNetLemmatizer


class InflectionReduction:

    def porterStemmer(self, text):
        
        #Inflection Reduction using Porter Stemmer
        
        stemmer = PorterStemmer()
        reducedText = []

        for sentence in text:
            # Apply stemming to each word in the sentence  
            reducedText.append(
                [stemmer.stem(word) for word in sentence]
            )

        # Return stemmed sentences
        return reducedText


    def wordnetLemmatizer(self, text):
        
       # Perform lemmatization using NLTK's WordNet Lemmatizer
        
        lemmatizer = WordNetLemmatizer()
        reducedText = []

        for sentence in text:

            # Convert each word to its base (dictionary) form
            reducedText.append(
                [lemmatizer.lemmatize(word) for word in sentence]
            )

        # Return lemmatized sentences
        return reducedText


    def reduce(self, text):
       
        # Wrapper function to apply selected inflection reduction method
        # Currently using WordNet Lemmatizer
        
        reducedText = self.wordnetLemmatizer(text)
        return reducedText