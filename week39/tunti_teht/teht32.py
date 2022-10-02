import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import numpy as np
#teht 3

df = pd.read_csv('salary.csv')

X = df.loc[:,['YearsExperience']]
y = df.loc[:, ['Salary']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)


model = LinearRegression()
model.fit(X_train, y_train)

y_predit = model.predict(X_test)

r2 = r2_score(y_test, y_predit)
mae = mean_absolute_error(y_test, y_predit)
mse = mean_squared_error(y_test, y_predit)
rmse = np.sqrt(mse)


print (f'r2 {r2}')
print (f'mae {mae}')
print (f'mse {mse}')
print (f'rmse {rmse}')

plt.scatter(X_test, y_test, color='red')
plt.plot(X_test, y_predit, color='blue')
plt.show()

print (f'uuden tyontekijan palkka 7v kokemuksella on: {model.predict([[7]])}')

