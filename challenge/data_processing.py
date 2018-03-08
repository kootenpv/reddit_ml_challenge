import just
import pandas as pd
import numpy as np

fnames = sorted(just.glob("data/*"))
titles = []
for fname in fnames:
    titles.extend(list(pd.read_csv(fname)["title"]))

titles = np.array(titles)

class_list = ["Discussion", "News", "Project", "Research"]
classes = {x[0]: x for x in class_list}
class_ind = {x: n for n, x in enumerate(class_list)}

X_train = [x for x in titles if x[0] == "[" and x[2] == "]" and x[1] in classes]
y_train = np.array([classes[x[1]] for x in X_train])
y_train_multi = np.array(pd.get_dummies(y_train))

# hide class labels ;)
X_train = np.array([x[3:] for x in X_train])


X_val = X_train[1::2]
y_val = y_train[1::2]
y_val_multi = y_train_multi[1::2]
X_train = X_train[0::2]
y_train = y_train[0::2]
y_train_multi = y_train_multi[0::2]

X_test = titles[np.array([x[0] != "[" for x in titles])]
