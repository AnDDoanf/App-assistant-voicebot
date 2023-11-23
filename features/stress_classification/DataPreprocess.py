import pandas as pd           
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re 
import string

class DataPreprocess():
    def __init__(self, data):
        self.data = data 

    def clear_text(self, text):
        text = text.lower()
        text = re.sub('\[.*?\]', '', text)
        text = re.sub("\\W"," ",text) 
        text = re.sub('https?://\S+|www\.\S+', '', text)
        text = re.sub('<.*?>+', '', text)
        text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
        text = re.sub('\n', '', text)
        text = re.sub('\w*\d\w*', '', text)    
        return text

    def remove_stopwords(self, text):
        stpw = set(stopwords.words('english'))
        filtered_text = [word for word in text if word not in stpw]
        return filtered_text

    def lemmatize_words(self, text):
        lemmer = WordNetLemmatizer()
        lemmatized_text = [lemmer.lemmatize(word,pos='v') for word in text]
        return lemmatized_text

    def preprocess(self):
        self.data['text'] = self.data['text'].apply(self.clear_text)
        self.data['text'] = self.data['text'].apply(word_tokenize)
        self.data['text'] = self.data['text'].apply(self.remove_stopwords)
        self.data['text'] = self.data['text'].apply(self.lemmatize_words)
        # create corpus
        self.data['text'] = self.data['text'].apply(lambda x : ' '.join([index for index in x]))
        return self.data