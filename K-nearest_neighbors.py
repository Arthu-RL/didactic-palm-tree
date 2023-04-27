# from sklearn import datasets


# iris = datasets.load_iris()

# X = iris.data
# y = iris.target

# print(X, y)
# print(X.shape)
# print(y.shape)


# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# print(X_train.shape)
# print(X_test.shape)
# print(y_train.shape)
# print(y_test.shape)


import pandas as pd
from sklearn import neighbors, metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


data = pd.read_csv('car.data')
print(data.tail(5))
print()


X = data[[
    'buying',
    'maint',
    'safety'
]].values

y = data['class']

print(X.shape)
print(y.shape)


# Converting X (strings) to numbers.
le = LabelEncoder()
for i in range(len(X[0])):
    X[:, i] = le.fit_transform(X[:, i])

print("LabelEncoder: ", X, sep='\n')
print()


# Converting y (labels) to numbers.
label_mapping = {
    'unacc': 0,
    'acc': 1,
    'good': 2,
    'vgood': 3
}

y = y.map(label_mapping)
print(y)


# Creating a model
knn = neighbors.KNeighborsClassifier(n_neighbors=25, weights='uniform')

# Creating variables for training and testing.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# fitting variables from training dataset.
knn.fit(X_train, y_train)

# Prediction after fitting.
predict = knn.predict(X_test)

# Accuracy score
acc = metrics.accuracy_score(y_test, predict)

print(y_test)
print("Predictions:", predict)
print(f'Accuracy: {acc*100}%')
