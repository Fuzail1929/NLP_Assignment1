# NLP_Assignment1

## Overview

This project implements a complete NLP preprocessing pipeline for the Cranfield Information Retrieval dataset. The system performs:

- Sentence Segmentation
- Tokenization
- Inflection Reduction (Stemming & Lemmatization)
- Stopword Removal
- Corpus-Specific Stopword Analysis
- Theoretical Complexity Analysis

The implementation is modular and configurable via command-line arguments.

---

## Project Structure

    template_code_part1/
    │
    ├── main.py  
    ├── sentenceSegmentation.py  
    ├── tokenization.py  
    ├── inflectionReduction.py  
    ├── stopwordRemoval.py  
    ├── corpus_stopword_analysis.py  
    ├── util.py  
    │
    ├── output/  
    │   ├── segmented_docs.txt  
    │   ├── tokenized_docs.txt  
    │   ├── reduced_docs.txt  
    │   ├── stopword_removed_docs.txt  
    │
    └── README.md  

---

# Requirements

Install required libraries:
        
        pip install nltk spacy


Download spaCy model:
                
                python -m spacy download en_core_web_sm



Download NLTK resources:

      python -m nltk.downloader punkt
      python -m nltk.downloader wordnet
      python -m nltk.downloader omw-1.4
      python -m nltk.downloader stopwords

# Running the Pipeline

Navigate to the project folder:

        cd template_code_part1

emove old output files before running:
          
          rm output/*

---

# Part 1 – Sentence Segmentation

### Naive Sentence Segmentation

      python3 main.py -dataset ../cranfield -segmenter naive
      cp output/segmented_docs.txt output/segmented_docs_naive.txt
      cp output/segmented_queries.txt output/segmented_queries_naive.txt

Punkt Sentence Segmentation

        python3 main.py -dataset ../cranfield -segmenter punkt
        cp output/segmented_docs.txt output/segmented_docs_punkt.txt
        cp output/segmented_queries.txt output/segmented_queries_punkt.txt

# Part 2 – Tokenization

### Naive Tokenizer

    python3 main.py -dataset ../cranfield -tokenizer naive
    cp output/tokenized_docs.txt output/tokenized_docs_naive.txt

### Penn Treebank Tokenizer

      python3 main.py -dataset ../cranfield -tokenizer ptb
      cp output/tokenized_docs.txt output/tokenized_docs_ptb.txt

### spaCy Tokenizer
      python3 main.py -dataset ../cranfield -tokenizer spacy
      cp output/tokenized_docs.txt output/tokenized_docs_spacy.txt

---

# Part 3 – Inflection Reduction

## Porter Stemmer

Modify `reduce()` in **inflectionReduction.py** to:
        
        return self.porterStemmer(text)

Run:
      
      python3 main.py -dataset ../cranfield

Save output:

        cp output/reduced_docs.txt output/reduced_docs_stemmer.txt
        cp output/reduced_queries.txt output/reduced_queries_stemmer.txt

---

## WordNet Lemmatizer

Modify `reduce()` in **inflectionReduction.py** to:
          
          return self.wordnetLemmatizer(text)

Run:
        
        python3 main.py -dataset ../cranfield

Save output:

      cp output/reduced_docs.txt output/reduced_docs_lemmatizer.txt
      cp output/reduced_queries.txt output/reduced_queries_lemmatizer.txt

---

# Part 4 – Stopword Removal

Stopwords are removed using the **NLTK stopword list**.

Run the pipeline:

# Part 4 – Stopword Removal

Stopwords are removed using the **NLTK stopword list**.

Run the pipeline:
          
          python3 main.py -dataset ../cranfield

Output generated:
            
            output/stopword_removed_docs.txt
            output/stopword_removed_queries.txt

# Final Output Files

The `output/` folder should contain:

    segmented_docs_naive.txt
    segmented_docs_punkt.txt
    segmented_queries_naive.txt
    segmented_queries_punkt.txt
    tokenized_docs_naive.txt
    tokenized_docs_ptb.txt
    tokenized_docs_spacy.txt
    reduced_docs_stemmer.txt
    reduced_docs_lemmatizer.txt
    reduced_queries_stemmer.txt
    reduced_queries_lemmatizer.txt
    stopword_removed_docs.txt
    stopword_removed_queries.txt


---

# Summary

This project demonstrates:

* Sentence segmentation using naive and Punkt methods
* Tokenization using naive, Penn Treebank, and spaCy tokenizers
* Inflection reduction using stemming and lemmatization
* Stopword removal using NLTK
* A modular preprocessing pipeline for information retrieval tasks


              
              
