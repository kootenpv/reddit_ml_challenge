from data_processing import X_train, X_val, y_train, y_val, X_test

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import RidgeClassifier

import calculate

count_vec = CountVectorizer()
X_train_proc = count_vec.fit_transform(X_train)
X_val_proc = count_vec.transform(X_val)

clf = RidgeClassifier(6)
clf.fit(X_train_proc, y_train)
print("f1_score", calculate.score(clf, X_val_proc, y_val))
