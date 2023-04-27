from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics


iris = datasets.load_iris()

print(iris)

x = iris.data
y = iris.target

# Spliting the variables for train and test.
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)
print()

print("y_test: ", y_test)

# Classes of a dataset.
classes = ['Iris Setosa', 'Iris Versicolour', 'Iris Virginica']

# Creating a model.
model = svm.SVC()

# Training the model.
model.fit(x_train, y_train)

print("Model trained: ", model)

# Making predictions.
predict = model.predict(x_test)

# Comparing predictions with the trained model.
acc = metrics.accuracy_score(y_test, predict)

print("Predictions: ", predict)
print()
print("Accuracy: ", acc)


#for i, p in enumerate(predict):
#    print(classes[predict[i]])
