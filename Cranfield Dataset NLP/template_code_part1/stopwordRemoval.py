from util import *

from nltk.corpus import stopwords


class StopwordRemoval():

    def fromList(self, text):
        
       # Stopword Removal using NLTK stopword list
        stop_words = set(stopwords.words('english'))
        stopwordRemovedText = []

        for sentence in text:
            #  only keep  words that are not present in the stopword list
            filtered = [
                word for word in sentence
                if word.lower() not in stop_words
            ]
            stopwordRemovedText.append(filtered)

        # Return sentences after stopword removal
        return stopwordRemovedText




	