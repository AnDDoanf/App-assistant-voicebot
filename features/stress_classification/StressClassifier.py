import pickle
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from DataPreprocess import DataPreprocess
import pandas as pd

class StressClassifier():
    def __init__(self, query):
        with open('features/stress_classification/model.pkl', 'rb') as f:
            self.model = pickle.load(f)

        with open('features/stress_classification/vectorizer.pkl', 'rb') as f:
            self.vect = pickle.load(f)
        
        self.data = pd.DataFrame({
            'text':[" ".join(query)]
        })

    def pre_processing(self):
        pre_processor = DataPreprocess(data=self.data)
        self.data = pre_processor.preprocess()

    def isStress(self):
        X_valid = self.vect.transform(self.data['text'])
        self.data['predicted'] = self.model.predict(X_valid)
        self.data['predicted']=self.data['predicted'].apply(lambda x : 'Stress' if x == 1 else 'Not Stress')
        print(self.data['predicted'])
        return self.data['predicted']