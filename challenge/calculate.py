import numpy as np
from sklearn.metrics import f1_score


def score(clf, X, y):
    if not hasattr(y, "shape"):
        y = np.array(y)
    if len(y.shape) == 1 or y.shape[1] == 1:
        predictions = clf.predict(X)
    else:
        predictions = np.argmax(clf.predict(X), axis=1)
        y = np.argmax(y, axis=1)
    return f1_score(predictions, y, average="weighted")
