import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, precision_score
from sklearn.preprocessing import StandardScaler
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import ensemble


df = pd.read_csv('iris.csv')


sns.scatterplot(x='petal length (cm)', y='petal width (cm)', hue='Species', data=df)
plt.show()

X = df.iloc[:, 0:4]
y = df.iloc[:, [4]]
columns = X.columns

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)



model = ensemble.RandomForestClassifier(max_depth=5, criterion='gini')
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_pred_pros = model.predict_proba(X_test)

ax = plt.axes()
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='g')
ax.set_title('RF')
plt.show()






