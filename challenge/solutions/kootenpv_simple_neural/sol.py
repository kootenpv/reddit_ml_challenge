from keras.models import Sequential
from keras.layers import Dense, Dropout, GRU, Embedding
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer

from data_processing import X_train, X_val, y_train, y_val, y_train_multi, y_val_multi, X_test
import calculate

keras_tokenizer = Tokenizer()

keras_tokenizer.fit_on_texts(X_train)

X_train_proc = keras_tokenizer.texts_to_sequences(X_train)
max_length = max([len(x) for x in X_train_proc])
X_train_proc = pad_sequences(X_train_proc, maxlen=max_length)

X_val_proc = keras_tokenizer.texts_to_sequences(X_val)
X_val_proc = pad_sequences(X_val_proc, maxlen=max_length)

input_length = X_train_proc.shape[1]
num_features = X_train_proc.max()
num_classes = y_val_multi.shape[1]

model = Sequential()
model.add(Embedding(input_dim=num_features + 1, output_dim=100, input_length=input_length))
model.add(GRU(units=128, activation='relu', return_sequences=True))
model.add(Dropout(0.5))
model.add(GRU(units=64, activation='relu', return_sequences=True))
model.add(Dropout(0.3))
model.add(GRU(units=32, activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(4, activation='softmax'))

print('Compiling...')
model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.fit(X_train_proc, y_train_multi,
          batch_size=64, epochs=5, validation_split=0.1,
          verbose=1)

print("f1_score", calculate.score(model, X_val_proc, y_val_multi))
# predict first 5 unseen titles
# or go to live new data at reddit.com/r/MachineLearning
# model.predict(pad_sequences(keras_tokenizer.texts_to_sequences(X_test[:5]), maxlen=max_length))
