from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.svm import SVC
from DataPreprocess import DataPreprocess
import pandas as pd
import pickle

class SVCModel():
    def __init__(self) -> None:
        filepath = "features/stress_classification/Stress.csv"
        data = pd.read_csv(filepath)
        pre_processor = DataPreprocess(data=data)
        self.data = pre_processor.preprocess()
        
        del filepath, data, pre_processor 

        X = self.data['text']
        y = self.data['label']
        self.vect = TfidfVectorizer()

        self.X_train, self.X_val, self.y_train, self.y_val = train_test_split(X, y, stratify=y, test_size=0.1)
        self.model = SVC()
        
        self.X_train = self.vect.fit_transform(self.X_train)
        self.X_val = self.vect.transform(self.X_val)    

    def train(self):
        self.model.fit(self.X_train, self.y_train)

    def show_evaluate(self):
        self.y_pred = self.model.predict(self.X_val)
        accuracy_score(self.y_val, self.y_pred)
        cm = confusion_matrix(self.y_val, self.y_pred)
        fig = ConfusionMatrixDisplay(confusion_matrix=cm)  
        fig.plot().figure_.savefig('features/stress_classification/model_confussion_matrix.pdf')

    def save_model(self):
        with open('features/stress_classification/model.pkl','wb') as f:
            pickle.dump(self.model,f)
        with open('features/stress_classification/vectorizer.pkl', 'wb') as fin:
            pickle.dump(self.vect, fin)

if __name__ == '__main__':
    model = SVCModel()
    model.train()
    model.show_evaluate()
    model.save_model()