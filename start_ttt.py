import numpy as np
import pandas as pd
import nltk
from bs4 import BeautifulSoup
import re
import os
import codecs
from sklearn import feature_extraction
import mpld3
stopwords = nltk.corpus.stopwords.words('english')
print stopwords[:10]