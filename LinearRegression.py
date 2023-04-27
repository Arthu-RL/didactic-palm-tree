from sklearn import datasets
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import scale
import matplotlib.pyplot as plt
import pprint


def p(*args):
    pprint.pprint(*args, sort_dicts=False, width=50)


wine = datasets.load_wine()

x = scale(wine.data)
y = wine.target

# p(wine)
print()
print("x: ", x, sep='\n')
print()
print("y: ", y, sep='\n')
print()
print(x.shape)
print(y.shape)


# Creating a linear regression model.
lin_reg = linear_model.LinearRegression()

# Creating a graphical representation of the attributes in function of the instances.
fig, ax = plt.subplots(figsize=(9, 5))
plt.scatter(x.T[0], y, color='purple')
plt.title("Wine Classification", fontsize=11)
plt.show()

# Creating variables for training and testing.
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Training the model
model = lin_reg.fit(x_train, y_train)

# Predictions
predictions = model.predict(x_test)

print("y_test: ", y_test)
print()
print("Predictions: ", predictions)
print()
print("R^2 value: ", lin_reg.score(x, y))
print()
print("Coefficient factor: ", lin_reg.coef_)
print()
print("Intercept: ", lin_reg.intercept_)
print()
