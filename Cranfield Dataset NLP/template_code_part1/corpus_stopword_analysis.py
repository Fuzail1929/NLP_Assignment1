import json
from collections import defaultdict
from nltk.corpus import stopwords
import nltk

# First ,we will try to make sure NLTK stopwords are downloaded already
nltk.download('stopwords')


# Load tokenized documents
with open("output/tokenized_docs.txt", "r") as f:
    docs = json.load(f)

doc_count = len(docs)


# we now Computing the Document Frequency

df = defaultdict(int)

for doc in docs:
    unique_terms = set()
    for sentence in doc:
        for word in sentence:
            unique_terms.add(word.lower())
    for term in unique_terms:
        df[term] += 1


# Now , Build Corpus-Based Stopwords

threshold = 0.7   #  setting the limit to find the stopwords : 70% of documents

corpus_stopwords = set()

for term, freq in df.items():
    if freq / doc_count > threshold:
        corpus_stopwords.add(term)


# Load NLTK Stopwords
nltk_stopwords = set(stopwords.words('english'))


# Comparison between the two stopword lists : 

overlap = corpus_stopwords.intersection(nltk_stopwords)
only_corpus = corpus_stopwords - nltk_stopwords
only_nltk = nltk_stopwords - corpus_stopwords


# Printing the Results for beeter understanding of the differences between the two stopword lists

print("\n--- STOPWORD ANALYSIS ---\n")

print("Total documents:", doc_count)
print("Corpus-based stopwords:", len(corpus_stopwords))
print("NLTK stopwords:", len(nltk_stopwords))
print("Overlap:", len(overlap))

# Print some sample words from each category for better understanding
print("\nSample words only in corpus-based list:")
print(list(only_corpus)[:15])

print("\nSample words only in NLTK list:")
print(list(only_nltk)[:15])