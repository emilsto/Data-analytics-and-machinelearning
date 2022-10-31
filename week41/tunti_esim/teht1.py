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

#Teht 1 ja 2

df = pd.read_csv('titanic-class-age-gender-survived.csv')



X = df.iloc[:, [0,1,2]]
y = df.iloc[:, [-1]]

#Teht 2 lisaa gender ja PClass sarake

# Dummy
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(drop='first'), ['Gender', 'PClass'])], remainder='passthrough')
X = ct.fit_transform(X) # ensimmäisellä kerralla fit_transform


#Opetus ja testidata
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
acc = accuracy_score(y_test, y_pred) 
recall = recall_score(y_test, y_pred) 
precision = precision_score(y_test, y_pred) 

print(f'cm: {cm}')
print(f'acc: {acc}')
print(f'recall: {recall}')
print(f'precision: {precision}')


sns.heatmap(cm, annot=True, fmt='g')
plt.show()

tn, fp, fn, tp = cm.ravel()

Xnew = pd.read_csv('titanic-new.csv')

Xnew = ct.transform(Xnew)

y_pred_new = model.predict(Xnew)
y_pred_new_pros = model.predict_proba(Xnew)

print(f'y_pred_new: {y_pred_new}')
print(f'y_pred_new_pros: {y_pred_new_pros}')
