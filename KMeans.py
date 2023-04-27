# import pandas as pd
from sklearn import datasets
from sklearn import cluster
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.preprocessing import scale


ds = datasets.load_breast_cancer()
print(ds)

x = scale(ds.data)
y = ds.target

print(x.shape)
print(y.shape)
print()

# Creating variables for training and testing.
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Creating a model using KMeans.
model = cluster.KMeans(n_clusters=2, random_state=0, n_init=30)

# Training the model.
model.fit(x_train, y_train)

print("Model: ", model)
print()

# Predictions
prediction = model.predict(x_test)

# Labels of the model.
labels = model.labels_

# Calculating the accuracy.
acc = metrics.accuracy_score(y_test, prediction)

# Seeing the results.
print("y_test: ", y_test)
print()
print("Predictions: ", prediction)
print()
print("Accuracy: ", acc * 100, '%')
