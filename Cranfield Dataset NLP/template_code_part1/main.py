from sentenceSegmentation import SentenceSegmentation
from tokenization import Tokenization
from inflectionReduction import InflectionReduction
from stopwordRemoval import StopwordRemoval

import argparse
import json
import os
from sys import version_info
from util import *



class SearchEngine:

	def __init__(self, args):

		# Perform sentence segmentation based on selected method
		self.args = args
		self.tokenizer = Tokenization()
		self.sentenceSegmenter = SentenceSegmentation()
		self.inflectionReducer = InflectionReduction()
		self.stopwordRemover = StopwordRemoval()

		# Create output folder if not exists
		if not os.path.exists(self.args.out_folder):
			os.makedirs(self.args.out_folder)

	def segmentSentences(self, text):

		# Perform sentence segmentation based on selected method
		if self.args.segmenter == "naive":
			return self.sentenceSegmenter.naive(text)
		elif self.args.segmenter == "punkt":
			return self.sentenceSegmenter.punkt(text)

	def tokenize(self, text):

		# Perform tokenization using selected tokenizer
		if self.args.tokenizer == "naive":
			return self.tokenizer.naive(text)
		elif self.args.tokenizer == "spacy":
			return self.tokenizer.spacyTokenizer(text)
		elif self.args.tokenizer == "ptb":
			return self.tokenizer.pennTreeBank(text)

	def reduceInflection(self, text):

		# Apply stemming or lemmatization based on the selected method
		return self.inflectionReducer.reduce(text)

	def removeStopwords(self, text):

		# Remove common stopwords from tokens using NLTK's stopword list
		return self.stopwordRemover.fromList(text)


	def preprocessQueries(self, queries):

		# Sentence segmentation for queries
		segmentedQueries = []
		for query in queries:
			segmentedQueries.append(self.segmentSentences(query))

		with open(os.path.join(self.args.out_folder, "segmented_queries.txt"), 'w') as f:
			json.dump(segmentedQueries, f)


		# Tokenization for segmented queries
		tokenizedQueries = []
		for query in segmentedQueries:
			tokenizedQueries.append(self.tokenize(query))

		with open(os.path.join(self.args.out_folder, "tokenized_queries.txt"), 'w') as f:
			json.dump(tokenizedQueries, f)


		# Inflection reduction (stemming / lemmatization) for queries
		reducedQueries = []
		for query in tokenizedQueries:
			reducedQueries.append(self.reduceInflection(query))

		with open(os.path.join(self.args.out_folder, "reduced_queries.txt"), 'w') as f:
			json.dump(reducedQueries, f)


		# Stopword removal for queries
		stopwordRemovedQueries = []
		for query in reducedQueries:
			stopwordRemovedQueries.append(self.removeStopwords(query))

		with open(os.path.join(self.args.out_folder, "stopword_removed_queries.txt"), 'w') as f:
			json.dump(stopwordRemovedQueries, f)

		return stopwordRemovedQueries


	def preprocessDocs(self, docs):

		# Sentence segmentation for documents
		segmentedDocs = []
		for doc in docs:
			segmentedDocs.append(self.segmentSentences(doc))

		with open(os.path.join(self.args.out_folder, "segmented_docs.txt"), 'w') as f:
			json.dump(segmentedDocs, f)


		# Tokenization for segmented documents
		tokenizedDocs = []
		for doc in segmentedDocs:
			tokenizedDocs.append(self.tokenize(doc))

		with open(os.path.join(self.args.out_folder, "tokenized_docs.txt"), 'w') as f:
			json.dump(tokenizedDocs, f)


		# Inflection reduction for documents
		reducedDocs = []
		for doc in tokenizedDocs:
			reducedDocs.append(self.reduceInflection(doc))

		with open(os.path.join(self.args.out_folder, "reduced_docs.txt"), 'w') as f:
			json.dump(reducedDocs, f)


		# Stopword removal for documents
		stopwordRemovedDocs = []
		for doc in reducedDocs:
			stopwordRemovedDocs.append(self.removeStopwords(doc))

		with open(os.path.join(self.args.out_folder, "stopword_removed_docs.txt"), 'w') as f:
			json.dump(stopwordRemovedDocs, f)

		return stopwordRemovedDocs


	def evaluateDataset(self):

		# Load Cranfield queries
		query_path = os.path.join(self.args.dataset, "cran_queries.json")
		doc_path = os.path.join(self.args.dataset, "cran_docs.json")

		with open(query_path, 'r') as f:
			queries_json = json.load(f)

		queries = [item["query"] for item in queries_json]
		self.preprocessQueries(queries)

		# Load Cranfield documents
		with open(doc_path, 'r') as f:
			docs_json = json.load(f)

		docs = [item["body"] for item in docs_json]
		self.preprocessDocs(docs)


	def handleCustomQuery(self):
		
		# Allow user to input a custom query 
		# and preprocess it using the same pipeline as the dataset queries
		print("Enter query below")
		query = input()

		self.preprocessQueries([query])

		doc_path = os.path.join(self.args.dataset, "cran_docs.json")

		with open(doc_path, 'r') as f:
			docs_json = json.load(f)

		docs = [item["body"] for item in docs_json]
		self.preprocessDocs(docs)


if __name__ == "__main__":

	# Command-line argument configuration
	parser = argparse.ArgumentParser(description='main.py')

	parser.add_argument('-dataset', default="cranfield",
						help="Path to dataset folder")

	parser.add_argument('-out_folder', default="output",
						help="Path to output folder")

	parser.add_argument('-segmenter', default="punkt",
	                    help="Sentence Segmenter Type [naive|punkt]")

	parser.add_argument('-tokenizer', default="ptb",
	                    help="Tokenizer Type [naive|ptb|spacy]")

	parser.add_argument('-custom', action="store_true",
						help="Take custom query as input")

	args = parser.parse_args()

	# Initialize search engine preprocessing pipeline
	searchEngine = SearchEngine(args)

	# Run pipeline either on dataset or custom query
	if args.custom:
		searchEngine.handleCustomQuery()
	else:
		searchEngine.evaluateDataset()
