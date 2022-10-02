import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#teht 1

x = pd.Series([1, 2, 3, 4, 6, 7, 8])
y = 2  * x + 3

df = pd.DataFrame({'x' : x, 'y' : y})

df.plot(kind='scatter', x='x', y='y')
plt.plot(df.x, df.y)
plt.show()

#teht 2

X = df.loc[:, ['x']]
y = df.loc[:, ['y']]

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict([[5]])

# varmistetaan suoran yhtälö mallista
coef = model.coef_
inter = model.intercept_
print('Suoran yhtälö on: ')
print(f'y = {coef[0][0]} * x + {inter[0]}')

