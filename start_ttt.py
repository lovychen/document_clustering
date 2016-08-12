#! /usr/bin/env python
# -*- coding=utf-8 -*-
import numpy as np
import pandas as pd
import nltk
from bs4 import BeautifulSoup
import re
import os
import codecs
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfVectorizer
import mpld3
stopwords = nltk.corpus.stopwords.words('english')
print stopwords[:10]
print "-" *20
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
# print stemmer.text
class Document_Clustering:
    def __init__(self, url):
        self.url = url

    def Tf_Idf(self):
        # define vectorizer parameters
        tfidf_vectorizer = TfidfVectorizer(max_df=0.8, max_features=200000,
                                           min_df=0.2, stop_words='english',
                                           use_idf=True, tokenizer=tokenize_and_stem, ngram_range=(1, 3))%time
        tfidf_matrix = tfidf_vectorizer.fit_transform(synopses)  # fit the vectorizer to synopses

        print(tfidf_matrix.shape)

    def tokenize_and_stem(self,text):
        # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
        tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
        print tokens
        filtered_tokens = []
        # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
        for token in tokens:
            if re.search('[a-zA-Z]', token):
                filtered_tokens.append(token)
        stems = [stemmer.stem(t) for t in filtered_tokens]
        print stems
        return stems


    def tokenize_only(self,text):  # 对一篇文章进行分词处理（英文）
        # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
        tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
        filtered_tokens = []
        # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
        for token in tokens:
            if re.search('[a-zA-Z]', token):
                filtered_tokens.append(token)
        print filtered_tokens
        return filtered_tokens


if  __name__ == "__main__":
    Document_Clustering("uuu").tokenize_and_stem("hello,what are you doing now,i want to go to school,by some fruits")
