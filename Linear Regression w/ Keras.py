import pandas as pd
import numpy as np

dataset_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data"
features = ["CRIM","ZN","INDUS","CHAS","NOX","RM","AGE","DIS","RAD","TAX","PRATIO","B","LSTAT","MEDV"]

boston = pd.read_csv(dataset_url, sep='\s+', names=features)

X = boston["RM"].values
y = boston["MEDV"].values

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3)


from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(1, input_dim=1))

model.compile(optimizer='sgd', loss='mean_squared_error')

model.fit(X_train, y_train, epochs=100)

mse = model.evaluate(X_test, y_test)
print("MSE sul test set: %.4f" % mse)

y_pred = model.predict(X_test)

weight, bias = model.get_weights()
print("Bias: %.4f" % bias)
print("Peso: %.4f" % weight )

import matplotlib.pyplot as plt

plt.scatter(X_train, y_train, c="green",  edgecolor='white', label="Train set")
plt.scatter(X_test, y_test, c="blue",  edgecolor='white', label="Test set")

plt.xlabel('Numero medio di stanze [RM]')
plt.ylabel('Valore in $1000 [MEDV]')

plt.legend(loc='upper left')

plt.plot(X_test, y_pred, color='red', linewidth=3)

