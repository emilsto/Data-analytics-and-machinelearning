import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



df = pd.read_csv("titanic.csv")

#T3 

df.drop(df[df['PClass'] == "*"].index, inplace = True)



sns.swarmplot(data = df, x="PClass", y="Age", hue="Survived")
plt.show()

