from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Criação de um conjunto de dados.

X = ["O tempo está bom hoje", "Eu gosto de programar em python.", "Eu não gosto de fazer exercícios físicos", "O jogo foi emocionante"]
y = ["clima", "programar", "exercicios", "esportes"]


# Transforma dados de uma matriz com texto em uma matriz numérica.

modelVectorizer = CountVectorizer()
X = modelVectorizer.fit_transform(X)


# Cria e treina um modelo de classificação de texto utilizando o algoritmo Multinomial Naive Bayes

modelClassifier = MultinomialNB()
modelClassifier.fit(X, y)

# Criar dados para testar o modelo

X_test = ["Ta fazendo frio hoje", "Vamos fazer um site", "Vou quero fazer academia", "Não gosto de assistir jogo"]
y_test = ["clima", "programar", "exercicios", "esportes"]

# Mapeamento da matriz texto para uma uma matriz numérica

X_test = modelVectorizer.transform(X_test)

# Previsões

preds = modelClassifier.predict(X_test)

# Cálculo de precisão
acc = accuracy_score(y_test, preds)

print("Accuracy {:.2f}" .format(acc))
