from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import classification_report


class SvmClassification():
    def classify(self,text,score):       
        vectorizer = TfidfVectorizer(min_df=5,
                                 max_df = 0.8,
                                 sublinear_tf=True,
                                 use_idf=True,decode_error='ignore')
        
        train_data = []
        train_labels = []
        test_data = []
        test_labels = []
        
        totalLen = len(text)
        train = int(totalLen*0.7)
        test = totalLen - train
        
        train_data = text[0:train]
        train_labels = score[0:train]
        
        test_data = text[train+1:totalLen]
        test_labels = score[train+1:totalLen]
        
        train_vectors = vectorizer.fit_transform(train_data)
        test_vectors = vectorizer.transform(test_data)
        classifier_rbf = svm.SVC()
        x = list()
        x =  train_vectors[:]
        len2 =len(train_labels)
        
        classifier_rbf.fit(x, train_labels)
        prediction_rbf = classifier_rbf.predict(test_vectors)
         
        prediction_liblinear = classifier_liblinear.predict(test_vectors)
        print(classification_report(test_labels, prediction_rbf))        
        
        